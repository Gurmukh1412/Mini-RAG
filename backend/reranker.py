from sentence_transformers import CrossEncoder

reranker_model = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)

def rerank(query: str, docs: list, top_k: int = 3):
    if not docs:
        return []

    texts = []
    for d in docs:
        if "text" in d.metadata and d.metadata["text"].strip():
            texts.append(d.metadata["text"])
        elif hasattr(d, "page_content") and d.page_content.strip():
            texts.append(d.page_content)

    # 🚨 Critical safety
    if not texts:
        return []

    try:
        pairs = [[query, t] for t in texts]
        scores = reranker_model.predict(pairs)

        ranked = sorted(
            zip(texts, scores),
            key=lambda x: x[1],
            reverse=True
        )
        return [text for text, _ in ranked[:top_k]]

    except Exception:
        # 🔒 If reranker fails, fall back to raw texts
        return texts[:top_k]
