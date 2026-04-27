def chunk_text(text, chunk_size=80, overlap=20):
    words = text.split()
    chunks = []
    step = chunk_size - overlap

    for i in range(0, len(words), step):
        chunk = words[i : i + chunk_size]
        if chunk:
            chunks.append(" ".join(chunk))

    return chunks


def build_chunk_records(docs):
    records = []

    for doc in docs:
        chunks = chunk_text(doc["text"])

        for i, chunk in enumerate(chunks, 1):
            records.append(
                {
                    "chunk_id": f"{doc['doc_id']}-{i}",
                    "doc_id": doc["doc_id"],
                    "text": chunk,
                    "title": doc["title"],
                }
            )

    return records
