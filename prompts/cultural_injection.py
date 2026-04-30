
def cultural_injection_en(prompt: str, context: str, culture: str) -> str:
    return (f"Context: {context} \n"
        f"Culture: {culture}\n"
        f"Use the given context to inform a culturally appropriate answer.\n\n"
        f"{prompt}")


def cultural_injection_de(prompt: str, context: str, culture: str) -> str:
    return(f"Kontext: {context} \n"
           f"Kultur: {culture} \n"
           f"Nutzen sie den gegebenen Kontext um eine Kulturell angemessene antwort zu geben. \n\n"
           f"{prompt}")


def cultural_injection_el(prompt: str, context: str, culture: str) -> str:
    return (f"Πλαίσιο: {context} \n"
            f"Κουλτούρα: {culture}\n"
            f"Χρησιμοποίησε το δοθέν πλαίσιο για να διαμορφώσεις μια πολιτισμικά κατάλληλη απάντηση.\n\n"
            f"{prompt}")


def cultural_injection_es(prompt: str, context: str, culture: str) -> str:
    return(f"Contexto: {context} \n"
           f"Cultura: {culture} \n"
           f"Utilice el contexto proporcionado para fundamentar una respuesta culturalmente apropiada. \n\n"
           f"{prompt}")


def cultural_injection_it(prompt: str, context: str, culture: str) -> str:
    return(f"Contesto: {context} \n"
           f"Cultura: {culture} \n"
           f"Usa il contesto fornito per formulare una risposta culturalmente appropriata.\n\n"
           f"{prompt}")


def cultural_injection_pl(prompt: str, context: str, culture: str) -> str:
    return (f"Kontekst: {context}\n"
            f"Kultura: {culture}\n"
            f"Wykorzystaj podany kontekst, aby udzielić kulturowo odpowiedniej odpowiedzi.\n\n"
            f"{prompt}")


def cultural_injection_ru(prompt: str, context: str, culture: str) -> str:
    return (f"Контекст: {context} \n"
            f"Культура: {culture}\n"
            f"Используй данный контекст, чтобы сформировать культурно уместный ответ.\n\n"
            f"{prompt}")


def cultural_injection_tr(prompt: str, context: str, culture: str) -> str:
    return(f"Bağlam: {context} \n"
           f"Kültür: {culture} \n"
           f"Verilen bağlamı kullanarak kültürel açıdan uygun bir yanıt ver. \n\n"
           f"{prompt}")


CULTURAL_INJECTION_STRATEGIES = {
    "en": cultural_injection_en,
    "de": cultural_injection_de,
    "el": cultural_injection_el,
    "es": cultural_injection_es,
    "it": cultural_injection_it,
    "pl": cultural_injection_pl,
    "ru": cultural_injection_ru,
    "tr": cultural_injection_tr,
}


def get_cultural_injection_fn(language: str):
    if language not in CULTURAL_INJECTION_STRATEGIES:
        raise ValueError(f"Unsupported language: {language!r}. Supported: {list(CULTURAL_INJECTION_STRATEGIES)}")
    return CULTURAL_INJECTION_STRATEGIES[language]
