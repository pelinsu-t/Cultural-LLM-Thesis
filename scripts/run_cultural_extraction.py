import json
from pathlib import Path
from src.data_loading.loader import load_data
from src.query_understanding.keyword_extraction import extract_keywords_from_data


def save_jsonl(data, path):
    with open(path, "w", encoding="utf-8") as f:
        for entry in data:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

if __name__ == "__main__":
    raw_dir = Path("data/raw")
    processed_dir = Path("data/processed")
    processed_dir.mkdir(parents=True, exist_ok=True)

    input_files = sorted(raw_dir.glob("*.jsonl"))
    if not input_files:
        print("No JSONL files found in data/raw/")
        exit(1)

    for input_path in input_files:
        stem = input_path.stem  # e.g. "de_specific"
        output_path = processed_dir / f"{stem}_features.jsonl"

        if output_path.exists():
            print(f"Skipping {input_path} (output already exists)")
            continue

        print(f"\nProcessing {input_path} ...")
        data = load_data(str(input_path))
        results = extract_keywords_from_data(data, top_n=5)
        save_jsonl(results, output_path)
        print(f"Saved {len(results)} entries to {output_path}")