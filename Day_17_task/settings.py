from pydantic_settings import BaseSettings
from pydantic import Field
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    default_search_limit: int = 3
    merged_search_limit: int = 5

    # Guardrails thresholds
    min_top_score_for_answer: float = 0.5
    min_avg_score_for_answer: float = 0.4
    min_results_for_answer: int = 2

    groq_api_key: str = Field(..., alias="GROQ_API_KEY")
    groq_model_name: str = Field("llama-3.1-8b-instant", alias="GROQ_MODEL")

    model_config = {"env_file": ".env"}


settings = Settings()
