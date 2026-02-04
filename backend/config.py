import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def validate_env():
    """
    Ensure all required environment variables are present.
    """
    missing = []
    if not QDRANT_URL:
        missing.append("QDRANT_URL")
    if not QDRANT_API_KEY:
        missing.append("QDRANT_API_KEY")
    if not GROQ_API_KEY:
        missing.append("GROQ_API_KEY")

    if missing:
        raise EnvironmentError(f"Missing environment variables: {', '.join(missing)}")
