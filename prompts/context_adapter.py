def build_context(entry: dict) -> dict:
    """
    Takes a processed NER entry and returns the values
    needed to fill the prompt templates.
    """
    keywords = [kw["keyword"] for kw in entry.get("keywords", [])]
    culture_terms = entry.get("culture_terms", [])

    return {
        "prompt": entry["prompt"],
        "context": "Keywords: " + ", ".join(keywords) if keywords else "",
        "culture": culture_terms[0] if culture_terms else "unknown",
    }