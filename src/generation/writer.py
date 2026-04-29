import json
from pathlib import Path
from datetime import date
import shutil


def write_jsonl(entries: list, path: str):
    """
    Write a list of {id, prompt, answer} dicts to a JSONL file.
    """
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for entry in entries:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def write_metadata(output_dir: str, experiment_config: dict):
    """
    Write submission_metadata.json to the output directory.
    """
    metadata = {
        "team": experiment_config.get("team", "su"),
        "system": experiment_config.get("system", "base_system"),
        "model": experiment_config.get("model", "mock-llm"),
        "submissionid": experiment_config.get("submissionid", "experiment-1"),
        "date": str(date.today()),
        "label": experiment_config.get("label", ""),
        "languages": experiment_config.get("languages", ["en"]),
        "modifications": experiment_config.get("modifications", {}),
    }
    path = Path(output_dir) / "submission_metadata.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)


def zip_submission(output_dir: str, zip_name: str):
    """
    Zip the output directory into a submission archive.
    """
    shutil.make_archive(zip_name, "zip", output_dir)
    print(f"Submission saved to {zip_name}.zip")