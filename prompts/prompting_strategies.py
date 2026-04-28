def chain_of_thought_template(prompt: str) -> str:
    return ("Think through the question step by step before answering. "
            "Identify the cultural concepts being asked about, determine which kinds of norms are "
            "relevant (for example social, workplace, family, or religious norms), "
            "and infer the specific culture or cultural setting the user is referring to. "
            "Then interpret the question within that context and provide a culturally appropriate, "
            "accurate, and context-sensitive answer. \n\n"
            f"{prompt}")

def persona_template(prompt: str, country: str) -> str:
    return(f"Answer as someone who lives in {country} and is familiar with its customs, "
           f"traditions, and everyday norms. Provide responses that reflect how people "
           f"in that culture would typically understand and handle the situation.\n\n"
           f"{prompt}")

def uncertainty_template(prompt:str) -> str:
    return (
        "Before answering, carefully evaluate what can be inferred from the question and what cannot. "
        "Avoid making unsupported assumptions about cultural specifics. When the cultural context is "
        "ambiguous or your confidence is limited, explicitly acknowledge the uncertainty and answer cautiously.\n\n"
        f"{prompt}")

def combined_template(prompt:str, country:str) -> str:
    return ("Reason step by step before answering. Identify the cultural concepts and relevant norms "
            "(e.g., social, workplace, family), and infer the cultural context. "
            f"Answer as a local from {country}, reflecting realistic customs, traditions, and expectations. "
            "Avoid unsupported assumptions. If cultural details are uncertain, acknowledge this and respond cautiously. "
            "Give a clear and culturally appropriate answer.\n\n"
        f"{prompt}")

