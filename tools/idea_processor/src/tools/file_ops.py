from os import replace
import re
from pathlib import Path

from langchain_core.tools import tool

ARTIFACTS_ROOT = Path("artifacts")


@tool
def write_markdown_artifact(filename: str, content: str, subfolder: str) -> str:
    """Writes content to a .md file under artifacts/<subfolder>/ and returns the absolute path."""
    safe_filename = filename
    if not safe_filename:
        safe_filename = "report.md"
    # Replace invalid characters but keep '/' and '.' and remove '*'
    safe_subfolder = re.sub(r"[^\w\-/\.]", "_", subfolder).replace('*', '').replace(':', '').strip("_")

    target_dir = ARTIFACTS_ROOT / safe_subfolder
    target_dir.mkdir(parents=True, exist_ok=True)
    full_path = target_dir / f"{safe_filename}"

    full_path.write_text(content, encoding="utf-8")
    return str(full_path.resolve())
