"""Mock vector embeddings using TF-IDF-like word frequency vectors. No API keys needed."""

import math
from collections import Counter


class MockEmbedder:
    """Simple word-frequency embedder that produces comparable vectors."""

    def __init__(self):
        self.vocab = {}
        self.idf = {}

    def fit(self, texts: list[str]):
        """Build vocabulary from all texts."""
        doc_count = len(texts)
        word_doc_freq = Counter()
        for text in texts:
            unique_words = set(text.lower().split())
            for w in unique_words:
                word_doc_freq[w] += 1

        self.vocab = {w: i for i, w in enumerate(word_doc_freq.keys())}
        self.idf = {w: math.log(doc_count / (freq + 1)) + 1 for w, freq in word_doc_freq.items()}
        print(f"  📐 Built vocabulary: {len(self.vocab)} terms")

    def embed(self, text: str) -> list[float]:
        """Convert text to a TF-IDF-like vector."""
        words = text.lower().split()
        word_counts = Counter(words)
        total = len(words) if words else 1

        vector = [0.0] * len(self.vocab)
        for word, count in word_counts.items():
            if word in self.vocab:
                tf = count / total
                vector[self.vocab[word]] = tf * self.idf.get(word, 1.0)
        return vector

    def embed_batch(self, texts: list[str]) -> list[list[float]]:
        return [self.embed(t) for t in texts]
