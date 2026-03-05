# from app.ingestion.embedder import openAIEmbedder
# from app.retrieval.dense_qdrant import QdrantVectorStore

# embedder = openAIEmbedder()
# vector_store = QdrantVectorStore()

# text = "The termination clause allows either party to end the agreement with 30 days notice."

# vector = embedder.embed_text(text)

# vector_store.upsert_chunks([
#     {
#         "text": text,
#         "vector": vector,
#         "source": "test_doc.txt",
#         "page": 1,
#         "chunk_index": 0
#     }
# ])

# print("Test chunk inserted successfully.")

# # print("VECTOR TYPE:", type(vector))
# # print("VECTOR SAMPLE:", vector[:5] if vector else vector)

from app.orchestrator.query_pipeline import QueryPipeline

pipeline = QueryPipeline()

doc = {
    "text": "The termination clause allows either party to end the agreement with 30 days notice.",
    "source": "test_doc.txt",
    "page": 1,
    "chunk_index": 0
}

pipeline.ingestion.ingest_documents([doc])

query = "How can the agreement be terminated?"
result = pipeline.run(query)

print("ANSWER:")
print(result["answer"])