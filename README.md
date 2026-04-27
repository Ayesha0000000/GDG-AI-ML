<div align="center">

<!-- Animated Header Banner -->
<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:302b63,100:24243e&height=200&section=header&text=GDG%20AI%2FML%20Journey&fontSize=50&fontColor=ffffff&fontAlignY=38&desc=Building%20AI-Powered%20Backend%20from%20Zero%20to%20Hero&descAlignY=60&descColor=a78bfa&animation=fadeIn" />

<br/>

<!-- Badges Row 1 -->
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)
[![Qdrant](https://img.shields.io/badge/Qdrant-Vector%20DB-DC143C?style=for-the-badge&logo=databricks&logoColor=white)](https://qdrant.tech)

<!-- Badges Row 2 -->
[![RAG](https://img.shields.io/badge/RAG-Pipeline-8B5CF6?style=for-the-badge&logo=openai&logoColor=white)]()
[![Groq](https://img.shields.io/badge/Groq-LLM%20API-F97316?style=for-the-badge&logo=lightning&logoColor=white)](https://groq.com)
[![pytest](https://img.shields.io/badge/Tested%20with-pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://pytest.org)
[![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)](LICENSE)

<br/>

> **🚀 A 17-Day hands-on AI engineering journey** — from zero to a fully functional  
> **RAG-powered Question Answering API** with vector search, guardrails & Docker deployment.

<br/>

</div>

---

## 📖 Table of Contents

- [🎯 Project Overview](#-project-overview)
- [🏗️ System Architecture](#-system-architecture)
- [🗓️ Day-by-Day Journey](#-day-by-day-journey)
- [🧰 Tech Stack](#-tech-stack)
- [⚡ Quick Start](#-quick-start)
- [📁 Project Structure](#-project-structure)
- [🏆 Final Outcomes](#-final-outcomes)
- [🤝 Contributing](#-contributing)

---

## 🎯 Project Overview

<div align="center">

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│   💡 Build a production-ready AI backend — step by step.           │
│                                                                     │
│   ✦ REST API with FastAPI      ✦ Vector Search with Qdrant         │
│   ✦ RAG Pipeline with Groq     ✦ Guardrails for safe responses     │
│   ✦ Dockerized deployment      ✦ Full test coverage                │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

</div>

This repository is a **complete, step-by-step engineering project** built during the GDG AI/ML program. Over **17 days**, a fully functional AI-powered backend was constructed from scratch — covering environment setup, API design, vector databases, embeddings, RAG (Retrieval-Augmented Generation), and intelligent guardrails.

---

## 🏗️ System Architecture

<div align="center">

```
╔══════════════════════════════════════════════════════════════════╗
║                    🌐 FINAL SYSTEM FLOW                         ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║   👤 User Question                                               ║
║         │                                                        ║
║         ▼                                                        ║
║   ┌─────────────┐                                               ║
║   │  FastAPI     │  ◄── REST Endpoint (/ask)                    ║
║   └──────┬──────┘                                               ║
║          │                                                       ║
║          ▼                                                       ║
║   ┌─────────────┐                                               ║
║   │   Qdrant     │  ◄── Vector Similarity Search                ║
║   │  Vector DB   │      (Sentence Transformers Embeddings)       ║
║   └──────┬──────┘                                               ║
║          │                                                       ║
║          ▼                                                       ║
║   ┌─────────────┐                                               ║
║   │  Context +   │  ◄── Retrieved chunks + Original query       ║
║   │    Query     │                                               ║
║   └──────┬──────┘                                               ║
║          │                                                       ║
║          ▼                                                       ║
║   ┌─────────────┐                                               ║
║   │  Groq  LLM  │  ◄── Fast inference API                       ║
║   └──────┬──────┘                                               ║
║          │                                                       ║
║          ▼                                                       ║
║   ┌─────────────┐                                               ║
║   │  Guardrails  │  ◄── Validation & Safety filters             ║
║   └──────┬──────┘                                               ║
║          │                                                       ║
║          ▼                                                       ║
║   ✅ Final Safe Answer                                           ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```

</div>

---

## 🗓️ Day-by-Day Journey

### 🔧 Phase 1 — Foundation (Days 1–3)

| Day | Topic | What Was Done | Goal |
|-----|-------|--------------|------|
| **Day 1** | 🖥️ Environment Setup | Installed Python & VS Code, created `venv`, learned terminal commands | Dev environment ready |
| **Day 2** | 🐙 Git & GitHub | Initialized repo, learned commit/push/branches, connected to GitHub | Version control live |
| **Day 3** | 🐍 Python Setup | Installed deps with `pip`, understood project structure, created base files | Python env configured |

---

### ⚙️ Phase 2 — Backend Development (Days 4–7)

| Day | Topic | What Was Done | Goal |
|-----|-------|--------------|------|
| **Day 4** | 🚀 FastAPI Intro | Created first app with `/`, `/items`, `/health` endpoints, ran with Uvicorn | Backend API live |
| **Day 5** | 🔐 Config Management | Used `.env` files, Pydantic settings, secured sensitive credentials | Config done right |
| **Day 6** | 🧪 Testing | Wrote unit tests with `pytest`, tested API endpoints | Code reliability ensured |
| **Day 7** | 🗄️ Database | Connected SQLite, created models/schemas, did CRUD operations | Data persistence ready |

---

### 🐳 Phase 3 — Containerization (Days 8–10)

| Day | Topic | What Was Done | Goal |
|-----|-------|--------------|------|
| **Day 8** | 🐳 Docker Basics | Created `Dockerfile`, built image, ran container | App containerized |
| **Day 9** | 🧩 Docker Compose | Used `docker-compose.yml`, connected services, simplified deployment | Multi-service setup |
| **Day 10** | 🏛️ Advanced Backend | Improved API structure, modular code, better routing | Clean architecture |

---

### 🤖 Phase 4 — AI & Vector Search (Days 11–13)

| Day | Topic | What Was Done | Goal |
|-----|-------|--------------|------|
| **Day 11** | 🔍 Qdrant Vector DB | Introduced vector database, stored embeddings, learned similarity search | Semantic search enabled |
| **Day 12** | 🧠 Embeddings | Used `sentence-transformers`, converted text → vectors, stored in Qdrant | AI understanding enabled |
| **Day 13** | 📥 Data Ingestion | Loaded documents, chunked text, stored chunks in vector DB | RAG data prep done |

---

### 🦾 Phase 5 — RAG & Guardrails (Days 15–17)

| Day | Topic | What Was Done | Goal |
|-----|-------|--------------|------|
| **Day 15** | 🔗 RAG Pipeline | Built full RAG pipeline, retrieved context, sent to Groq LLM, generated answers | AI Q&A system live |
| **Day 16** | 🎯 Advanced Retrieval | Improved search logic, added normalization & better ranking | More accurate responses |
| **Day 17** | 🛡️ Guardrails | Added validation layer, controlled AI responses, filtered unsafe queries | Safe & reliable AI |

---

## 🧰 Tech Stack

<div align="center">

| Category | Technology | Purpose |
|----------|-----------|---------|
| 🐍 **Language** | Python 3.11+ | Core development language |
| ⚡ **API Framework** | FastAPI + Uvicorn | High-performance REST API |
| 🗄️ **Database** | SQLite | Relational data storage |
| 🔍 **Vector DB** | Qdrant | Semantic/similarity search |
| 🧠 **Embeddings** | Sentence-Transformers | Text → vector conversion |
| 🤖 **LLM** | Groq API | Fast language model inference |
| 🐳 **Containers** | Docker + Docker Compose | App containerization & deployment |
| 🧪 **Testing** | pytest | Unit & integration testing |
| 🔐 **Config** | Pydantic + python-dotenv | Settings & secrets management |

</div>

---

## ⚡ Quick Start

### Prerequisites

```bash
# Required
Python 3.11+
Docker & Docker Compose
Git
```

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Ayesha0000000/GDG-AI-ML.git
cd GDG-AI-ML
```

### 2️⃣ Setup Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3️⃣ Configure Environment Variables

```bash
# Copy the example env file
cp .env.example .env

# Edit and add your keys
GROQ_API_KEY=your_groq_api_key_here
QDRANT_HOST=localhost
QDRANT_PORT=6333
```

### 4️⃣ Run with Docker (Recommended)

```bash
# Start all services (API + Qdrant)
docker-compose up --build
```

### 5️⃣ Run Locally (Without Docker)

```bash
# Start Qdrant separately, then:
uvicorn app.main:app --reload --port 8000
```

### 6️⃣ Test the API

```bash
# Health check
curl http://localhost:8000/health

# Ask a question (RAG)
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What is machine learning?"}'
```

### 7️⃣ Run Tests

```bash
pytest tests/ -v
```

> **API Docs available at:** `http://localhost:8000/docs` (Swagger UI auto-generated by FastAPI)

---

## 📁 Project Structure

```
GDG-AI-ML/
│
├── 📁 app/
│   ├── main.py              # FastAPI app entry point
│   ├── config.py            # Pydantic settings & env vars
│   ├── 📁 routers/
│   │   ├── items.py         # /items endpoints
│   │   └── ask.py           # /ask RAG endpoint
│   ├── 📁 models/
│   │   └── schemas.py       # Pydantic models & DB schemas
│   ├── 📁 services/
│   │   ├── embeddings.py    # Sentence-transformer logic
│   │   ├── qdrant.py        # Vector DB operations
│   │   ├── rag.py           # RAG pipeline
│   │   └── guardrails.py    # Response validation & filtering
│   └── 📁 database/
│       └── sqlite.py        # SQLite CRUD operations
│
├── 📁 data/
│   └── documents/           # Source documents for RAG
│
├── 📁 tests/
│   ├── test_api.py          # API endpoint tests
│   └── test_rag.py          # RAG pipeline tests
│
├── 📁 days/                 # Day-wise learning notes & code
│   ├── day01/
│   ├── day02/
│   ├── ...
│   └── day17/
│
├── Dockerfile               # Docker image definition
├── docker-compose.yml       # Multi-service orchestration
├── requirements.txt         # Python dependencies
├── .env.example             # Environment variables template
└── README.md                # You are here!
```

---

## 🏆 Final Outcomes

<div align="center">

```
╔══════════════════════════════════════════════════════╗
║           🎉 BY DAY 17, WE SUCCESSFULLY BUILT:      ║
╠══════════════════════════════════════════════════════╣
║                                                      ║
║   ✅  Full Backend REST API (FastAPI)                ║
║   ✅  AI-Powered Semantic Search (Qdrant)            ║
║   ✅  RAG-Based Question Answering (Groq LLM)        ║
║   ✅  Guardrails for Safe & Valid Responses          ║
║   ✅  Fully Dockerized Application                   ║
║   ✅  Complete Test Suite (pytest)                   ║
║   ✅  GitHub Version-Controlled Project              ║
║                                                      ║
╚══════════════════════════════════════════════════════╝
```

</div>

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. **Fork** this repository
2. Create your feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/my-feature`
5. Open a **Pull Request**

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Built with ❤️ during the GDG AI/ML Program**

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:24243e,50:302b63,100:0f0c29&height=120&section=footer&animation=fadeIn" />

</div>
