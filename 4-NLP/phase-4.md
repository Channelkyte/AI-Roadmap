# Phase 4 · NLP Fundamentals

---

## What You'll Learn

- **Tokenization** — LLMs read tokens, not words. Understand byte-pair encoding (BPE) and why it matters for context windows and cost.
- **Word Embeddings** — words as vectors, semantic similarity, Word2Vec intuition. This is the foundation of how models understand meaning.
- **TF-IDF** — implement it from scratch using Python and NumPy. Then understand why embeddings replaced it.
- **HuggingFace NLP Tasks** — run NER, summarization, sentiment, and question-answering using `pipeline()`. Know which model architecture fits which task.
- **Fine-tuning BERT** — use `Trainer` API to fine-tune `bert-base-uncased` on a classification task. Understand what fine-tuning actually changes in the model.
- **Encoder vs Decoder** — know the difference cold. BERT = encoder (understanding). GPT = decoder (generation). This question comes up in every AI interview.
- **HuggingFace Hub** — push your fine-tuned model to the Hub. Real engineers publish their work.

---

## Resources

| Resource | What You Get | Format | Cost |
|----------|-------------|--------|------|
| HuggingFace NLP Course (huggingface.co/learn) | The definitive NLP + Transformers course. Chapters 1–4 are required. | Interactive | Free |
| Jay Alammar — "The Illustrated Word2Vec" | Best visual explanation of embeddings on the internet. | Blog | Free |
| Jay Alammar — "The Illustrated BERT" | Understand BERT architecturally before fine-tuning it. | Blog | Free |
| Andrej Karpathy — "Let's build the GPT tokenizer" (YouTube) | 2-hour deep dive on tokenization. Watch it once, seriously. | Video | Free |
| HuggingFace Trainer docs | Official reference for fine-tuning. Bookmark it. | Docs | Free |
| Weights & Biases + HuggingFace integration | One-line W&B integration with Trainer. Always use it. | Docs | Free |

---
