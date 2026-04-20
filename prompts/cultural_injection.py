def cultural_injection_template(prompt: str, context: str, culture: str) -> str:
    return (f"Context: {context} \n"
        f"Culture: {culture}\n"
        f"Use the context above to inform a culturally appropriate answer.\n\n"
        f"{prompt}")