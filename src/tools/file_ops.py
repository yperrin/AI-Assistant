import re
from pathlib import Path

from langchain_core.tools import tool

ARTIFACTS_ROOT = Path("artifacts")


@tool
def write_markdown_artifact(filename: str, content: str, subfolder: str) -> str:
    """Writes content to a .md file under artifacts/<subfolder>/ and returns the absolute path."""
    safe_filename = re.sub(r"[^\w\-]", "_", filename).strip("_")
    if not safe_filename:
        safe_filename = "report"

    target_dir = ARTIFACTS_ROOT / subfolder
    target_dir.mkdir(parents=True, exist_ok=True)
    full_path = target_dir / f"{safe_filename}.md"

    full_path.write_text(content, encoding="utf-8")
    return str(full_path.resolve())
