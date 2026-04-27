from pydantic_settings import BaseSettings
from pydantic import Field
from dotenv import load_dotenv

# 🔥 Ensure .env load ho jaye
load_dotenv()


class Settings(BaseSettings):
    # Qdrant settings
    qdrant_url: str = "http://127.0.0.1:6333"
    qdrant_collection_name: str = "week2_day13_chunks"
    default_search_limit: int = 3

    # Embedding model
    embedding_model_name: (
        str
    ) = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"

    # Groq settings (IMPORTANT)
    groq_api_key: str = Field(..., alias="GROQ_API_KEY")
    groq_model_name: str = Field("llama-3.1-8b-instant", alias="GROQ_MODEL")

    # 🔥 Pydantic v2 config (INDENTATION FIXED)
    model_config = {"env_file": ".env"}


# 🔥 Create instance
settings = Settings()
