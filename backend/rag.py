from retriever import retriever
from reranker import rerank
from llm import generate_answer


def rag_query(question: str, k: int = 4):
    """
    End-to-end RAG pipeline:
    Query → Retrieve → Rerank → Generate → Sources with citations
    """

    if not question or not question.strip():
        return {
            "answer": "Question cannot be empty.",
            "sources": []
        }

    # -----------------------------
    # 1. Retrieve (Top-k)
    # -----------------------------
    try:
        # retriever only takes query
        docs = retriever.invoke(question)

        # manually enforce top-k safety
        docs = docs[:k]
    except Exception as e:
        return {
            "answer": f"Retriever error: {str(e)}",
            "sources": []
        }

    if not docs:
        return {
            "answer": "No relevant documents found.",
            "sources": []
        }

    # -----------------------------
    # 2. Rerank
    # -----------------------------
    try:
        top_texts = rerank(question, docs)
    except Exception as e:
        return {
            "answer": f"Reranker error: {str(e)}",
            "sources": []
        }

    if not top_texts:
        return {
            "answer": "Relevant documents were found, but no usable text was available.",
            "sources": []
        }

    # -----------------------------
    # 3. Generate Answer
    # -----------------------------
    try:
        answer = generate_answer(question, top_texts)
    except Exception as e:
        return {
            "answer": f"LLM error: {str(e)}",
            "sources": []
        }

    # -----------------------------
    # 4. Build citations
    # -----------------------------
    sources = []
    for i, d in enumerate(docs):
        src = d.metadata.get("source") if d.metadata else None
        sources.append({
            "id": i + 1,
            "source": src or f"doc_{i+1}"
        })

    # Append inline citation markers
    citation_marks = " ".join([f"[{s['id']}]" for s in sources])
    answer_with_citations = f"{answer}\n\n{citation_marks}"

    return {
        "answer": answer_with_citations,
        "sources": sources
    }
