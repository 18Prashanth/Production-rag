from qdrant_client import QdrantClient
from app.core.config import settings
from qdrant_client.models import VectorParams, Distance
import logging

logger = logging.getLogger(__name__)

def get_qdrant_client():
    return QdrantClient(
        url=settings.qdrant_url,
        api_key=settings.qdrant_api_key
    )

def ensure_collection_exists():
    client = get_qdrant_client()
    
    collections = client.get_collections().collections
    collections = client.get_collections().collections
    collection_names = [c.name for c in collections]

    if settings.qdrant_collection_name not in collection_names:
        logger.info("Creating Qdrant collection...")

        client.create_collection(
            collection_name=settings.qdrant_collection_name,
            vectors_config=VectorParams(
                size=settings.openai_embedding_dim,
                distance=Distance.COSINE,
            ),
        )

        logger.info("Collection created successfully.")
    else:
        logger.info("Qdrant collection already exists.")
