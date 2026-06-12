import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

# Define paths matching your project layout
BASE_MODEL_NAME = "Qwen/Qwen2.5-14B-Instruct"
LORA_ADAPTER_DIR = "./avca-remediation-lora/final_adapter"
OUTPUT_DIR = "./avca-vllm-ready"

def merge_weights():
    print(f"🚀 Starting merge process...")
    print(f"📦 Loading base model: {BASE_MODEL_NAME}")
    
    # Load the base model in float16 to match your vLLM setup
    base_model = AutoModelForCausalLM.from_pretrained(
        BASE_MODEL_NAME,
        torch_dtype=torch.float16,
        device_map="cpu",  # Load to CPU system RAM first to avoid spilling VRAM
        trust_remote_code=True
    )
    
    # Load the tokenizer
    print("📋 Loading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL_NAME, trust_remote_code=True)
    
    # Wrap the base model with the LoRA adapter layers
    print(f"🩹 Loading LoRA adapter from: {LORA_ADAPTER_DIR}")
    model = PeftModel.from_pretrained(base_model, LORA_ADAPTER_DIR)
    
    # Mathematically fuse the LoRA matrices back into the base layers
    print("🧬 Fusing adapter layers into base model (Merge & Unload)...")
    merged_model = model.merge_and_unload()
    
    # Save the brand new, standalone model weights
    print(f"💾 Saving unified weights to: {OUTPUT_DIR}")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    merged_model.save_pretrained(OUTPUT_DIR, safe_serialization=True)
    tokenizer.save_pretrained(OUTPUT_DIR)
    
    print("🏆 Flawless victory! Your model is completely merged and vLLM-ready.")

if __name__ == "__main__":
    merge_weights()