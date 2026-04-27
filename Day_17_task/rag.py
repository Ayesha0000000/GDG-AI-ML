from llm_client import generate_answer_from_prompt
from retrieval import dual_query_search
from guardrails import choose_action


def build_context(results):
    return "\n".join([r["text"] for r in results])


def build_prompt(q, results):
    return f"Question: {q}\nContext:\n{build_context(results)}"


def answer_with_rag(question, limit):
    data = dual_query_search(question, limit)
    results = data["results"]

    decision = choose_action(question, results)

    if decision["action"] == "clarify":
        return {
            "question": question,
            "action": "clarify",
            "answer": "Please clarify your question",
            "confidence": decision["confidence"],
            "sources": results,
        }

    if decision["action"] == "refuse":
        return {
            "question": question,
            "action": "refuse",
            "answer": "Not enough reliable info",
            "confidence": decision["confidence"],
            "sources": results,
        }

    # Answer case
    prompt = build_prompt(question, results)
    ans = generate_answer_from_prompt(prompt)

    return {
        "question": question,
        "action": "answer",
        "answer": ans,
        "confidence": decision["confidence"],
        "sources": results,
    }
