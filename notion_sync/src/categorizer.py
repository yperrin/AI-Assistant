import os
import logging
from pathlib import Path
from dotenv import load_dotenv
import frontmatter
from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from typing import Literal

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables for local testing (though uv usually loads them, it's good practice)
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Setup paths
BASE_DIR = Path(os.environ.get("BRAIN_DIR", "d:/Projects/brain"))
LEARNING_DIR = BASE_DIR / "learning"

# Define the Pydantic schema for the LLM output
class FileMetadata(BaseModel):
    summary: str = Field(description="A 1-2 sentence TL;DR summary of the document.")
    topics: list[str] = Field(description="A list of core topics discussed in the document (e.g. ['Machine Learning', 'Python']).")
    tools_mentioned: list[str] = Field(description="A list of specific tools or frameworks mentioned (e.g. ['LangGraph', 'Next.js', 'Obsidian']).")
    complexity: Literal["Beginner", "Intermediate", "Advanced"] = Field(description="The technical complexity of the content.")

def get_markdown_files():
    """Yield all markdown files in the specified directories."""
    if LEARNING_DIR.exists():
        yield from LEARNING_DIR.rglob("*.md")

def main():
    if not GEMINI_API_KEY:
        logging.error("GEMINI_API_KEY must be set in .env")
        return

    # Initialize the client
    client = genai.Client(api_key=GEMINI_API_KEY)
    
    total_processed = 0
    total_skipped = 0

    for filepath in get_markdown_files():
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
            
            # Check if already processed
            if post.metadata.get('processed_by_ai') is True:
                total_skipped += 1
                continue
                
            logging.info(f"Processing: {filepath.name}...")
            
            # Extract content to send to LLM
            content = post.content
            if not content.strip():
                logging.info(f"Skipping {filepath.name} because it is empty.")
                continue
                
            # Send to Gemini Flash using Structured Outputs
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=[
                    "Analyze the following markdown document and extract the requested metadata.",
                    content
                ],
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=FileMetadata,
                    temperature=0.1,
                )
            )
            
            # Parse the structured response
            metadata: FileMetadata = response.parsed
            if not metadata:
                logging.warning(f"Failed to parse metadata from Gemini for {filepath.name}")
                continue
                
            # Update the frontmatter dictionary
            post.metadata['processed_by_ai'] = True
            post.metadata['summary'] = metadata.summary
            post.metadata['topics'] = metadata.topics
            post.metadata['tools_mentioned'] = metadata.tools_mentioned
            post.metadata['complexity'] = metadata.complexity
            
            # Write back the file preserving the markdown body
            with open(filepath, 'wb') as f:
                frontmatter.dump(post, f)
            
            total_processed += 1
            
        except Exception as e:
            logging.error(f"Error processing {filepath.name}: {e}")

    logging.info(f"Categorization complete. Processed {total_processed} new files. Skipped {total_skipped} existing files.")

if __name__ == "__main__":
    main()
