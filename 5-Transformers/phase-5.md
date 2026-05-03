# Phase 5 · Transformers — How They Actually Work

---

## What You'll Learn

- **The Attention Mechanism** — queries, keys, and values. Understand the intuition: attention is the model deciding *what to focus on* when processing each token.
- **Scaled Dot-Product Attention** — why scores are scaled by `√d_k`. This is a real interview question.
- **Multi-Head Attention** — why one attention head isn't enough. Each head learns a different type of relationship.
- **Positional Encoding** — transformers have no built-in sense of order. Understand how position is injected and why it's necessary.
- **The Transformer Block** — attention → add & norm → feed-forward → add & norm. Know this sequence.
- **Encoder-Only vs Decoder-Only** — BERT (encoder, bidirectional) vs GPT (decoder, causal/unidirectional). Know when you'd use each and why.
- **What Fine-Tuning Actually Does** — you're not retraining the transformer from scratch. You're adjusting weights that already encode language understanding.

---

## Resources

| Resource | What You Get | Format | Cost |
|----------|-------------|--------|------|
| Jay Alammar — "The Illustrated Transformer" | The single best visual explanation of transformers. Required reading. | Blog | Free |
| Andrej Karpathy — "Let's build GPT from scratch" (YouTube) | Build a GPT character-level model from scratch in PyTorch. Watch every minute. | Video | Free |
| 3Blue1Brown — "Attention in transformers" (YouTube) | Best visual intuition for attention. Watch this before reading papers. | Video | Free |
| HuggingFace NLP Course — Chapter 1–2 | Practical transformer usage to complement the theory. | Interactive | Free |
| "Attention Is All You Need" (original paper) | Read the abstract, introduction, and architecture section. Not the full paper — yet. | Paper | Free |

---
