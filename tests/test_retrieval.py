from app.ingestion.embedder import openAIEmbedder
from app.retrieval.dense_qdrant import QdrantVectorStore
from app.retrieval.sparse_bm25 import BM25Retriever
from app.retrieval.hybrid import HybridRetriever
from app.reranker.cohere_reranker import CohereReranker

embedder = openAIEmbedder()
vector_store = QdrantVectorStore()
sparse = BM25Retriever()
reranker = CohereReranker()


query = "How can the agreement be terminated?"
query_vector = embedder.embed_text(query)

results = vector_store.search(query_vector, top_k=3)

print("RETRIEVED:", results)



# Add document to BM25 manually
doc = {
    "text": "The termination clause allows either party to end the agreement with 30 days notice.",
    "source": "test_doc.txt",
    "page": 1,
    "chunk_index": 0
}

sparse.add_documents([doc])

hybrid = HybridRetriever(vector_store, sparse)

query = "How can the agreement be terminated?"
query_vector = embedder.embed_text(query)

hybrid_results = hybrid.search(query, query_vector, top_k=3)

print("HYBRID RESULTS:", results)


reranked = reranker.rerank(query, hybrid_results, top_k=3)
print("RERANKED RESULTS:", reranked)


