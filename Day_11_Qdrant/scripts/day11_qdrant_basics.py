from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct,
    Filter,
    FieldCondition,
    MatchValue,
)

COLLECTION = "week2_day11_vectors"
QDRANT_URL = "http://qdrant:6333"


def main():
    client = QdrantClient(url=QDRANT_URL)

    # recreate collection
    if client.collection_exists(COLLECTION):
        client.delete_collection(COLLECTION)

    client.create_collection(
        collection_name=COLLECTION,
        vectors_config=VectorParams(size=4, distance=Distance.COSINE),
    )

    # insert data
    points = [
        PointStruct(
            id=1, vector=[0.10, 0.20, 0.30, 0.40], payload={"category": "notes"}
        ),
        PointStruct(
            id=2, vector=[0.11, 0.19, 0.29, 0.39], payload={"category": "notes"}
        ),
        PointStruct(
            id=3, vector=[0.90, 0.10, 0.05, 0.02], payload={"category": "todo"}
        ),
        PointStruct(
            id=4, vector=[0.88, 0.12, 0.04, 0.01], payload={"category": "todo"}
        ),
    ]

    client.upsert(collection_name=COLLECTION, points=points)

    # search without filter
    res = client.search(
        collection_name=COLLECTION, query_vector=[0.10, 0.20, 0.30, 0.40], limit=3
    )
    print("Top results:", res)

    # search with filter
    flt = Filter(must=[FieldCondition(key="category", match=MatchValue(value="todo"))])

    res2 = client.search(
        collection_name=COLLECTION,
        query_vector=[0.10, 0.20, 0.30, 0.40],
        query_filter=flt,
    )

    print("Filtered results:", res2)


if __name__ == "__main__":
    main()
