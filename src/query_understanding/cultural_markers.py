import re
import pycountry


def get_country_terms():
    countries = []

    for country in pycountry.countries:
        countries.append(country.name.lower())

        # Optional: include common names
        if hasattr(country, "official_name"):
            countries.append(country.official_name.lower())

    return list(set(countries))


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