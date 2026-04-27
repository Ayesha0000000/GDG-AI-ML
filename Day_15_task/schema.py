from pydantic import BaseModel


class RagRequest(BaseModel):
    question: str
    limit: int = 3


class RagResponse(BaseModel):
    question: str
    answer: str
    sources: list
