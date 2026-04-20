def mock_llm(prompt: str) -> str:
    words = len(prompt.split())
    return f"[MOCK] This is a test answer for a {words}-word prompt."

