# Mini-RAG: Retrieval Augmented Generation Project

This is a mini project based on **Retrieval-Augmented Generation (RAG)** where a language model is combined with a vector database to answer user queries using relevant external context.

The main goal of this project was to understand how **LLMs + vector search** work together in real applications, instead of using a plain chatbot.

---

## 📌 About this project

I built this project as part of an **online assessment for an interview**.  
At the time of starting, I was **new to RAG systems and vector databases**, but I tried my best to understand the concepts and implement them properly within the given time.

This project represents my **learning approach, problem-solving mindset, and willingness to explore new technologies**, even with limited prior experience.


---

## 📌 Why I built this project

While studying about Large Language Models, I realized that:
- LLMs can hallucinate
- They don’t know private or custom data
- Fine-tuning is expensive and slow

So I built this project to learn how **RAG solves these problems** by retrieving relevant information first and then generating answers.

This project helped me understand **system-level thinking** in AI applications.

---

## 🧠 How the system works (High Level)

User Question
↓
Convert question to embedding
↓
Search similar vectors in database
↓
Fetch top relevant context
↓
(Optional) Re-rank context
↓
Send context + question to LLM
↓
Final Answer

---

## ✨ Features

- End-to-end RAG pipeline
- Vector similarity search using embeddings
- Clean separation between retrieval and generation
- API-based backend using FastAPI
- Secure handling of API keys using environment variables
- Easy to extend or modify for other datasets

---

## ⚙️ Tech Stack Used
### Backend
- Python
- FastAPI
- GROQ API
- Pinecone (Vector Database)

### Frontend
- Simple Python-based interface
- Communicates with backend using REST APIs

---

## 📁 Project Structure

Mini-RAG/
├── backend/
│ ├── api.py                                 # API endpoints
│ ├── rag.py                                 # Main RAG pipeline
│ ├── retriever.py                           # Vector retrieval logic
│ ├── reranker.py                            # Re-ranking logic
│ ├── embeddings.py                          # Embedding generation
│ ├── vectorstore.py                         # Vector DB handling
│ ├── llm.py                                 # LLM interaction
│ ├── config.py                              # Configurations
│ └── requirements.txt
│
├── frontend/
│ ├── app.py                                 # Frontend interface
│ └── requirements.txt
│
├── README.md
└── LICENSE


---

## 🛠️ How to run locally

### 1. Clone the repository
```bash
git clone https://github.com/Gurmukh1412/Mini-RAG.git
cd Mini-RAG

2. Setup backend
cd backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt

3.Create a .env file:

OPENAI_API_KEY=your_api_key
PINECONE_API_KEY=your_api_key
PINECONE_ENV=gcp-starter
PINECONE_INDEX=text-rag-index


4.Run the server:

uvicorn api:app --reload

5.🌐 API Access

After running the backend, API documentation is available at:

http://127.0.0.1:8000/docs

🎯 What I learned from this project
        How vector databases work
        How embeddings are used for semantic search
        How RAG reduces hallucinations in LLMs
        How to design modular AI systems
        How to structure an ML project properly

🚀 Future Improvements
        Add document upload support
        Improve retrieval accuracy
        Add UI instead of CLI
        Support multiple datasets

📄 License
This project is licensed under the MIT License.

👤 Author
Gurmukh Singh
Undergraduate Student, IIT Mandi
