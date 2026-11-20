from crewai import LLM
from src.config.settings import settings

def get_llm() -> LLM:
    return LLM(
        model=settings.model_name,
        temperature=settings.temperature,
        api_key=settings.openai_api_key
    )