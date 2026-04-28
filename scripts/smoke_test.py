"""
Quick smoke test — run before check.py to verify the setup is working.
Usage: PYTHONPATH=. python scripts/smoke_test.py
"""
print("1. Testing imports...")
from src.data_loading.loader import load_data
from src.query_understanding.keyword_extraction import extract_keywords_from_data
from src.generation.llm import load_llm
from prompts.prompting_strategies import chain_of_thought_template
print("   OK")

print("2. Testing data loading...")
data = load_data("data/raw/en_specific.jsonl")
assert len(data) > 0, "No data loaded"
print(f"   OK — loaded {len(data)} entries")

print("3. Testing keyword extraction (first 2 entries)...")
results = extract_keywords_from_data(data[:2], top_n=3)
assert len(results) == 2
print(f"   OK — sample: {results[0]['keywords']}")

print("4. Loading LLM (this may take a minute)...")
llm = load_llm("/home/ubuntu/shared/models/llama-3_1_8b_it")
print("   OK")

print("5. Running a single inference...")
test_prompt = data[0]["prompt"]
answer = llm(test_prompt)
assert isinstance(answer, str) and len(answer) > 0
print(f"   OK — answer preview: {answer[:100]}")

print("\nAll checks passed. Ready to run check.py.")