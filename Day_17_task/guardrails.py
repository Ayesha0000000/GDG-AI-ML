from statistics import mean


# 🧠 Check if question vague hai
def is_query_vague(query: str) -> bool:
    query = query.strip().lower()

    vague_words = ["help", "explain", "tell me", "info"]

    # agar 1 word hai ya vague words me hai
    if len(query.split()) <= 1:
        return True

    if query in vague_words:
        return True

    return False


# 📊 Confidence calculate karo
def compute_confidence(results):
    if not results:
        return {"top_score": 0, "avg_score": 0, "count": 0}

    scores = [r.get("score", 0) for r in results]

    return {"top_score": max(scores), "avg_score": mean(scores), "count": len(results)}


# 🎯 Final decision (main function)
def choose_action(question, results):
    confidence = compute_confidence(results)

    # ❓ vague question
    if is_query_vague(question):
        return {
            "action": "clarify",
            "reason": "Question is vague",
            "confidence": confidence,
        }

    # ❌ no results
    if confidence["count"] == 0:
        return {"action": "refuse", "reason": "No data found", "confidence": confidence}

    # ❌ weak top score
    if confidence["top_score"] < 0.5:
        return {"action": "refuse", "reason": "Low top score", "confidence": confidence}

    # ❌ weak average score
    if confidence["avg_score"] < 0.4:
        return {
            "action": "refuse",
            "reason": "Low average score",
            "confidence": confidence,
        }

    # ✅ good case
    return {"action": "answer", "reason": "Enough confidence", "confidence": confidence}
