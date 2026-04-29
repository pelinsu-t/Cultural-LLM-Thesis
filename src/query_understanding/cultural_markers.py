import re
from babel import Locale

SUPPORTED_LOCALES = ["en", "de", "el", "es", "it", "pl", "ru", "tr"]

def get_country_terms():
    terms = set()
    for lang in SUPPORTED_LOCALES:
        for name in Locale(lang).territories.values():
            terms.add(name.lower())
    return list(terms)


CULTURE_TERMS = get_country_terms()


def detect_cultural_markers(text: str):
    text_lower = text.lower()

    found_terms = [
        term for term in CULTURE_TERMS
        if re.search(rf"\b{term}\b", text_lower, re.IGNORECASE)
    ]

    return {
        "has_explicit_culture": len(found_terms) > 0,
        "culture_terms": found_terms
    }