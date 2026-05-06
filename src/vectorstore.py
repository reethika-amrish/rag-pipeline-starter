"""In-memory vector store with cosine similarity search."""

import math


def cosine_similarity(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    mag_a = math.sqrt(sum(x * x for x in a)) or 1e-10
    mag_b = math.sqrt(sum(x * x for x in b)) or 1e-10
    return dot / (mag_a * mag_b)


class VectorStore:
    """Simple in-memory vector store."""

    def __init__(self):
        self.entries = []  # list of {chunk, vector}

    def add(self, chunks: list[dict], vectors: list[list[float]]):
        for chunk, vec in zip(chunks, vectors):
            self.entries.append({"chunk": chunk, "vector": vec})
        print(f"  🗄️  Stored {len(chunks)} vectors in memory")

    def search(self, query_vector: list[float], top_k: int = 3) -> list[dict]:
        """Find top-K most similar chunks."""
        scored = []
        for entry in self.entries:
            score = cosine_similarity(query_vector, entry["vector"])
            scored.append({"chunk": entry["chunk"], "score": round(score, 4)})

        scored.sort(key=lambda x: x["score"], reverse=True)
        return scored[:top_k]
