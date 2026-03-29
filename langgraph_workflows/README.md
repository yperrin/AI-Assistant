# Multi-Agent Workflows Project

This project explores the use of multiple AI agents interacting through [LangGraph](https://github.com/langchain-ai/langgraph), leveraging both local and online models to evaluate ideas and perform research.

## Models Used
* `llama3.1:8b` (Local via Ollama): Used for synthesis, architecture, and writing.
* `qwen2.5-coder:7b` (Local via Ollama): Used for coding tasks (where applicable).
* `deepseek-r1:8b` (Local via Ollama): Used for planning and debating.
* `gemini-2.5-flash-lite` (Online via Google GenAI): Used for web-grounded research via Google Search.

## Agent Workflows

The project currently implements two main LangGraph state-graphs:

### 1. Idea Evaluation Workflow (`src/graphs/idea.py`)
This workflow iteratively evaluates an idea by simulating an active debate and research process between different agent personas:
* **Researcher Node**: Uses Gemini to perform web searches to gather recent, fact-based data on an idea.
* **Architect Node**: Acts as the optimistic "idea architect". It uses Ollama to evaluate the idea's pros, cons, and feasibility, proposing potential implementations.
* **Critic Node**: Acts as the pragmatic architect. It actively challenges the idea and the Architect's thought process, highlighting weaknesses, pitfalls, and missing information.
* **Analysis Node**: Evaluates the current state of the discussion and determines if further information is required. If `SEARCH_REQUIRED` is triggered, it loops back to the Researcher. Otherwise, the loop continues or completes based on maximum iterations.

### 2. Researcher Workflow (`src/graphs/researcher.py`)
A direct pipeline for comprehensive research and reporting:
* **Researcher Node**: Uses Gemini and Google Search to gather direct responses and data on a query.
* **Writer Node**: Uses Ollama to digest the raw research data and format it into a structured Markdown report highlighting Overview, Key Findings, Analysis, Risks, and Areas for additional research.

Artifacts and intermediate steps for all graphs are locally written out using a deterministic file-op tool.

## Setup Instructions

### Environment Setup
You must create a `.env` file at the root. Key variables:
```env
OLLAMA_THINKING_MODEL="llama3.1:8b"
OLLAMA_SEARCH_MODEL="llama3.1:8b"
OLLAMA_HOST="http://localhost:11434"
GOOGLE_SEARCH_MODEL="gemini-2.5-flash-lite"
GOOGLE_API_KEY="..." # For Gemini
```

### Dependency Management (Using `uv`)
* install: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
* create the `.venv` folder: `uv venv`
* activate: `.venv\Scripts\activate`
* to install all packages in `pyproject.toml`: `uv sync`

## Running the Application
* Execute the main idea evaluation workflow: `python -m src.main`

## Training & References
* [LangGraph Complete Course](https://www.youtube.com/watch?v=jGg_1h0qzaM)
* [LangChain Crash Course](https://www.youtube.com/watch?v=J7j5tCB_y4w)
