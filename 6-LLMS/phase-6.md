# Phase 6 · LLMs + Prompting + Observability
> **~4 weeks | Month 5–6**

## Mentor Note
Knowing how to call an LLM API is table stakes. What separates junior from mid-level AI engineers is **observability** and **security**. Every LLM call in a production system should be traced. Prompt injection awareness is not optional — it's a real attack vector. Set up LangSmith from day one here, just like you did W&B in Phase 3.

---

## What You'll Learn

- **Tokens vs Words** — LLMs think in tokens. Know how to estimate token count, why it affects cost, and what a context window limit actually means.
- **Temperature & Sampling** — what temperature controls, when to set it low (factual tasks) vs high (creative tasks). Know `top_p` and `top_k` at a surface level.
- **Prompting Techniques** — zero-shot, few-shot, chain-of-thought (CoT), system prompts. Know when to use each and why. CoT alone can dramatically improve reasoning output.
- **Function / Tool Calling** — let the LLM decide when to call a function. This is how agents are built. Understand the request/response cycle.
- **Structured JSON Output** — force the model to return structured data using system prompts or response format parameters. Critical for building reliable AI pipelines.
- **Streaming Responses** — return tokens as they're generated instead of waiting for the full response. Required for any chat interface.
- **LangSmith Tracing** — trace every LLM call: inputs, outputs, latency, token usage. Production systems are blind without this.
- **Prompt Injection Defense** — understand the attack, know the basic mitigations. Sanitize user input before it touches a system prompt.
- **Local LLMs with Ollama** — run `llama3`, `mistral`, or `phi3` locally. Free, private, useful for development and testing.

---

## 📦 Project — FastAPI Chatbot with Memory, Streaming + Observability

**FastAPI + Anthropic/OpenAI API + LangSmith + JWT + Prompt Injection Defense**

Build a production-quality chatbot backend:
- `POST /chat` — accepts user message, returns LLM response (streamed)
- Conversation history maintained per session (in-memory or Redis)
- Structured JSON output for at least one endpoint (e.g. `/analyze`)
- JWT auth protecting all routes
- Rate limiting (reuse Phase 2 pattern)
- Every LLM call traced in **LangSmith** (inputs, outputs, latency, tokens)
- User input sanitized against basic prompt injection patterns
- `.env` for all API keys — no hardcoding

This is not a toy chatbot. This is a real backend a company could use.

---

## Resources

| Resource | What You Get | Format | Cost |
|----------|-------------|--------|------|
| Anthropic — Prompt Engineering Guide | Best prompting reference from the model creators. Read all of it. | Docs | Free |
| OpenAI — Prompt Engineering Guide | Complements Anthropic's guide. Covers function calling well. | Docs | Free |
| LangSmith docs (smith.langchain.com) | Set up tracing in 10 minutes. Do this on day one of the phase. | Docs | Free |
| Ollama (ollama.com) | Run LLMs locally. Pull `llama3` or `mistral` and test locally. | Tool | Free |
| Simon Willison — Prompt Injection blog | The best plain-English explanation of prompt injection risks. | Blog | Free |
| Hamel Husain — LLM Evals blog | How to evaluate LLM outputs beyond vibes. Practical and real. | Blog | Free |

---

## Tips
- Use Anthropic's Claude API or OpenAI — pick one and go deep. Don't bounce between both.
- LangSmith free tier is enough. Set it up before you write your first LLM call.
- Local LLMs via Ollama are free to experiment with. Use them for development, switch to the real API for your portfolio project.
- Streaming is not optional for chat UIs. Learn it here, you'll use it in Phase 7 and 8.