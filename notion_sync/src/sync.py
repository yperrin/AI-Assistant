import os
import json
import logging
from datetime import datetime, timezone
from pathlib import Path
from dotenv import load_dotenv

from notion_client import Client
from notion2md.exporter.block import StringExporter

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables
load_dotenv()
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

# Setup paths
BASE_DIR = Path(os.environ.get("BRAIN_DIR", "d:/Projects/brain"))
INBOX_IDEAS_DIR = BASE_DIR / "inbox" / "ideas"
LEARNING_DIR = BASE_DIR / "learning"

# State file relative to current script's project dir
STATE_FILE_PATH = Path(__file__).parent.parent / ".sync_state.json"

def get_last_sync_time() -> str:
    """Returns ISO format date string of last sync, or a default past date."""
    if STATE_FILE_PATH.exists():
        try:
            with open(STATE_FILE_PATH, 'r') as f:
                state = json.load(f)
                return state.get("last_synced_time", "2000-01-01T00:00:00.000Z")
        except Exception as e:
            logging.error(f"Failed to read state file: {e}")
    return "2000-01-01T00:00:00.000Z"

def save_last_sync_time(sync_time: str):
    with open(STATE_FILE_PATH, 'w') as f:
        json.dump({"last_synced_time": sync_time}, f)

def resolve_filename_collision(target_path: Path) -> Path:
    """If file exists, append _1, _2, etc."""
    if not target_path.exists():
        return target_path
    
    base_name = target_path.stem
    ext = target_path.suffix
    directory = target_path.parent
    
    counter = 1
    new_path = directory / f"{base_name}_{counter}{ext}"
    while new_path.exists():
        counter += 1
        new_path = directory / f"{base_name}_{counter}{ext}"
        
    return new_path

def sanitize_filename(name: str) -> str:
    # Extremely basic sanitization to avoid path traversal/invalid chars
    keepcharacters = (' ', '.', '_', '-')
    sanitized = "".join(c for c in name if c.isalnum() or c in keepcharacters).rstrip()
    return sanitized if sanitized else "Untitled"

def process_page(page: dict, client: Client):
    page_id = page['id']
    props = page.get('properties', {})
    
    # Extract Title (assuming column is called 'Name' or 'title' type)
    title = "Untitled"
    for prop_name, prop_data in props.items():
        if prop_data.get('type') == 'title':
            title_parts = prop_data.get('title', [])
            if title_parts:
                title = sanitize_filename("".join([t.get('plain_text', '') for t in title_parts]))
            break

    # Extract Categories
    categories = []
    cat_prop = props.get('Categories', {})
    cat_type = cat_prop.get('type')
    
    if cat_type == 'select' and cat_prop.get('select'):
        categories.append(cat_prop['select'].get('name'))
    elif cat_type == 'multi_select':
        categories.extend([c.get('name') for c in cat_prop.get('multi_select', [])])
        
    if not categories:
        logging.info(f"Skipping {title} ({page_id}): No categories found.")
        return
        
    # Check if category matches our targets
    is_idea = any('Idea' in str(c) for c in categories)
    is_training = any('Training' in str(c) for c in categories)
    
    if not (is_idea or is_training):
        logging.info(f"Skipping {title} ({page_id}): Category not Idea or Training.")
        return
        
    # Extract Date from "Date" property or fallback to page creation time
    date_str = page.get('created_time')
    date_prop = props.get('Date', {})
    if date_prop.get('type') == 'date' and date_prop.get('date'):
        date_str = date_prop['date'].get('start', date_str)
        
    # Parse YYYY-MM
    try:
        dt = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
        yyyy_mm = dt.strftime("%Y-%m")
    except Exception:
        yyyy_mm = "Unknown"
        
    # Determine target directory
    target_dir = None
    if is_idea:
        target_dir = INBOX_IDEAS_DIR
    elif is_training:
        target_dir = LEARNING_DIR / yyyy_mm
        
    target_dir.mkdir(parents=True, exist_ok=True)
    
    target_path = target_dir / f"{title}.md"
    target_path = resolve_filename_collision(target_path)
    
    logging.info(f"Exporting {title} to {target_path} (Categories: {', '.join(categories)})")
    
    try:
        # StringExporter uses NOTION_TOKEN env var implicitly
        md_content = StringExporter(block_id=page_id).export()
        
        # Prepend a metadata block (frontmatter)
        frontmatter = f"---\ntitle: {title}\nid: {page_id}\nurl: {page.get('url')}\n---\n\n"
        
        with open(target_path, 'w', encoding='utf-8') as f:
            f.write(frontmatter + md_content)
    except Exception as e:
        logging.error(f"Failed to export {title}: {e}")

def main():
    if not NOTION_TOKEN or not DATABASE_ID:
        logging.error("NOTION_TOKEN and NOTION_DATABASE_ID must be set in .env")
        return

    # Set up client
    client = Client(auth=NOTION_TOKEN)
    
    last_sync = get_last_sync_time()
    logging.info(f"Starting sync for edited pages starting after {last_sync}")
    
    has_more = True
    next_cursor = None
    
    # Use the script start time as the next "last_sync" timestamp 
    # so we don't miss entries edited while the script runs.
    curr_time_utc = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    
    # Ensure our root dirs exist
    INBOX_IDEAS_DIR.mkdir(parents=True, exist_ok=True)
    LEARNING_DIR.mkdir(parents=True, exist_ok=True)
    
    # 1. Retrieve the database object
    journals_database = client.databases.retrieve(database_id=DATABASE_ID)
    journals_database_id = journals_database["data_sources"][0]["id"]
    has_more = True
    next_cursor = None

    while has_more:
        response = client.data_sources.query(
            data_source_id=journals_database_id,
            filter={
                "property": "Date",
                "date": {
                    "after": last_sync
                }
            },
            start_cursor=next_cursor
        )
        print(response)
        results = response["results"]

        if not results:
            logging.info("No new entries found.")
        
        for page in results:
            process_page(page, client)
                
        next_cursor = response.get("next_cursor")
        has_more = response.get("has_more", False)
        
    save_last_sync_time(curr_time_utc)
    logging.info(f"Sync complete. Updated last sync time: {curr_time_utc}")

if __name__ == "__main__":
    main()
