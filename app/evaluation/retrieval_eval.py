import json
from app.orchestrator.query_pipeline import QueryPipeline


def evaluate_retrieval():
    pipeline = QueryPipeline()

    with open("app/evaluation/benchmark_dataset.json") as f:
        dataset = json.load(f)

    correct = 0
    total = len(dataset)

    for sample in dataset:
        query = sample["question"]
        expected_source = sample["expected_source"]

        query_vector = pipeline.embedder.embed_text(query)
        hybrid_results = pipeline.hybrid.search(query, query_vector)

        sources = [r["source"] for r in hybrid_results[:5]]

        if expected_source in sources:
            correct += 1

    recall_at_5 = correct / total

    return recall_at_5


from app.evaluation.retrieval_eval import evaluate_retrieval


def test_recall_at_5():
    score = evaluate_retrieval()
    assert score >= 0.8