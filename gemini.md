# Brain Project Agent Workflow Guidelines

## Project Objective
This repository is a personal learning project designed to create agentic workflows that deliver personal value. The primary goal is to build an automated idea and study material pipeline:
1. Fetch data from Notion and save it as local markdown files in an `inbox` or `learning` folder. Training materials in `learning/` are organized into subfolders by year and month (e.g., `2026-04`).
2. Utilize an Idea Processor (built with LangGraph) to review the items in the inbox, analyze feasibility, and propose implementations.

Over time, this system is expected to learn, adapt, and become more personalized to the user's specific workflow.

## Repository Structure & Architecture
The repository relies on a polyglot, micro-project architecture, choosing the best language and tool for each specific job:
- **`langgraph_workflows/`**: A Python-based project utilizing LangGraph to analyze ideas and orchestrate LLM workflows.
- **`notion_sync/`**: A Python project to download data from Notion to local markdown files.
- **`learning/`**: Categorized training materials organized by date (YYYY-MM).
- **`blogs/ai/`**: Professional blog posts about AI created for work.
- **Prompt Prototyping**: Prompts will be prototyped and optionally traced using **Langfuse**.
- **Expansion**: The project may later incorporate tools built with Java, Angular, or n8n based on what is the best fit for future agentic pipelines.

## Knowledge Management & Prioritization
- **Recent Knowledge First**: When retrieving information from the `learning/` or `blogs/ai/` folders, always prioritize the most recent knowledge in case of conflicting information.
- **Date-Based Organization**: Use the YYYY-MM subfolder structure to determine recency.

## Coding Standards
Agents contributing to any sub-project MUST adhere strictly to industry standards for the corresponding language:
- **Python**: Follow PEP 8 guidelines. Prioritize comprehensive type hints, modular codebase structures, robust error handling, and modern standard tooling.
- **Java**: Follow official Java conventions, object-oriented best practices, and standard build tools (e.g., Maven/Gradle).
- **Angular**: Strictly follow the official Angular Style Guide (e.g., strong typing, modular components, reactive architectures).
- **n8n**: Produce clean, readable flow logic with well-named nodes.

## The System Soul
Always refer to the companion `soul.md` file in the root directory. It contains personal preferences, tone guidelines, and customizations that the AI should consider. The AI is expected to update `soul.md` when it learns new, persistent preferences or behavioral rules from the user.
