from groq import Groq
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

def generate_answer(context: str, question: str) -> str:
    prompt = f"""
You are a retrieval-augmented assistant.

Rules:
- Use ONLY the context provided.
- DO NOT use external knowledge.
- DO NOT invent URLs.
- Cite sources strictly as [Doc 1], [Doc 2], etc.

Context:
{context}

Question:
{question}

Answer:
"""

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=400
    )

    return completion.choices[0].message.content.strip()
