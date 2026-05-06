"""RAG response generator — grounds answers in retrieved chunks."""


def generate_response(query: str, retrieved: list[dict]) -> dict:
    """Generate a grounded response using retrieved context.
    In production: this calls an LLM with the context in the prompt.
    Here: we construct a response from the retrieved chunks directly."""

    if not retrieved:
        return {"answer": "I don't have information about that in my portfolio.", "sources": []}

    # Build context from top chunks
    context_parts = []
    sources = []
    for r in retrieved:
        chunk = r["chunk"]
        context_parts.append(chunk["text"])
        sources.append({
            "document": chunk["source_title"],
            "relevance": r["score"],
            "metadata": chunk["metadata"]
        })

    context = " ".join(context_parts)

    # Mock LLM response — in production this would be:
    # prompt = f"Based on the following context, answer the question.\nContext: {context}\nQuestion: {query}"
    # response = llm.invoke(prompt)
    answer = f"Based on my portfolio: {context[:500]}..."

    return {
        "answer": answer,
        "sources": sources,
        "chunks_used": len(retrieved),
        "grounded": True
    }
