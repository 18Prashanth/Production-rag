class HybridRetriever:
    def __init__(self, dense_retriever, sparse_retriever):
        self.dense = dense_retriever
        self.sparse = sparse_retriever

    def search(self, query: str, query_vector: list[float], top_k: int = 5):
        dense_results = self.dense.search(query_vector, top_k=top_k)
        sparse_results = self.sparse.search(query, top_k=top_k)

        combined = dense_results + sparse_results

        # Deduplicate by (source, chunk_index)
        seen = set()
        unique_results = []

        for r in combined:
            key = (r["source"], r["chunk_index"])
            if key not in seen:
                seen.add(key)
                unique_results.append(r)

        return unique_results