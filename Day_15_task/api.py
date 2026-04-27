from fastapi import FastAPI
from rag import answer_with_rag
from schema import RagRequest

app = FastAPI()


@app.post("/rag")
def rag(payload: RagRequest):
    return answer_with_rag(payload.question, payload.limit)
