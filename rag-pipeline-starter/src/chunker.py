"""Semantic chunking with metadata tagging."""


def chunk_document(doc: dict, chunk_size: int = 100, overlap: int = 25) -> list[dict]:
    """Split a document into overlapping chunks preserving metadata."""
    text = doc["content"].strip()
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size - overlap):
        chunk_words = words[i:i + chunk_size]
        if len(chunk_words) < 15:
            continue
        chunks.append({
            "id": f"{doc['id']}-chunk-{len(chunks)}",
            "text": " ".join(chunk_words),
            "source_doc": doc["id"],
            "source_title": doc["title"],
            "metadata": doc["metadata"],
        })
    return chunks


def chunk_all(documents: list[dict]) -> list[dict]:
    """Chunk all portfolio documents."""
    all_chunks = []
    for doc in documents:
        all_chunks.extend(chunk_document(doc))
    print(f"  📄 Chunked {len(documents)} documents → {len(all_chunks)} chunks")
    return all_chunks
