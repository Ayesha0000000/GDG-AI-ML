from llm_client import generate_answer_from_prompt
from retrieval import search_chunks


def build_context_block(results):
    parts = []
    for i, item in enumerate(results, 1):
        parts.append(f"[{i}] {item['text']}")
    return "\n".join(parts)


def build_prompt(question, results):
    context = build_context_block(results)

    return f"""
Question: {question}

Context:
{context}

Answer only using context.
"""


def answer_with_rag(question, limit):
    results = search_chunks(question, limit)
    prompt = build_prompt(question, results)
    answer = generate_answer_from_prompt(prompt)

    return {"question": question, "answer": answer, "sources": results}
