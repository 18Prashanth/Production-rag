from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
from app.core.config import settings
from app.retrieval.qdrant_client import get_qdrant_client
import uuid


class QdrantVectorStore:
    def __init__(self):
        self.client = get_qdrant_client()
        self.collection_name = settings.qdrant_collection_name

    def upsert_chunks(self, chunks: list[dict]):
        """
        chunks format:
        [
            {
                "text": "...",
                "vector": [...],
                "source": "file.pdf",
                "page": 1,
                "chunk_index": 0
            }
        ]
        """

        points = []

        for chunk in chunks:
            points.append(
                PointStruct(
                    id=str(uuid.uuid4()),
                    vector=chunk["vector"],
                    payload={
                        "text": chunk["text"],
                        "source": chunk["source"],
                        "page": chunk["page"],
                        "chunk_index": chunk["chunk_index"],
                    },
                )
            )

            self.client.upsert(collection_name=self.collection_name,points=points)
    
    def search(self, query_vector: list[float], top_k: int = 5):
        results = self.client.query_points(
        collection_name=self.collection_name,
        query=query_vector,   # NOT query_vector=
        limit=top_k
        )

        return [
            {
                "text": r.payload["text"],
                "source": r.payload["source"],
                "page": r.payload["page"],
                "chunk_index": r.payload["chunk_index"],
                "score": r.score
            }
            for r in results.points
        ]