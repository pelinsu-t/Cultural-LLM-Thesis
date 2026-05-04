# this is a script for testing components of the pipeline

from prompts.base import base_template
from prompts.prompting_strategies import get_prompt_fn
from prompts.cultural_injection import get_cultural_injection_fn
from prompts.context_adapter import build_context

from src.generation.llm import load_llm
from scripts.submission_runner import run_experiment

llm = load_llm("/home/ubuntu/shared/models/llama-3_1_8b_it")
# /home/ubuntu/shared/models/aya-expanse-8b


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

experiments = [
    {
        "name": "experiment-1-base",
        "prompt_fn": lambda entry, _lang: base_template(entry["prompt"]),
        "config": {
            "submissionid": "experiment-1-base",
            "system": "base",
            "label": "base",
            "languages": ["de", "el", "en", "es", "it", "pl", "ru", "tr"],
            "modifications": {}
        }
    },
    {
        "name": "experiment-2a-cot",
        "prompt_fn": lambda entry, lang: get_prompt_fn("chain_of_thought", lang)(entry["prompt"]),
        "config": {
            "submissionid": "experiment-2a-cot",
            "system": "prompted",
            "label": "chain-of-thought",
            "languages": ["de", "el", "en", "es", "it", "pl", "ru", "tr"],
            "modifications": {
                "prompt_prefix_english": "Think through the question step by step before answering. "
            "Identify the cultural concepts being asked about, determine which kinds of norms are "
            "relevant (for example social, workplace, family, or religious norms), "
            "and infer the specific culture or cultural setting the user is referring to. "
            "Then interpret the question within that context and provide a culturally appropriate, "
            "accurate, and context-sensitive answer."
            }
        }
    },
    {
        "name": "experiment-2b-persona",
        "prompt_fn": lambda entry, lang: get_prompt_fn("persona", lang)(
            entry["prompt"],
            build_context(entry)["culture"]
        ),
        "config": {
            "submissionid": "experiment-2b-persona",
            "system": "prompted",
            "label": "persona",
            "languages": ["de", "el", "en", "es", "it", "pl", "ru", "tr"],
            "modifications": {
                "prompt_prefix_english": "Answer as someone who lives in {country} and is familiar with its customs, "
                "traditions, and everyday norms. Provide responses that reflect how people "
                "in that culture would typically understand and handle the situation."
            }
        }
    },
    {
        "name": "experiment-2c-uncertainty",
        "prompt_fn": lambda entry, lang: get_prompt_fn("uncertainty", lang)(entry["prompt"]),
        "config": {
            "submissionid": "experiment-2c-uncertainty",
            "system": "prompted",
            "label": "uncertainty-aware",
            "languages": ["de", "el", "en", "es", "it", "pl", "ru", "tr"],
            "modifications": {
                "prompt_prefix_english":
                    "Before answering, carefully evaluate what can be inferred from the question and what cannot. "
                    "Avoid making unsupported assumptions about cultural specifics. When the cultural context is "
                    "ambiguous or your confidence is limited, explicitly acknowledge the uncertainty and answer cautiously."
            }
        }
    },
    {
        "name": "experiment-3-cultural-injection",
        "prompt_fn": lambda entry, lang: get_cultural_injection_fn(lang)(
            **build_context(entry)
        ),
        "config": {
            "submissionid": "experiment-3-cultural-injection",
            "system": "keyword-prompting",
            "label": "cultural-injection-ner",
            "languages": ["de", "el", "en", "es", "it", "pl", "ru", "tr"],
            "modifications": {
                "prompt_prefix_english": "Context: {keywords} \n Culture: {culture}"
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

