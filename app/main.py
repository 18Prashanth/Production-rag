from fastapi import FastAPI
from app.api.routes import router
from app.core.logging import setup_logging
from app.retrieval.qdrant_client import ensure_collection_exists

setup_logging()

app = FastAPI(title="Production RAG System")

@app.on_event("startup")
def startup_event():
    ensure_collection_exists()

app.include_router(router)


@app.get("/health")
def health_check():
    return {"status": "ok"}