from pydantic_settings import BaseSettings
from pydantic import Field
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    qdrant_url: str = "http://127.0.0.1:6333"
    qdrant_collection_name: str = "week2_day13_chunks"

    embedding_model_name: (
        str
    ) = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"

    default_search_limit: int = 3
    merged_search_limit: int = 5

    groq_api_key: str = Field(..., alias="GROQ_API_KEY")
    groq_model_name: str = Field("llama-3.1-8b-instant", alias="GROQ_MODEL")

    model_config = {"env_file": ".env"}


settings = Settings()
