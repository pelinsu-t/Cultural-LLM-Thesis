def chain_of_thought_template(prompt: str) -> str:
    return ("Consider the following question carefully, reasoning step by step: understand which culture"
            " the user is asking about, evaluate the specific context, and answer appropriately. \n\n"
            f"{prompt}")

def persona_template(prompt: str, country: str) -> str:
    return(f"You are a local in {country}. You are knowledgeable in the local customs and traditions.\n\n"
           f"{prompt}")

def uncertainty_template(prompt:str) -> str:
    return (
        "Before you answer, carefully evaluate what you know and what you don't. "
        "Express uncertainty if you are not confident about cultural specifics.\n\n"
        f"{prompt}")

