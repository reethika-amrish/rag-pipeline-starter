"""End-to-end RAG pipeline over Reethika's portfolio."""

from .ingest import PORTFOLIO_DOCUMENTS
from .chunker import chunk_all
from .embedder import MockEmbedder
from .vectorstore import VectorStore
from .generator import generate_response


def build_pipeline():
    """Ingest, chunk, embed, and store — returns a query function."""
    print("\n🔧 Building RAG Pipeline over Portfolio\n")

    # 1. Chunk documents
    chunks = chunk_all(PORTFOLIO_DOCUMENTS)

    # 2. Build embedder and embed all chunks
    embedder = MockEmbedder()
    embedder.fit([c["text"] for c in chunks])
    vectors = embedder.embed_batch([c["text"] for c in chunks])

    # 3. Store in vector store
    store = VectorStore()
    store.add(chunks, vectors)

    print(f"\n✅ Pipeline ready — {len(chunks)} chunks indexed\n")

    def query(question: str, top_k: int = 3) -> dict:
        """Query the portfolio RAG pipeline."""
        query_vec = embedder.embed(question)
        retrieved = store.search(query_vec, top_k=top_k)
        return generate_response(question, retrieved)

    return query


SAMPLE_QUESTIONS = [
    "What experience does Reethika have with LangGraph?",
    "Tell me about the migration project",
    "What frontend frameworks has she worked with?",
    "Describe the RAG pipeline project",
    "What AWS services has she used?",
    "What is her experience with HITL workflows?",
    "Tell me about the Angular clinical research project",
]


if __name__ == "__main__":
    query_fn = build_pipeline()

    print("=" * 60)
    print("  📚 Portfolio RAG — Ask questions about my experience")
    print("=" * 60)

    # Run sample questions
    for q in SAMPLE_QUESTIONS:
        print(f"\n💬 Q: {q}")
        result = query_fn(q)
        print(f"📎 Sources: {', '.join(s['document'] for s in result['sources'])}")
        print(f"📊 Relevance: {[s['relevance'] for s in result['sources']]}")
        print(f"💡 A: {result['answer'][:200]}...")
        print("-" * 60)

    # Interactive mode
    print("\n\nType your own questions (or 'quit' to exit):\n")
    while True:
        q = input("Q: ").strip()
        if q.lower() in ("quit", "exit", "q"):
            break
        result = query_fn(q)
        print(f"\n📎 Sources: {', '.join(s['document'] for s in result['sources'])}")
        print(f"💡 A: {result['answer'][:300]}...\n")
