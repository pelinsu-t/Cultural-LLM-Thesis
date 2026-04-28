# this is a script for testing components of the pipeline

from prompts.base import base_template
from prompts.prompting_strategies import chain_of_thought_template, persona_template, uncertainty_template
from prompts.cultural_injection import cultural_injection_template
from prompts.context_adapter import build_context

from src.generation.llm import load_llm
from scripts.submission_runner import run_experiment

llm = load_llm("/home/ubuntu/shared/models/llama-3_1_8b_it")


input_files = [
    ("data/processed/en_specific_features.jsonl", "en", "specific"),
    #("data/processed/en_unspecific_features.jsonl", "en", "unspecific"),
]

experiments = [
    {
        "name": "experiment-1-base",
        "prompt_fn": lambda entry: base_template(entry["prompt"]),
        "config": {
            "submissionid": "experiment-1-base",
            "label": "base",
            "languages": ["en"],
            "modifications": {}
        }
    },
    {
        "name": "experiment-2a-cot",
        "prompt_fn": lambda entry: chain_of_thought_template(entry["prompt"]),
        "config": {
            "submissionid": "experiment-2a-cot",
            "label": "chain-of-thought",
            "languages": ["en"],
            "modifications": {
                "prompt_prefix_english": "Consider the following question carefully..."
            }
        }
    },
    {
        "name": "experiment-2b-persona",
        "prompt_fn": lambda entry: persona_template(
            entry["prompt"],
            build_context(entry)["culture"]
        ),
        "config": {
            "submissionid": "experiment-2b-persona",
            "label": "persona",
            "languages": ["en"],
            "modifications": {
                "prompt_prefix_english": "You are a local in {culture}..."
            }
        }
    },
    {
        "name": "experiment-2c-uncertainty",
        "prompt_fn": lambda entry: uncertainty_template(entry["prompt"]),
        "config": {
            "submissionid": "experiment-2c-uncertainty",
            "label": "uncertainty-aware",
            "languages": ["en"],
            "modifications": {
                "prompt_prefix_english": "Before you answer, evaluate uncertainty..."
            }
        }
    },
    {
        "name": "experiment-3-cultural-injection",
        "prompt_fn": lambda entry: cultural_injection_template(
            **build_context(entry)
        ),
        "config": {
            "submissionid": "experiment-3-cultural-injection",
            "label": "cultural-injection-ner",
            "languages": ["en"],
            "modifications": {
                "prompt_prefix_english": "Context: {keywords}\nCulture: {culture}"
            }
        }
    },
]

for exp in experiments:
    print(f"\nRunning {exp['name']}...")
    run_experiment(
        input_files=input_files,
        output_dir=f"data/output/{exp['name']}",
        llm=llm,
        experiment_config=exp["config"],
        prompt_fn=exp["prompt_fn"],
    )
    print(f"Done — check data/submissions/{exp['name']}.zip")

