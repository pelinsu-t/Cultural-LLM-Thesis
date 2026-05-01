import os
from src.data_loading.loader import load_data
from src.generation.writer import write_jsonl, write_metadata, zip_submission
from tqdm import tqdm


def run_experiment(
    input_files: list,
    output_dir: str,
    llm,
    experiment_config: dict,
    prompt_fn=None,
):
    """
    Run a full experiment and produce a submission-ready zip.

    input_files: list of (path, language, type) tuples
    output_dir:  where to write output files
    llm:         any function that takes a prompt string and returns a string
    experiment_config: metadata describing this experiment
    """
    if prompt_fn is None:
        prompt_fn = lambda entry, _lang: entry["prompt"]

    for path, language, split_type in input_files:
        output_path = f"{output_dir}/{language}_{split_type}.jsonl"
        if os.path.exists(output_path):
            print(f"Skipping {output_path} (already exists)")
            continue

        data = load_data(path)

        print(f"Generating {len(data)} prompts for {language}_{split_type}...")
        prompts = [prompt_fn(entry, language) for entry in data]
        answers = llm.batch(prompts)
        entries = [
            {"id": entry["id"], "prompt": entry["prompt"], "answer": ans}
            for entry, ans in zip(data, answers)
        ]

        write_jsonl(entries, output_path)
        print(f"Written {len(entries)} entries to {output_path}")

    write_metadata(output_dir, experiment_config)
    zip_submission(output_dir, f"data/submissions/{experiment_config['submissionid']}")