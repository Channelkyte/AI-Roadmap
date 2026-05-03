# Phase 5 · Transformers — How They Actually Work
> **~3 weeks | Month 5**

## Mentor Note
Do not skip this phase. Most junior AI engineers can use transformers. Very few can explain them. The ones who can explain them — clearly, without notes — are the ones who get hired and trusted with real systems. Your explainer also becomes a permanent portfolio piece that shows depth. Three weeks of focused study will separate you from 80% of other candidates.

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

## 📦 Project — Transformer Explainer (Blog Post or README)

**The deliverable is your own explanation — not running code**

Write a detailed blog post or GitHub README that explains how transformers work in your own words:
- Use diagrams you drew yourself (even hand-drawn and photographed is fine)
- Explain attention, multi-head attention, positional encoding, and the transformer block
- Compare encoder-only vs decoder-only with real model examples
- No copy-pasting from articles. Every sentence should be yours.

Publish it: GitHub README, Notion page, LinkedIn article, or personal blog. Link it in your portfolio. Most junior engineers cannot do this — it is a direct signal of depth.

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

## Tips
- Watch Karpathy's video with a notebook open. Pause and type every line yourself. Passive watching won't cut it.
- 3Blue1Brown first → Jay Alammar second → Karpathy third. That order builds intuition before implementation.
- Your explainer post is more valuable than another code project at this stage. Write it with care.