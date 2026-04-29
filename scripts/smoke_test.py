"""
Quick smoke test — run on the server before check.py to verify the full pipeline.
Usage: PYTHONPATH=. python scripts/smoke_test.py
"""
N_SAMPLES = 10
LANG = "en"
DATA_PATH = "data/processed/en_specific_features.jsonl"
MODEL_PATH = "/home/ubuntu/shared/models/llama-3_1_8b_it"

print("1. Testing imports...")
from src.data_loading.loader import load_data
from src.generation.llm import load_llm
from prompts.base import base_template
from prompts.prompting_strategies import get_prompt_fn
from prompts.cultural_injection import get_cultural_injection_fn
from prompts.context_adapter import build_context
print("   OK")

print(f"2. Loading data ({N_SAMPLES} samples)...")
data = load_data(DATA_PATH)[:N_SAMPLES]
assert len(data) == N_SAMPLES, f"Expected {N_SAMPLES} entries, got {len(data)}"
print(f"   OK — loaded {len(data)} entries")

print("3. Loading LLM (this may take a minute)...")
llm = load_llm(MODEL_PATH)
print("   OK")

strategies = [
    ("base",             lambda entry, _lang: base_template(entry["prompt"])),
    ("chain_of_thought", lambda entry, lang:  get_prompt_fn("chain_of_thought", lang)(entry["prompt"])),
    ("persona",          lambda entry, lang:  get_prompt_fn("persona", lang)(entry["prompt"], build_context(entry)["culture"])),
    ("uncertainty",      lambda entry, lang:  get_prompt_fn("uncertainty", lang)(entry["prompt"])),
    ("cultural_injection", lambda entry, lang: get_cultural_injection_fn(lang)(**build_context(entry))),
]

for strategy_name, prompt_fn in strategies:
    print(f"\n{'='*60}")
    print(f"Strategy: {strategy_name}")
    print(f"{'='*60}")
    for i, entry in enumerate(data):
        formatted = prompt_fn(entry, LANG)
        answer = llm(formatted)
        print(f"\n--- Sample {i+1} (id={entry['id']}) ---")
        print(f"[PROMPT SENT TO LLM]\n{formatted}")
        print(f"[MODEL OUTPUT]\n{answer}")

print("\nSmoke test complete.")
