from pydantic import BaseModel


class RagRequest(BaseModel):
    question: str
    limit: int = 3
