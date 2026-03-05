import cohere
from app.core.config import settings


class CohereReranker:
    def __init__(self):
        self.client = cohere.Client(settings.cohere_api_key)
        self.model = "rerank-english-v3.0"

    def rerank(self, query: str, documents: list[dict], top_k: int = 3):
        """
        documents: list of dicts with "text" field
        """

        if not documents:
            return []

        texts = [doc["text"] for doc in documents]

        response = self.client.rerank(
            model=self.model,
            query=query,
            documents=texts,
            top_n=top_k
        )

        reranked_results = []

        for r in response.results:
            original_doc = documents[r.index]
            reranked_results.append({
                **original_doc,
                "rerank_score": r.relevance_score
            })

        return reranked_results