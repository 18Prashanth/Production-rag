from app.orchestrator.query_pipeline import QueryPipeline
from app.evaluation.citation_validator import validate_citations


def test_citation_present():
    pipeline = QueryPipeline()

    doc = {
        "text": "The termination clause allows either party to end the agreement with 30 days notice.",
        "source": "test_doc.txt",
        "page": 1,
        "chunk_index": 0
    }

    pipeline.ingestion.ingest_documents([doc])

    result = pipeline.run("How can the agreement be terminated?")

    assert validate_citations(result["answer"])