import os

def generate(prompt: str) -> str:
    provider = os.getenv("LLM_PROVIDER", "demo").lower()

    if provider == "demo":
        return (
            "Demo response: the answer should be grounded in the approved "
            "policy/knowledge source. In a production deployment, the "
            "configured enterprise LLM would generate the final response "
            "with citations and guardrails."
        )

    if provider == "openai":
        from langchain_openai import ChatOpenAI
        model = ChatOpenAI(model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"), temperature=0)
        return model.invoke(prompt).content

    if provider == "vertex":
        from langchain_google_vertexai import ChatVertexAI
        model = ChatVertexAI(
            model_name=os.getenv("VERTEX_MODEL", "gemini-2.5-flash"),
            temperature=0,
        )
        return model.invoke(prompt).content

    raise ValueError(f"Unsupported LLM_PROVIDER: {provider}")
