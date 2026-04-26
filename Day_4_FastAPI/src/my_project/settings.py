from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "My API"
    environment: str = "dev"
    debug: bool = True

    # 👇 Day 9 ke liye IMPORTANT
    database_url: str
    qdrant_url: str


def get_settings():
    return Settings()
