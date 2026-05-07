# Week 1: Foundations

Build your first AI pipelines and a fully deployed personal career chatbot — all without any agentic framework, just pure Python and the Gemini API.

## What you'll build

| Lab | Title | What you learn |
|-----|-------|----------------|
| `1_lab1.ipynb` | Your First AI Call | Gemini API basics, multi-step pipelines |
| `2_lab2.ipynb` | The LLM Showdown | Multi-model comparison, LLM-as-judge pattern |
| `3_lab3.ipynb` | Your Digital Twin (Part 1) | Gradio chat UI, Reflection / Evaluator pattern |
| `4_lab4.ipynb` | Your Digital Twin (Part 2) | Tool use, the agent loop, HuggingFace deployment |
| `5_extra.ipynb` | The Agent Loop | Build a full agent loop from scratch with TODO tools |

## Before you start

1. Complete setup: see `setup/` for your OS
2. Create `.env` in the project root with your `GEMINI_API_KEY`
3. Install dependencies: `uv sync` from the project root

## Agentic patterns introduced this week

- **Multi-step pipeline** — output of one LLM call feeds the next
- **Parallelization** — same task sent to multiple models
- **LLM-as-Judge** — a model evaluates other models' outputs
- **Reflection** — a model critiques and re-generates its own output
- **Tool use** — LLM calls Python functions to interact with the world
- **Agent loop** — LLM runs tools in a loop until a goal is reached

## The `me/` folder

Labs 3 and 4 use personal profile data:

- `me/summary.txt` — edit this with your own bio (2–3 paragraphs)
- `me/linkedin.pdf` — export your LinkedIn profile as PDF and place it here (optional)

## Deployment

Lab 4 deploys the career chatbot to HuggingFace Spaces using `app.py`.
Before deploying: update `self.name` in `app.py` and fill in `me/summary.txt`.
