from keybert import KeyBERT
from src.data_loading.loader import load_data
from src.query_understanding.cultural_markers import detect_cultural_markers
from tqdm import tqdm
from dataclasses import dataclass
from dataclasses import asdict

# formatting how keywords should be stored
@dataclass
class Keyword:
    keyword: str
    score: float

# formatting how results should be stored
@dataclass
class NERResult:
    text: str
    keywords: list
    culture_terms: list

    @property
    def has_explicit_culture(self) -> bool:
        return len(self.culture_terms) > 0

    @property
    def n_keywords(self) -> int:
        return len(self.keywords)

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


def format_keywords(keywords: list) -> list[Keyword]:
    return [Keyword(keyword=str(k), score=float(s)) for k, s in keywords]



def extract_keywords_from_data(data: list, top_n: int = 5) -> list:
    """
    Run keyword extraction over a list of prompt dictionaries.
    Returns a new list of enriched dictionaries with keywords and cultural markers.
    """
    output = []

    for entry in tqdm(data, desc="Processing prompts"):
        prompt_id = entry.get("id")
        prompt_text = entry.get("prompt", "")

        keywords = extract_keywords(prompt_text, top_n=top_n)
        formatted_keywords = format_keywords(keywords)
        marker_info = detect_cultural_markers(prompt_text)

        result = NERResult(
            text=prompt_text,
            keywords=formatted_keywords,
            culture_terms=marker_info["culture_terms"],
        )

        output.append({
            "id": prompt_id,
            "prompt": prompt_text,
            "keywords": [asdict(k) for k in result.keywords],
            "n_keywords": result.n_keywords,  # from the @property!
            "has_explicit_culture": result.has_explicit_culture,  # from the @property!
            "culture_terms": result.culture_terms,
        })

    return output
