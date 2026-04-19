# Brain Project Agent Guidelines

This is the root agent guide for the Brain repository.

## Start Here By Task

- **Synchronization with Notion**: 
  Use the [`notion-sync`](.agents/skills/notion-sync/SKILL.md) skill to fetch the latest journal entries and ideas.
- **Idea Processing**: 
  Workflows in `langgraph_workflows/` analyze ideas fetched from Notion.

## Project Structure

- `notion_sync/`: Python tool to sync Notion data.
- `langgraph_workflows/`: Agents and graphs to process ideas.
- `inbox/`: Temporary storage for synced ideas.
- `learning/`: Categorized training materials.

## Conventions

- Use `uv` for Python dependency management and execution.
- Follow the guidelines in `gemini.md` and `soul.md` for project soul and personality.
