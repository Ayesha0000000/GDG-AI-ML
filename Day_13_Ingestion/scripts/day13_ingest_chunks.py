import json
from pathlib import Path
from sentence_transformers import SentenceTransformer
from day13.ingestion import build_chunk_records
from day13.vector_store import get_qdrant_client, recreate_collection
from qdrant_client import models

DATA_FILE = Path("data/raw/day13_documents.json")


def main():
    docs = json.loads(DATA_FILE.read_text())
    chunks = build_chunk_records(docs)

    model = SentenceTransformer(
        "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    )
    vectors = model.encode([c["text"] for c in chunks]).tolist()

    client = get_qdrant_client()
    recreate_collection(client, "day13_collection", len(vectors[0]))

    points = []
    for i, (c, v) in enumerate(zip(chunks, vectors)):
        points.append(models.PointStruct(id=i, vector=v, payload=c))

    client.upsert(collection_name="day13_collection", points=points)

    print("✅ Ingestion Done")


if __name__ == "__main__":
    main()
