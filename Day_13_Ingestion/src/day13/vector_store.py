from qdrant_client import QdrantClient, models


def get_qdrant_client():
    return QdrantClient(url="http://localhost:6333")


def recreate_collection(client, name, size):
    if client.collection_exists(name):
        client.delete_collection(name)

    client.create_collection(
        collection_name=name,
        vectors_config=models.VectorParams(size=size, distance=models.Distance.COSINE),
    )
