from src.data_loading.loader import load_data
from src.generation.writer import write_jsonl, write_metadata, zip_submission


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
        data = load_data(path)

        entries = []
        for entry in data:
            formatted_prompt = prompt_fn(entry, language)
            answer = llm(formatted_prompt)
            entries.append({
                "id": entry["id"],
                "prompt": entry["prompt"], # saving the original prompt not the modified version
                "answer": answer,
            })

        output_path = f"{output_dir}/{language}_{split_type}.jsonl"
        write_jsonl(entries, output_path)
        print(f"Written {len(entries)} entries to {output_path}")

    write_metadata(output_dir, experiment_config)
    zip_submission(output_dir, f"data/submissions/{experiment_config['submissionid']}")