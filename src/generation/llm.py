import torch
from transformers import AutoTokenizer, pipeline
from tqdm import tqdm


def load_llm(model_path: str, max_new_tokens: int = 200, batch_size: int = 16):
    tokenizer = AutoTokenizer.from_pretrained(model_path, use_fast=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "left"

    # Flash Attention 2 gives significant speedup on Ampere+ GPUs; fall back if unavailable
    try:
        pipe = pipeline(
            "text-generation",
            model=model_path,
            tokenizer=tokenizer,
            device_map="auto",
            torch_dtype=torch.bfloat16,
            model_kwargs={"attn_implementation": "flash_attention_2"},
        )
    except (ImportError, ValueError):
        pipe = pipeline(
            "text-generation",
            model=model_path,
            tokenizer=tokenizer,
            device_map="auto",
            torch_dtype=torch.bfloat16,
        )

    def llm(prompt: str) -> str:
        messages = [{"role": "user", "content": prompt}]
        out = pipe(messages, max_new_tokens=max_new_tokens, do_sample=False)
        return out[0]["generated_text"][-1]["content"]

    def batch(prompts: list[str]) -> list[str]:
        all_messages = [[{"role": "user", "content": p}] for p in prompts]
        results = []
        for i in tqdm(range(0, len(all_messages), batch_size), desc="batches"):
            chunk = all_messages[i:i + batch_size]
            outputs = pipe(
                chunk,
                max_new_tokens=max_new_tokens,
                do_sample=False,
                batch_size=batch_size,
                padding=True,
                truncation=True,
            )
            results.extend(o[0]["generated_text"][-1]["content"] for o in outputs)
        return results

    llm.batch = batch
    return llm