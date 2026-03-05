from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    #Environment
    environment:str = Field(default="local")

    #API Keys
    openai_api_key: str
    cohere_api_key: str
    qdrant_api_key: str | None = None

    # OpenAI
    openai_embedding_model: str = "text-embedding-3-large"
    openai_embedding_dim: int = 3072
    openai_llm_model: str = "gpt-4o-mini"

     # Qdrant
    qdrant_url: str = "http://localhost:6333"
    qdrant_collection_name: str = "legal_docs"

    # Retrieval
    top_k_retrieval: int = 10
    top_k_rerank: int = 3

    model_config = {
        "env_file": ".env",
        "extra": "ignore"  # optional safety
    }



settings = Settings()

