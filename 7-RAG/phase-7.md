# Phase 7 · RAG + LangChain + Agents
> **~5 weeks | Month 6–7 | Most Employable Skill Right Now**

## Mentor Note
This is what companies are actively building and hiring for right now. If you can ship a working RAG system with evaluation metrics, you are ahead of most self-taught AI engineers applying for the same roles. LangGraph has replaced basic LangChain agents as the production standard — learn both, but prioritize LangGraph for anything stateful. Your Phase 7 project is your portfolio centerpiece. Treat it like a real product.

---

## What You'll Learn

- **Why RAG Exists** — LLMs hallucinate on facts they weren't trained on. RAG grounds responses in real documents. Understand the problem before the solution.
- **Vector Databases** — embeddings stored as vectors, similarity search (cosine, dot product). ChromaDB to start, know that Pinecone/Weaviate exist for production scale.
- **Document Chunking** — why you can't just feed a whole PDF into an LLM. Chunk size (~500 tokens), overlap (~50 tokens), and why both matter for retrieval quality.
- **Full RAG Pipeline** — ingest → chunk → embed → store → retrieve → generate. Know every step and what can break at each one.
- **Conversational RAG** — add memory so the chatbot understands follow-up questions in context.
- **LangChain** — chains, document loaders, retrievers, prompt templates. The glue of most AI pipelines.
- **LangGraph** — stateful agents with graph-based control flow. This is the production-grade way to build agents with loops, conditions, and memory.
- **Model Context Protocol (MCP)** — how agents call external tools (APIs, databases, search). The emerging standard for tool use.
- **Redis Embedding Cache** — don't re-embed the same documents on every run. Cache embeddings, save time and cost.
- **RAGAS Evaluation** — measure your RAG system properly: faithfulness, answer relevancy, context precision, context recall. Vibes are not a metric.

---

## 📦 Project — RAG Chatbot over Philippine Documents

**LangChain + ChromaDB + LangGraph + FastAPI + LangSmith + RAGAS**

This is your portfolio centerpiece. Build it like a real product:

1. **Ingest** real documents — university syllabi, PH laws, government issuances, technical docs, anything locally relevant
2. **Chunk and embed** documents into **ChromaDB** with Redis caching for embeddings
3. **Build the RAG pipeline** — retrieve top-K relevant chunks, inject into LLM context, generate grounded answers
4. **Add conversational memory** using LangGraph so follow-up questions work naturally
5. **Wrap in FastAPI** — `POST /chat`, `POST /ingest`, `GET /health` — with JWT auth and rate limiting
6. **Trace everything** in LangSmith — retrieval steps, LLM calls, latency, token usage
7. **Evaluate with RAGAS** — run an evaluation set and include the report in your README
8. **Push to GitHub** with an architecture diagram, live demo link (added in Phase 8), and your RAGAS results

---

## Resources

| Resource | What You Get | Format | Cost |
|----------|-------------|--------|------|
| LangChain docs (python.langchain.com) | Official reference. Read the RAG and retrieval sections thoroughly. | Docs | Free |
| LangGraph docs (langchain-ai.github.io/langgraph) | The production agent framework. Work through all quickstart examples. | Docs | Free |
| Greg Kamradt — LangChain cookbook (YouTube) | Practical LangChain walkthroughs. Chunking strategy video is essential. | Video | Free |
| ChromaDB docs (trychroma.com) | Set up a local vector DB in minutes. Read the quickstart and cookbook. | Docs | Free |
| RAGAS docs (docs.ragas.io) | Evaluation framework for RAG. Required — don't ship without metrics. | Docs | Free |
| Pinecone — "What is RAG?" (learning.pinecone.io) | Best written RAG explainer. Read before building. | Article | Free |
| Redis docs — caching basics | Understand how to cache embeddings. Don't re-embed on every run. | Docs | Free |

---

## Tips
- Pick documents that are genuinely useful and locally relevant. A RAG chatbot over Philippine laws or university policies is far more interesting to a hiring manager than one over a generic Wikipedia dump.
- Start without LangGraph first — get a working RAG pipeline with basic LangChain, then refactor to LangGraph for stateful conversation. Don't learn both at once.
- Your RAGAS evaluation report should be in the README. Numbers show you understand quality, not just functionality.
- This project will be deployed in Phase 8. Build it clean from the start.