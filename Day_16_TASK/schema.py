from pydantic import BaseModel


class RagRequest(BaseModel):
    question: str
    limit: int = 3


class RagResponse(BaseModel):
    question: str
    normalized_query: str
    answer: str
    sources: list
