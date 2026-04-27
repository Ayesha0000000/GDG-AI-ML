from sentence_transformers import SentenceTransformer
from day13.vector_store import get_qdrant_client


def main():
    model = SentenceTransformer(
        "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    )
    client = get_qdrant_client()

    query = "What is FastAPI?"
    vector = model.encode(query).tolist()

    results = client.search(
        collection_name="day13_collection", query_vector=vector, limit=2
    )

    for r in results:
        print(r.payload)


if __name__ == "__main__":
    main()
