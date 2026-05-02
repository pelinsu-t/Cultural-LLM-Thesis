from vllm import LLM, SamplingParams


def load_llm(model_path: str, max_new_tokens: int = 200):
    model = LLM(model=model_path, dtype="bfloat16")
    sampling_params = SamplingParams(max_tokens=max_new_tokens, temperature=0)

    def llm(prompt: str) -> str:
        outputs = model.generate([prompt], sampling_params)
        return outputs[0].outputs[0].text

    def batch(prompts: list[str]) -> list[str]:
        outputs = model.generate(prompts, sampling_params)
        return [o.outputs[0].text for o in outputs]

    llm.batch = batch
    return llm