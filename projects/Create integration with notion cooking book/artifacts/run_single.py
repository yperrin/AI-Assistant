import os
import sys
from dotenv import load_dotenv
load_dotenv()

from src.graphs.idea import build_idea_graph
from src.main import process_file

def main():
    filepath = r"d:\Projects\brain\inbox\ideas\Create integration with notion cooking book.md"
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return
        
    print(f"Starting processor for: {filepath}")
    graph = build_idea_graph()
    process_file(filepath, graph)
    print("Finished processing.")

if __name__ == "__main__":
    main()
