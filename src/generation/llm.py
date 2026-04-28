import torch
from transformers import AutoTokenizer, pipeline


def load_llm(model_path: str, max_new_tokens: int = 512):
    """
    Load Llama-3.1-8B-Instruct (or any chat model) and return a callable
    with the same interface as mock_llm: takes a prompt string, returns a string.

    model_path: local folder path or HuggingFace model ID
    """
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    pipe = pipeline(
        "text-generation",
        model=model_path,
        tokenizer=tokenizer,
        device_map="auto",
        torch_dtype=torch.bfloat16,
    )

    def llm(prompt: str) -> str:
        messages = [{"role": "user", "content": prompt}]
        output = pipe(
            messages,
            max_new_tokens=max_new_tokens,
            do_sample=False,
        )
        return output[0]["generated_text"][-1]["content"]

    return llm