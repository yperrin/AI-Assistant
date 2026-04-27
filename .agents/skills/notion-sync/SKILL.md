---
name: notion-sync
description: |
  Sync Notion 'Journal Entries' database to local Markdown files.
  Run this when the user needs to update the local learning folders with the latest data from Notion.
---

# Notion Synchronization Skill

Use this skill to run the synchronization process that fetches entries from the Notion "Journal Entries" database and saves them as local Markdown files.

## Workflow

1. Navigate to the `tools/notion_sync` directory.
2. Ensure the environment variables in `.env` are set (NOTION_API_KEY, NOTION_DATABASE_ID, GEMINI_API_KEY).
3. Run the synchronization and categorization commands using `uv`.

## Execution Command

```powershell
uv run python src/sync.py
uv run python src/categorizer.py
```

## Post-Execution
- Confirm that new files have been created in `learning/`.
- The synchronization maintains state in `.sync_state.json` to only fetch new or updated entries.
