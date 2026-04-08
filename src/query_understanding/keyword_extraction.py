from keybert import KeyBERT
from src.data_loading.loader import load_data

model = KeyBERT(model="paraphrase-multilingual-MiniLM-L12-v2")

def extract_keywords(text: str, top_n: int = 5) -> list:
    """
    Extract keywords from a single prompt.
    Returns a list of (keyword, score) tuples.
    """
    return model.extract_keywords(
        text,
        keyphrase_ngram_range=(1, 2),
        top_n=top_n
    )


def extract_keywords_from_data(data: list, top_n: int = 5) -> list:
    """
    Run keyword extraction over a list of prompt dictionaries.
    Adds a 'keywords' key to each entry in place.
    """
    for entry in data:
        entry["keywords"] = extract_keywords(entry["prompt"], top_n=top_n)
    return data

# example usage to check if it works
# path1 = "/Users/pelinsutopaloglu/Thesis/Thesis-Project/data/raw/en_unspecific.jsonl"
# data = load_data(path1)
# print(extract_keywords(data[7]["prompt"]))

# use python -m src.query_understanding.keyword_extraction