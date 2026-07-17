from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    openai_api_key: str
    serper_api_key: str
    model_name: str = "gpt-4.1-mini"
    temperature: float = 0.2
    verbose: bool = True

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

settings = Settings()