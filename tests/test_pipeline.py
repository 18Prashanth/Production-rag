from app.orchestrator.query_pipeline import QueryPipeline

pipeline = QueryPipeline()

query = "How can the agreement be terminated?"

result = pipeline.run(query)

print("ANSWER:")
print(result["answer"])