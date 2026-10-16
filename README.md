# Cross-Cultural LLM Robustness
Evaluation pipeline for cultural awareness in multilingual LLMs: six prompting strategies across Llama 3.1 8B and Aya Expanse 8B in eight languages. Code for our CLEF 2026 ELOQUENT paper.
---

## Project structure
 
```
Thesis-Project/
│
├── data/
│   ├── raw/                  # Input JSONL files (one per language × type)
│   ├── processed/            # NER-enriched JSONL files (output of extraction step)
│   ├── output/               # Per-experiment output files
│   └── submissions/          # Final submission zips, ready to send
│
├── prompts/
│   ├── base.py               # Experiment 1 — no modification
│   ├── prompting_strategies.py  # Experiment 2 — CoT, persona, uncertainty
│   ├── cultural_injection.py    # Experiment 3 — NER context injection
│   └── context_adapter.py    # Converts NER output into template-ready strings
│
├── scripts/
│   ├── run_cultural_extraction.py  # Step 1: run NER over raw data → processed/
│   ├── submission_runner.py        # Step 2: run all experiments → submissions/
│   └── check.py                    # Quick sanity checks
│
├── src/
│   ├── data_loading/
│   │   └── loader.py          # Loads JSONL files
│   ├── generation/
│   │   ├── mock_llm.py        # Fake LLM for pipeline testing (will be swapped)
│   │   └── writer.py          # Writes JSONL output + metadata + zip
│   └── query_understanding/
│       ├── keyword_extraction.py   # KeyBERT-based keyword extraction
│       └── cultural_markers.py     # Country/culture term detection (regex, word-bounded)
│
├── docs/
│   └── instructions.md        # Submission format requirements
│
└── requirements.txt
```
---

## How to run
### Step 1 — Extract cultural features
 
Runs NER and cultural marker detection over raw data. Only needs to be done once.

### Step 2 — Run experiments
 
Runs all 5 experiment conditions and produces one submission zip per condition.

Output will appear in `data/submissions/`.

Each zip contains:
```
submission_metadata.json
en_specific.jsonl
en_unspecific.jsonl
```

---

## Submission format
 
Output follows the format required by the evaluation organization:
 
```jsonl
{"id": "1-1", "prompt": "...", "answer": "..."}
```
 
With a `submission_metadata.json` describing the experiment condition (model, modifications, prompting strategy).
