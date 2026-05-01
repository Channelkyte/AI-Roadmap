# 🤖 AI Engineering Roadmap Training

<p align="center">
  <img src="image1.JPG" width="600"/><br><br>
  <img src="image2.JPG" width="600"/><br>
  <em>AI Engineering Roadmap Overview</em>
</p>

---

## 📌 About This Repository

This repository documents my structured journey toward becoming a **Junior AI Engineer**.

It combines:

- 📚 Self-study
- 🛠️ Hands-on projects
- 🎓 Structured coursework (Harvard CS50P)

The goal is to build strong, real-world foundations in:

> **Python • Machine Learning • NLP • Transformers • LLMs • RAG • AI Agents**

---

## 🎯 Objectives

- Build strong Python foundations for AI & backend systems
- Develop and deploy machine learning models
- Understand NLP and how Transformers work architecturally
- Work with modern LLM systems and prompt engineering
- Build RAG pipelines and AI agents using LangChain
- Design and serve AI backends using **FastAPI**

> **Note:** Based on mentor guidance — Flask, standalone Data Analysis, and DSA have been removed from this roadmap. Data analysis skills (NumPy, Pandas) will be picked up naturally during Machine Learning. FastAPI replaces Flask as the backend framework for AI services.

---

## 🧭 Learning Roadmap

### 📘 Core AI Engineering Path

```
Python Foundations
      ↓
FastAPI Basics
      ↓
Machine Learning (scikit-learn + PyTorch + Hugging Face)
      ↓
NLP Fundamentals
      ↓
Transformers (how they actually work)
      ↓
LLMs + Prompt Engineering
      ↓
RAG + LangChain + Agents
      ↓
Deploy + Portfolio
```

### 🎓 CS50P Integration (Foundation Layer)

Harvard CS50P strengthens core Python skills that directly support AI development:

- Python programming fundamentals
- OOP and functions
- File handling and APIs
- Problem-solving and debugging mindset

---

## 🧠 Phases Breakdown

### 🟢 Phase 1: Python Foundations
**Status: 🔄 In Progress (CS50P)**

- Syntax, data types, control flow
- Functions & OOP (classes, inheritance, magic methods)
- File handling & modules
- Exceptions & error handling
- Basic API requests

---

### 🟦 Phase 2: FastAPI Basics
**Status: ⏳ Upcoming**

- Why FastAPI over Flask for AI systems
- Routes, request/response models
- Pydantic for data validation
- Async endpoints
- Serving ML model predictions via API
- API testing basics

---

### 🟡 Phase 3: Machine Learning
**Status: ⏳ Upcoming**

> NumPy and Pandas are learned here in context, not as a separate phase

- Supervised & unsupervised learning
- Scikit-learn: pipelines, metrics, cross-validation
- PyTorch: tensors, autograd, training loop
- Hugging Face: pipelines, pretrained models
- Model evaluation & feature engineering

---

### 🟣 Phase 4: NLP Fundamentals
**Status: ⏳ Upcoming**

- Tokenization & text preprocessing
- Word embeddings (Word2Vec, TF-IDF)
- Sentiment analysis & text classification
- Named entity recognition (NER)
- Fine-tuning with Hugging Face Trainer

---

### 🔵 Phase 5: Transformers (How They Work)
**Status: ⏳ Upcoming**

> Dedicated phase based on mentor recommendation — before jumping into LLMs, understand the architecture

- Attention mechanism — what it is and why it matters
- Encoder vs decoder architectures (BERT vs GPT)
- Multi-head attention
- Positional encoding
- Reading and understanding the original "Attention Is All You Need" paper
- Karpathy's "Let's build GPT" walkthrough

---

### 🔴 Phase 6: LLMs + Prompt Engineering
**Status: ⏳ Upcoming**

- How LLMs work: tokens, context window, temperature
- Prompt engineering: zero-shot, few-shot, chain-of-thought
- System prompts and role prompting
- Anthropic / OpenAI API usage
- Streaming responses
- Function/tool calling and structured output (JSON mode)

---

### ⚫ Phase 7: RAG + LangChain + Agents
**Status: ⏳ Upcoming**

> Most employable AI engineering skill right now

- Vector databases: ChromaDB, FAISS
- Embeddings and semantic search
- RAG pipeline: ingest → chunk → embed → retrieve → generate
- LangChain: chains, memory, tools
- AI agents and the ReAct pattern
- Orchestrating agents with Python + FastAPI

---

### 🟤 Phase 8: Deploy + Portfolio
**Status: ⏳ Upcoming**

- Docker basics — containerize your FastAPI app
- Deploy to Render or Railway (free tier)
- GitHub portfolio: 3 pinned projects with real READMEs and demo links
- Hugging Face Spaces — publish live AI demos
- Kaggle — at least one public competition submission

---

## 📊 Progress Tracking

| Phase | Topic | Status |
|-------|-------|--------|
| 1 | Python Foundations | 🔄 In Progress |
| 2 | FastAPI Basics | ⏳ Upcoming |
| 3 | Machine Learning | ⏳ Upcoming |
| 4 | NLP Fundamentals | ⏳ Upcoming |
| 5 | Transformers (Architecture) | ⏳ Upcoming |
| 6 | LLMs + Prompt Engineering | ⏳ Upcoming |
| 7 | RAG + LangChain + Agents | ⏳ Upcoming |
| 8 | Deploy + Portfolio | ⏳ Upcoming |

---

## 🧰 Tech Stack

| Category | Tools |
|----------|-------|
| Language | Python |
| Backend / API | FastAPI |
| ML Framework | scikit-learn, PyTorch |
| NLP / LLMs | Hugging Face Transformers, LangChain |
| Vector DB | ChromaDB, FAISS |
| LLM APIs | Anthropic (Claude), OpenAI |
| Deployment | Docker, Render, Railway |
| Portfolio | GitHub, Hugging Face Spaces |

---

## 📝 Mentor Notes

Key adjustments made to this roadmap based on mentor feedback:

- ✅ **Data Analysis removed as standalone phase** — NumPy/Pandas learned in context during ML
- ✅ **Flask replaced with FastAPI** — industry standard for AI backend services and agent orchestration
- ✅ **DSA removed** — not required for AI engineering track
- ✅ **Transformers added as dedicated phase** — between NLP and LLMs, as recommended
- ✅ **Focus: Python + FastAPI** — core skill pair for orchestrating AI agents

---

## 👨‍💻 Author

**Carl Joshua M. Coloma**
Computer Science – Software Engineering
AI Engineering Track

> *"The fastest way to learn is to build something you actually care about."*
