from sentence_transformers import SentenceTransformer

# Load MiniLM model locally
_model = SentenceTransformer("all-MiniLM-L6-v2")

def embed(texts: list[str]) -> list[list[float]]:
    """
    Generate embeddings for a list of texts using MiniLM.
    Output dimension: 384
    """

    if not texts or not isinstance(texts, list):
        raise ValueError("Input must be a non-empty list of strings")

    embeddings = _model.encode(texts, show_progress_bar=False)

    return embeddings.tolist()
