from prompts.prompting_strategies import get_prompt_fn
from prompts.context_adapter import build_context
from src.generation.llm import load_llm
from scripts.submission_runner import run_experiment

llm = load_llm("/home/ubuntu/shared/models/llama-3_1_8b_it")

input_files = [
    ("data/processed/de_specific_features.jsonl", "de", "specific"),
    ("data/processed/de_unspecific_features.jsonl", "de", "unspecific"),
    ("data/processed/el_specific_features.jsonl", "el", "specific"),
    ("data/processed/el_unspecific_features.jsonl", "el", "unspecific"),
    ("data/processed/en_specific_features.jsonl", "en", "specific"),
    ("data/processed/en_unspecific_features.jsonl", "en", "unspecific"),
    ("data/processed/es_specific_features.jsonl", "es", "specific"),
    ("data/processed/es_unspecific_features.jsonl", "es", "unspecific"),
    ("data/processed/it_specific_features.jsonl", "it", "specific"),
    ("data/processed/it_unspecific_features.jsonl", "it", "unspecific"),
    ("data/processed/pl_specific_features.jsonl", "pl", "specific"),
    ("data/processed/pl_unspecific_features.jsonl", "pl", "unspecific"),
    ("data/processed/ru_specific_features.jsonl", "ru", "specific"),
    ("data/processed/ru_unspecific_features.jsonl", "ru", "unspecific"),
    ("data/processed/tr_specific_features.jsonl", "tr", "specific"),
    ("data/processed/tr_unspecific_features.jsonl", "tr", "unspecific"),
]

experiment = {
    "name": "experiment-2d-combined",
    "prompt_fn": lambda entry, lang: get_prompt_fn("combined", lang)(
        entry["prompt"],
        build_context(entry)["culture"]
    ),
    "config": {
        "submissionid": "experiment-2d-combined",
        "system": "prompted",
        "label": "combined",
        "languages": ["de", "el", "en", "es", "it", "pl", "ru", "tr"],
        "modifications": {
            "prompt_prefix_english": "Reason step by step before answering. Identify the cultural concepts and relevant norms "
                "(e.g., social, workplace, family), and infer the cultural context. "
                "Answer as a local from {country}, reflecting realistic customs, traditions, and expectations. "
                "Avoid unsupported assumptions. If cultural details are uncertain, acknowledge this and respond cautiously. "
                "Give a clear and culturally appropriate answer."
        }
    }
}

print(f"\nRunning {experiment['name']}...")
run_experiment(
    input_files=input_files,
    output_dir=f"data/output/{experiment['name']}",
    llm=llm,
    experiment_config=experiment["config"],
    prompt_fn=experiment["prompt_fn"],
)
print(f"Done — check data/submissions/{experiment['name']}.zip")