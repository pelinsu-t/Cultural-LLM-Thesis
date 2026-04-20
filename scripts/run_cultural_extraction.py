import json
from src.data_loading.loader import load_data
from src.query_understanding.keyword_extraction import extract_keywords_from_data


def save_jsonl(data, path):
    with open(path, "w", encoding="utf-8") as f:
        for entry in data:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

if __name__ == "__main__":
    input_path = "data/raw/en_specific.jsonl"
    output_path = "data/processed/en_specific_features.jsonl"

    data = load_data(input_path)
    results = extract_keywords_from_data(data, top_n=5)
    save_jsonl(results, output_path)

    print(f"Saved {len(results)} entries to {output_path}")