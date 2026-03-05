from rank_bm25 import BM25Okapi
import re


class BM25Retriever:
    def __init__(self):
        self.documents = []
        self.tokenized_corpus = []
        self.bm25 = None

    def _tokenize(self, text: str):
        text = text.lower()
        text = re.sub(r"[^\w\s]", "", text)
        return text.split()

    def add_documents(self, documents: list[dict]):
        """
        documents format:
        [
            {
                "text": "...",
                "source": "...",
                "page": 1,
                "chunk_index": 0
            }
        ]
        """
        self.documents.extend(documents)
        self.tokenized_corpus = [self._tokenize(doc["text"]) for doc in self.documents]
        self.bm25 = BM25Okapi(self.tokenized_corpus)

    def search(self, query: str, top_k: int = 5):
        if self.bm25 is None:
            return []
        tokenized_query = self._tokenize(query)
        scores = self.bm25.get_scores(tokenized_query)

        ranked_indices = sorted(
            range(len(scores)),
            key=lambda i: scores[i],
            reverse=True
        )[:top_k]

        results = []
        for i in ranked_indices:
            doc = self.documents[i]
            results.append({
                "text": doc["text"],
                "source": doc["source"],
                "page": doc["page"],
                "chunk_index": doc["chunk_index"],
                "score": scores[i],
                "method": "bm25"
            })

        return results