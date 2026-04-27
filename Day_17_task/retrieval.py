from sentence_transformers import SentenceTransformer
from functools import lru_cache
from normalization import normalize_roman_urdu
from settings import settings


@lru_cache(maxsize=1)
def get_model():
    return SentenceTransformer(settings.embedding_model_name)


# 🔴 TEMP MOCK (abhi Qdrant nahi use kar rahe)
def search_chunks(query, limit):
    return [
        {
            "score": 0.9,
            "doc_id": "1",
            "chunk_id": "c1",
            "title": "Test",
            "language": "en",
            "source": "test",
            "chunk_index": 0,
            "text": f"Result for query: {query}",
        }
    ]


def merge_results(results_list, limit):
    merged = []
    for results in results_list:
        merged.extend(results)

    # sort by score
    merged.sort(key=lambda x: x["score"], reverse=True)

    return merged[:limit]


def dual_query_search(query, limit):
    original = query
    normalized = normalize_roman_urdu(query)

    res1 = search_chunks(original, limit)
    res2 = search_chunks(normalized, limit)

    merged = merge_results([res1, res2], settings.merged_search_limit)

    return {
        "original_query": original,
        "normalized_query": normalized,
        "results": merged,
    }
