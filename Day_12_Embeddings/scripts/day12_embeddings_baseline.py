import hashlib
import json
import os
from pathlib import Path
from qdrant_client import QdrantClient, models
from sentence_transformers import SentenceTransformer

MODEL_NAME = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
COLLECTION_NAME = "week2_day12_docs"

DATA_FILE = Path("Day_12_Embeddings/data/day12_documents.json")
CACHE_DIR = Path(".cache/embeddings")
CACHE_FILE = CACHE_DIR / "cache.json"
HF_CACHE = Path(".cache/huggingface")

QDRANT_URL = "http://localhost:6333"


def hash_text(text):
    return hashlib.sha256(text.encode()).hexdigest()


def load_cache():
    if CACHE_FILE.exists():
        return json.loads(CACHE_FILE.read_text())
    return {}


def save_cache(cache):
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    CACHE_FILE.write_text(json.dumps(cache, indent=2))


def load_docs():
    return json.loads(DATA_FILE.read_text())


def get_model():
    os.environ["HF_HOME"] = str(HF_CACHE)
    return SentenceTransformer(MODEL_NAME)


def get_vectors(model, docs):
    cache = load_cache()
    vectors = []

    for doc in docs:
        key = hash_text(doc["text"])

        if key in cache:
            vec = cache[key]
        else:
            vec = model.encode(doc["text"], normalize_embeddings=True).tolist()
            cache[key] = vec

        vectors.append(vec)

    save_cache(cache)
    return vectors


def setup_qdrant(client, size):
    if client.collection_exists(COLLECTION_NAME):
        client.delete_collection(COLLECTION_NAME)

    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=models.VectorParams(size=size, distance=models.Distance.COSINE),
    )


def insert_data(client, docs, vectors):
    points = []

    for i, (doc, vec) in enumerate(zip(docs, vectors)):
        points.append(models.PointStruct(id=i, vector=vec, payload=doc))

    client.upsert(collection_name=COLLECTION_NAME, points=points)


def search(client, model, query):
    vec = model.encode(query, normalize_embeddings=True).tolist()

    result = client.query_points(
        collection_name=COLLECTION_NAME, query=vec, limit=3, with_payload=True
    )

    print("\nQuery:", query)
    for r in result.points:
        print(r.payload)


def main():
    docs = load_docs()
    model = get_model()
    vectors = get_vectors(model, docs)

    client = QdrantClient(url=QDRANT_URL)

    setup_qdrant(client, len(vectors[0]))
    insert_data(client, docs, vectors)

    print("✅ Data inserted in Qdrant")

    search(client, model, "How to build API?")
    search(client, model, "ویکٹر سرچ کیا ہے؟")


if __name__ == "__main__":
    main()
