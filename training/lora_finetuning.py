import torch
import os
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, Trainer, DataCollatorForSeq2Seq
from peft import LoraConfig, get_peft_model, TaskType

# 1. Paths and Configuration
model_name = "Qwen/Qwen2-7B-Instruct"
output_dir = "./fine-tuned-qwen"

print("🚀 Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token

# 2. Load Dataset & Apply Qwen Chat Template
print("📦 Loading and processing dataset...")
# dataset = load_dataset("json", data_files={"train": "training/dataset.jsonl"}, split="train")
# Hardcoded absolute path to guarantee the file is found instantly
dataset_path = "/workspace/shared/avca-copilot/training/dataset.jsonl"

print(f"📦 Loading dataset explicitly from: {dataset_path}")
dataset = load_dataset("json", data_files={"train": dataset_path}, split="train")
def format_and_tokenize(example):
    # Safely format the JSONL messages into Qwen's native chat structure
    text = tokenizer.apply_chat_template(example["messages"], tokenize=False, add_generation_prompt=False)
    tokenized = tokenizer(text, max_length=512, truncation=True)
    # For causal LM, labels are identical to input_ids
    tokenized["labels"] = tokenized["input_ids"].copy()
    return tokenized

tokenized_dataset = dataset.map(format_and_tokenize, remove_columns=dataset.column_names)

print("🧠 Loading base model in bfloat16...")
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)

# 3. Configure LoRA Parameters
print("⚙️ Applying Parameter-Efficient LoRA layers...")
lora_config = LoraConfig(
    r=8,
    lora_alpha=16,
    target_modules=["q_proj", "v_proj"], # Target key attention layers for rapid shifting
    lora_dropout=0.05,
    bias="none",
    task_type=TaskType.CAUSAL_LM
)
model = get_peft_model(model, lora_config)
model.print_trainable_parameters()

# 4. Training Hyperparameters
training_args = TrainingArguments(
    output_dir=output_dir,
    per_device_train_batch_size=1,     # Keeps VRAM footprint minimal
    gradient_accumulation_steps=4,     # Simulates a stable batch size of 4
    learning_rate=2e-4,
    num_train_epochs=3,
    logging_steps=2,
    save_strategy="no",                # Prevents disk write delays during the hackathon
    optim="adamw_torch",
    bf16=True,                         # Dynamic range acceleration for AMD ROCm
    remove_unused_columns=False
)

# 5. Initialize Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
    data_collator=DataCollatorForSeq2Seq(tokenizer, pad_to_multiple_of=8, return_tensors="pt", padding=True)
)

# 6. Execute Training
print("🔥 Launching training loop on GPU...")
trainer.train()

print(f"💾 Saving fine-tuned adapter weights to {output_dir}...")
trainer.model.save_pretrained(output_dir)
tokenizer.save_pretrained(output_dir)
print("🏁 Training Complete! Run your presentation benchmarks.")