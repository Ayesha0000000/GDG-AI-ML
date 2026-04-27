from llm_client import generate_answer_from_prompt
from retrieval import dual_query_search


def build_context(results):
    parts = []
    for i, item in enumerate(results, 1):
        parts.append(f"[{i}] {item['text']}")
    return "\n".join(parts)


def build_prompt(question, results):
    context = build_context(results)

    return f"""
Question: {question}

Context:
{context}

Answer using only context.
"""


def answer_with_rag(question, limit):
    data = dual_query_search(question, limit)

    results = data["results"]
    prompt = build_prompt(question, results)

    answer = generate_answer_from_prompt(prompt)

    return {
        "question": question,
        "normalized_query": data["normalized_query"],
        "answer": answer,
        "sources": results,
    }
