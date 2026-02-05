from fastapi import FastAPI
from pydantic import BaseModel, Field

from vectorstore import add_texts
from rag import rag_query

import os

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run("api:app", host="0.0.0.0", port=port)

app = FastAPI(
    title="Mini RAG API",
    description="End-to-end Retrieval-Augmented Generation API",
    version="1.0.0"
)

# -----------------------------
# Request Models
# -----------------------------
class AddRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        description="Text content to add to the vector database"
    )


class AskRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=1,
        description="User question"
    )
    k: int = Field(
        default=4,
        ge=1,
        le=10,
        description="Number of top documents to retrieve"
    )


# -----------------------------
# Routes
# -----------------------------
@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "Mini RAG API is running"
    }


@app.post("/add")
def add(req: AddRequest):
    """
    Add text to the vector store
    """
    add_texts([req.text])
    return {
        "status": "added",
        "length": len(req.text)
    }


@app.post("/ask")
def ask(req: AskRequest):
    """
    Ask a question using the RAG pipeline
    """
    return rag_query(
        question=req.question,
        k=req.k
    )
