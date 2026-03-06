from app.ingestion.embedder import openAIEmbedder
from app.retrieval.dense_qdrant import QdrantVectorStore
from app.retrieval.sparse_bm25 import BM25Retriever
from app.retrieval.hybrid import HybridRetriever
from app.reranker.cohere_reranker import CohereReranker
from app.llm.openai_provider import OpenAIProvider
from app.ingestion.ingestion_service import IngestionService


class QueryPipeline:
    def __init__(self):
        self.embedder = openAIEmbedder()
        self.dense = QdrantVectorStore()
        self.sparse = BM25Retriever()
        self.hybrid = HybridRetriever(self.dense, self.sparse)
        self.reranker = CohereReranker()
        self.llm = OpenAIProvider()
        self.ingestion = IngestionService(self.sparse)

    def run(self, query: str):
        query_vector = self.embedder.embed_text(query)

        hybrid_results = self.hybrid.search(query, query_vector)

        reranked = self.reranker.rerank(query, hybrid_results)

        top_context = reranked[:3]

        # answer = self.llm.generate(query, top_context)
        answer = self.llm.generate(query, reranked)

        return {
            "answer": answer,
            "contexts": top_context
        }