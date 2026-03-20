# 🚀 Production RAG System

### Building a Scalable, Real-World Retrieval-Augmented Generation Pipeline

> A production-ready AI system that combines **hybrid retrieval, reranking, and LLM generation** with full-stack deployment on AWS.

---

## 🧠 Why This Project Exists

Most RAG demos stop at “it works.”
This project answers a harder question:

> **What does it take to deploy a reliable, scalable RAG system in production?**

So instead of just building a chatbot, this project focuses on:

* Accuracy (hybrid retrieval + reranking)
* Trust (citation enforcement)
* Scalability (Docker + AWS)
* Reliability (CI/CD + evaluation)

---

## ⚡ What Makes This Stand Out

✨ **Hybrid Retrieval (BM25 + Vector)**
Captures both keyword precision and semantic meaning.

🎯 **Cross-Encoder Reranking (Cohere)**
Filters noise and boosts relevance.

📚 **Citation-Enforced Generation**
Every answer is grounded in real documents.

🐳 **Production Infrastructure**
Dockerized services deployed on AWS EC2 with Nginx.

🔁 **CI/CD Pipeline (Jenkins)**
Automated testing and deployment.

📊 **Evaluation Pipeline (RAG Metrics)**
Tracks hallucination and answer quality.

---

## 🏗️ System Architecture (At a Glance)

```id="arch1"
User Query
   ↓
FastAPI API Layer
   ↓
Hybrid Retrieval (BM25 + Qdrant)
   ↓
Cohere Reranker
   ↓
OpenAI GPT (with context)
   ↓
Answer + Citations
```

---

## 🔍 How It Works

### 1. Retrieval (The Brain’s Memory)

* **BM25** → keyword matching
* **Qdrant Vector Search** → semantic understanding

These are combined into a **hybrid candidate set**.

---

### 2. Reranking (The Filter)

* Cohere cross-encoder ranks results by true relevance
* Removes irrelevant chunks

---

### 3. Generation (The Voice)

* OpenAI GPT generates answers
* Strict prompt ensures:

  * grounded responses
  * citations included

---

### 4. Evaluation (The Reality Check)

* Faithfulness
* Answer relevance

Ensures the system doesn’t drift into hallucination territory.

---

## 📁 Project Structure

```id="arch2"
app/
 ├── api/            # FastAPI routes
 ├── retrieval/      # BM25 + vector + hybrid
 ├── reranker/       # Cohere reranker
 ├── orchestrator/   # Query pipeline
 └── evaluation/     # RAG evaluation

tests/               # Unit + pipeline tests

Dockerfile
docker-compose.yml
Jenkinsfile
```

---

## 🧪 Run It Locally

```bash id="run1"
pip install -r requirements.txt
docker run -p 6333:6333 qdrant/qdrant
uvicorn app.main:app --reload
```

👉 Swagger UI: http://localhost:8000/docs

---

## 🐳 Production Deployment

* **AWS EC2**
* **Docker Compose**
* **Nginx Reverse Proxy**

```id="deploy1"
Internet → Nginx → FastAPI → RAG Pipeline
```

---

## 🔁 CI/CD Pipeline

```id="cicd1"
GitHub → Jenkins → Tests → Build → Deploy
```

Every push = automatically tested and deployed.

---

## 📌 Example API Call

**POST /ask**

```json id="ex1"
{
  "query": "How can the agreement be terminated?"
}
```

**Response**

```json id="ex2"
{
  "answer": "The agreement can be terminated by either party with 30 days notice.",
  "source": "test_doc.txt"
}
```

---

## 🧰 Tech Stack

* **Backend:** FastAPI
* **Vector DB:** Qdrant
* **LLM:** OpenAI
* **Reranker:** Cohere
* **Infra:** Docker, AWS EC2, Nginx
* **CI/CD:** Jenkins

---

## 🌟 Key Learnings

* Hybrid retrieval significantly improves recall over pure vector search
* Reranking is critical for precision in real-world datasets
* Citation enforcement is essential for trust in LLM systems
* Productionizing AI ≠ just model building → infrastructure matters

---

## 🔮 Future Work

* PDF ingestion pipeline
* Streaming responses
* Observability (Prometheus + Grafana)
* Kubernetes deployment
* Retrieval benchmarking

---

## 🤝 Let’s Connect

If you're working on RAG systems, LLM infra, or applied AI — I’d love to connect and exchange ideas!



