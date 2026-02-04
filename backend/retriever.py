from vectorstore import get_vectorstore

# -----------------------------
# Singleton VectorStore
# -----------------------------
_vectorstore = None


def get_vectorstore_once():
    global _vectorstore
    if _vectorstore is None:
        _vectorstore = get_vectorstore()
    return _vectorstore


# -----------------------------
# Safe Retriever (MMR + top-k)
# -----------------------------
class SafeRetriever:
    def invoke(self, query: str, k: int = 4):
        """
        Safe MMR retriever with dynamic top-k
        """

        # ---- Safety guards for k ----
        try:
            k = int(k)
        except Exception:
            k = 4

        if k < 1:
            k = 1
        if k > 10:
            k = 10

        vectorstore = get_vectorstore_once()

        retriever = vectorstore.as_retriever(
            search_type="mmr",
            search_kwargs={
                "k": k,
                "fetch_k": max(k * 2, 10),
                "lambda_mult": 0.5
            }
        )

        docs = retriever.invoke(query)
        return docs if docs else []


# Public retriever used by rag.py
retriever = SafeRetriever()
