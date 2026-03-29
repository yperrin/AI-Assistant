# Synchronization with Notion Project

This project is about downloading my Journal Entries from Notion and saving them to a local database.

## Setup Instructions

### Environment Setup
You must create a `.env` file at the root. Key variables:
```env
NOTION_API_KEY=...
NOTION_DATABASE_ID=...
```

### Dependency Management (Using `uv`)
* install: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
* create the `.venv` folder: `uv venv`
* activate: `.venv\Scripts\activate`
* to install all packages in `pyproject.toml`: `uv sync`

## Running the Application
* Execute the sync process: `uv run python src/sync.py`
