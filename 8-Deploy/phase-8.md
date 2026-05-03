# Phase 8 · Deploy + CI/CD + Portfolio
> **~4 weeks | Month 8**

## Mentor Note
Two live links beats ten local projects — every time. Senior engineers reviewing your GitHub **will notice** whether your repos have CI or not. Deployment is not a bonus step. It's the difference between a portfolio and a collection of exercises. By the end of this phase, your RAG chatbot is live, your GitHub Actions pipeline is running, and your profile is ready to send to a hiring manager.

---

## What You'll Learn

- **Docker** — write a real `Dockerfile` for your FastAPI app. Understand every line: base image, working directory, dependencies, exposed port, entrypoint. Don't copy-paste blindly.
- **Docker Compose** — run your app + Redis + ChromaDB together locally with one command.
- **Render / Railway** — deploy your Dockerized app to the cloud on the free tier. Get a live HTTPS URL.
- **GitHub Actions** — CI/CD pipeline that runs your tests on every push and deploys on merge to `main`. This is the professional standard.
- **Secrets Management** — environment variables in Render/Railway dashboards, GitHub Actions secrets. No API keys in code, ever.
- **Hugging Face Spaces** — publish a Gradio or Streamlit demo of your RAG chatbot for a shareable, no-login-required live demo link.
- **GitHub Portfolio Polish** — pinned repos, professional READMEs with architecture diagrams and demo links, contribution graph that shows consistent activity.
- **Writing About Your Work** — every repo needs: what it does, why it exists, how to run it, and a link to the live demo. One paragraph minimum.

---

## 📦 Project — Capstone: Live RAG Chatbot with CI/CD

**Docker + Render/Railway + GitHub Actions + HuggingFace Spaces**

Deploy your Phase 7 RAG chatbot as a complete, production-style system:

1. **Dockerize** — write a `Dockerfile` for your FastAPI backend. Test it locally with `docker build` and `docker run`.
2. **Docker Compose** — add Redis and ChromaDB services. One `docker compose up` runs the full stack locally.
3. **Deploy to Render or Railway** — push your Docker image, set environment variables in the dashboard, get a live HTTPS URL.
4. **GitHub Actions CI/CD**:
   - On push → run `pytest` against your API
   - On merge to `main` → auto-deploy to Render/Railway
5. **HuggingFace Spaces** — create a Gradio frontend that calls your deployed FastAPI backend. Shareable demo link, no login required.
6. **GitHub Portfolio**:
   - Pin your top 3–5 repos
   - Every pinned repo has: clear title, description, architecture diagram, live demo link, RAGAS results (for the RAG project)
   - Profile README with a short bio, tech stack, and links to live projects

---

## Resources

| Resource | What You Get | Format | Cost |
|----------|-------------|--------|------|
| Docker official — Getting Started | The right way to learn Docker. Go through it once fully. | Docs | Free |
| TechWorld with Nana — Docker tutorial (YouTube) | Best beginner Docker course. Full walkthrough with real examples. | Video | Free |
| GitHub Actions docs — Quickstart | Official guide to writing your first workflow. | Docs | Free |
| Render docs (render.com/docs) | Deploy a Docker container in 15 minutes. Free tier is enough. | Docs | Free |
| Railway docs (docs.railway.app) | Alternative to Render. Slightly easier setup, similar free tier. | Docs | Free |
| HuggingFace Spaces — Gradio guide | Deploy a live demo in minutes. Use this for your shareable portfolio link. | Docs | Free |
| Makeareadme.com | Template and guide for writing professional READMEs. | Tool | Free |

---

## Portfolio Checklist
Before calling this phase complete, verify every item:

- [ ] RAG chatbot is live with a public HTTPS URL
- [ ] GitHub Actions runs tests on every push
- [ ] GitHub Actions deploys on merge to `main`
- [ ] HuggingFace Space is live and shareable
- [ ] Every pinned repo has a proper README with a demo link
- [ ] No API keys or secrets in any repo (check with `git log` if unsure)
- [ ] Architecture diagram exists for the RAG project
- [ ] RAGAS evaluation results are documented

---

## Tips
- Render free tier spins down after inactivity. Add a simple uptime ping or mention it in your README so interviewers know to wait 30 seconds on first load.
- GitHub Actions feels complex at first. Start with just the test step, then add deployment once tests pass.
- Your GitHub profile is a living document. Keep committing. Gaps in the contribution graph are noticed.
- You built a full AI system from scratch. Own it. Be able to walk through every layer of it in an interview — from the chunking strategy to the auth middleware to the CI pipeline.