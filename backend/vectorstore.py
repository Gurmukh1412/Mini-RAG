import time
import langchain
langchain.debug = False

from qdrant_client import QdrantClient
from qdrant_client.http.exceptions import ResponseHandlingException, UnexpectedResponse
from qdrant_client.models import VectorParams, Distance

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore
from langchain_core.documents import Document

from config import QDRANT_URL, QDRANT_API_KEY

# -----------------------------
# Config
# -----------------------------
COLLECTION_NAME = "text_rag"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
VECTOR_SIZE = 384  # MiniLM dimension

# -----------------------------
# Embeddings
# -----------------------------
embeddings = HuggingFaceEmbeddings(
    model_name=EMBEDDING_MODEL
)

# -----------------------------
# Qdrant Client (safe)
# -----------------------------
def create_qdrant_client():
    try:
        return QdrantClient(
            url=QDRANT_URL,
            api_key=QDRANT_API_KEY,
            timeout=30
        )
    except ResponseHandlingException:
        time.sleep(2)
        return QdrantClient(
            url=QDRANT_URL,
            api_key=QDRANT_API_KEY,
            timeout=30
        )

client = create_qdrant_client()

# -----------------------------
# Ensure collection exists
# -----------------------------
def ensure_collection():
    try:
        client.get_collection(COLLECTION_NAME)
    except Exception:
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=VECTOR_SIZE,
                distance=Distance.COSINE
            )
        )

# -----------------------------
# Lazy VectorStore
# -----------------------------
_vectorstore = None

def get_vectorstore():
    global _vectorstore
    if _vectorstore is None:
        ensure_collection()  # 🔑 CRITICAL LINE
        _vectorstore = QdrantVectorStore(
            client=client,
            collection_name=COLLECTION_NAME,
            embedding=embeddings
        )
    return _vectorstore

# -----------------------------
# Add texts
# -----------------------------
def add_texts(texts: list[str]):
    documents = []

    for t in texts:
        t = t.strip()
        if not t:
            continue

        documents.append(
            Document(
                page_content=t,
                metadata={"text": t}
            )
        )

    if not documents:
        return

    vs = get_vectorstore()
    vs.add_documents(documents)
