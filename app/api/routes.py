from fastapi import APIRouter
from app.api.schemas import AskRequest, AskResponse
from app.orchestrator.query_pipeline import QueryPipeline

router = APIRouter()
pipeline = QueryPipeline()


@router.post("/ask", response_model=AskResponse)
def ask_question(request: AskRequest):
    result = pipeline.run(request.query)
    return AskResponse(answer=result["answer"])