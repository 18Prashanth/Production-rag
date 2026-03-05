from app.ingestion.embedder import openAIEmbedder
from app.retrieval.dense_qdrant import QdrantVectorStore


class IngestionService:
    def __init__(self, sparse_retriever):
        self.embedder = openAIEmbedder()
        self.vector_store = QdrantVectorStore()
        self.sparse = sparse_retriever

    def ingest_documents(self, documents: list[dict]):
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

        texts = [doc["text"] for doc in documents]
        embeddings = self.embedder.embed_batch(texts)

        chunks_with_vectors = []

        for doc, vector in zip(documents, embeddings):
            chunk = {
                "text": doc["text"],
                "vector": vector,
                "source": doc["source"],
                "page": doc["page"],
                "chunk_index": doc["chunk_index"],
            }
            chunks_with_vectors.append(chunk)

        # Upsert into Qdrant
        self.vector_store.upsert_chunks(chunks_with_vectors)

        # Register in BM25
        self.sparse.add_documents(documents)

        return chunks_with_vectors