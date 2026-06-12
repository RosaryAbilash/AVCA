import torch
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import LoraConfig, get_peft_model
from trl import SFTTrainer, SFTConfig

# =================================================================
# 1. CONFIGURATION
# =================================================================
MODEL_ID = "Qwen/Qwen2.5-14B-Instruct"
DATASET_PATH = "dataset.jsonl"
# OUTPUT_DIR = "avca-remediation-lora"
OUTPUT_DIR = "avca-remediation-lora-bf16"

print(f"🚀 Initializing FINETUNE_001 Pipeline...")
print(f"📦 Loading Model: {MODEL_ID}")

# =================================================================
# 2. LOAD DATASET & FORMAT PROMPTS
# =================================================================
dataset = load_dataset(
    "json",
    data_files=DATASET_PATH,
    split="train"
)

def format_instruction(example):
    """
    Pre-formats the synthetic data into Qwen's native ChatML structure.
    """
    return {
        "text": f"""<|im_start|>system
{example['instruction']}<|im_end|>
<|im_start|>user
{example['input']}<|im_end|>
<|im_start|>assistant
{example['output']}<|im_end|>"""
    }

dataset = dataset.map(format_instruction)

# =================================================================
# 3. LOAD MODEL & TOKENIZER
# =================================================================
tokenizer = AutoTokenizer.from_pretrained(
    MODEL_ID,
    trust_remote_code=True
)
tokenizer.pad_token = tokenizer.eos_token
tokenizer.model_max_length = 2048

model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    dtype=torch.float16,          
    device_map="auto",
    trust_remote_code=True
)

# =================================================================
# 4. LoRA CONFIGURATION & CHECKPOINTING
# =================================================================
lora_config = LoraConfig(
    r=16,
    lora_alpha=32,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)

model = get_peft_model(model, lora_config)

# Enable memory optimizations & gradient flow
model.gradient_checkpointing_enable()
model.enable_input_require_grads() 

model.print_trainable_parameters()

# =================================================================
# 5. TRAINING ARGUMENTS
# =================================================================
training_args = SFTConfig(             
    output_dir=OUTPUT_DIR,
    # per_device_train_batch_size=2,
    # gradient_accumulation_steps=4,
    lr_scheduler_type="cosine",
    warmup_steps=50,             
    save_strategy="epoch",
    save_total_limit=2,            
    logging_steps=10,
    num_train_epochs=2,            
    max_steps=-1,
    learning_rate=2e-5,            
    weight_decay=0.01,             
    max_grad_norm=0.3,             
    fp16=True,
    bf16=False,
    # --- THE DATA BOMB FIXES ---
    max_length=1024,               # <-- CHANGED from 2048: Chops massive documents in half
    per_device_train_batch_size=1, # <-- CHANGED from 2: Processes 1 at a time
    gradient_accumulation_steps=8,
    optim="adamw_torch",
    remove_unused_columns=False,
    dataset_text_field="text",    
              # <-- CHANGED FROM max_seq_length TO max_length
)

# =================================================================
# 6. INITIALIZE SFT TRAINER
# =================================================================
# Using tokenizer=tokenizer for maximum compatibility across TRL 0.8.x - 0.10+
trainer = SFTTrainer(
    model=model,
    train_dataset=dataset,
    processing_class=tokenizer,   
    args=training_args             # <-- cleanly passing the config packing everything
)

# =================================================================
# 7. EXECUTE TRAINING
# =================================================================
print("🔥 Starting LoRA Fine-Tuning...")
trainer.train()

# Save the final LoRA adapter weights
trainer.model.save_pretrained(f"{OUTPUT_DIR}/final_adapter")
tokenizer.save_pretrained(f"{OUTPUT_DIR}/final_adapter")

print(f"✅ Training Complete! Weights saved to: {OUTPUT_DIR}/final_adapter")