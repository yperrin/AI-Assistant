---
name: idea-processor
description: |
  Analyze and route ideas from the inbox using a multi-agent LangGraph workflow.
  Use this when there are new ideas in 'inbox/ideas' that need evaluation, 
  architectural analysis, and routing to projects or rejection.
---

# Idea Processor Skill

This skill executes the multi-agent orchestration to evaluate markdown files in the `inbox/ideas` directory.

## Workflow

1.  **Preparation**: Ensure the `inbox/ideas` directory contains the `.md` files to be processed.
2.  **Environment**: Ensure the `.env` file in `tools/idea_processor/` has valid keys for Gemini and Ollama.
3.  **Execution**: Run the processor using `uv`.
4.  **Routing**:
    - **APPROVED**: Files are moved to `projects/<idea-name>/` along with a generated `technical_specification.md`.
    - **REJECTED**: Files are moved to `inbox/rejected_ideas/` with an appended AI evaluation rationale.

## Execution Command

```powershell
uv run python -m src.main
```

> [!NOTE]
> This command should be run from the `d:\Projects\brain\tools\idea_processor` directory.
