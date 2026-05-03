import os
import uuid
import glob
import shutil

from dotenv import load_dotenv
load_dotenv()

from src.graphs.idea import build_idea_graph

INBOX_DIR = r"d:\Projects\brain\inbox\ideas"
REJECTED_DIR = r"d:\Projects\brain\inbox\rejected_ideas"
APPROVED_DIR = r"d:\Projects\brain\projects"
ARTIFACTS_DIR = r"d:\Projects\brain\tools\idea_processor\artifacts"

def process_file(filepath: str, graph) -> None:
    print(f"\n==============================================")
    print(f"Processing: {filepath}")
    print(f"==============================================")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    run_id = uuid.uuid4().hex[:8]
    filename = os.path.basename(filepath)

    try:
        result = graph.invoke(
            {
                "run_id": run_id,
                "source_file": filepath,
                "idea": content,
                "current_thought": "",
                "current_dissent": "",
                "additional_information": "",
                "messages": [],
                "artifacts": [],
                "iteration": 0,
                "max_loop": 4,
                "decisions_log": [],
                "status": "initial_research",
            }
        )
        
        decision = result.get("decision", "REJECTED")
        rationale = result.get("rationale", "No rationale provided.")
        
        # Get the technical spec artifact
        tech_spec_path = None
        for artifact in result.get("artifacts", []):
            if artifact.get("description") == "Final Technical Specification":
                tech_spec_path = artifact.get("file_path")
                break

        print(f"Decision: {decision}")

        if decision == "APPROVED":
            # Move source file to projects
            target_project_dir = os.path.join(APPROVED_DIR, filename.replace(".md", ""))
            os.makedirs(target_project_dir, exist_ok=True)
            
            new_source_path = os.path.join(target_project_dir, filename)
            shutil.move(filepath, new_source_path)
            print(f"Moved idea to {new_source_path}")
            
            if tech_spec_path and os.path.exists(tech_spec_path):
                tech_spec_dest = os.path.join(target_project_dir, "technical_specification.md")
                shutil.copy2(tech_spec_path, tech_spec_dest)
                print(f"Copied tech spec to {tech_spec_dest}")
                
        else: # REJECTED
            os.makedirs(REJECTED_DIR, exist_ok=True)
            new_source_path = os.path.join(REJECTED_DIR, filename)
            
            # Append rationale to file
            with open(filepath, "a", encoding="utf-8") as f:
                f.write(f"\n\n### AI Evaluation Rationale\n**Decision**: {decision}\n\n{rationale}\n")
                
            shutil.move(filepath, new_source_path)
            print(f"Moved idea to {new_source_path}")

    except Exception as e:
        print(f"Error processing {filepath}: {e}")

def main():
    graph = build_idea_graph()
    
    if not os.path.exists(INBOX_DIR):
        print(f"Inbox directory not found: {INBOX_DIR}")
        return

    markdown_files = glob.glob(os.path.join(INBOX_DIR, "*.md"))
    if not markdown_files:
        print("No markdown files found in inbox.")
        return

    for filepath in markdown_files:
        process_file(filepath, graph)

if __name__ == "__main__":
    main()
