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

    # Inject soul.md as context for the agents
    soul_path = r"d:\Projects\brain\soul.md"
    soul_content = ""
    if os.path.exists(soul_path):
        with open(soul_path, "r", encoding="utf-8") as f:
            soul_content = f.read()

    idea_with_context = f"{content}\n\n---\n### SYSTEM DIRECTIVE (SOUL CONTEXT)\nThe following is the personal 'Soul' file governing your preferences and ecosystem architecture. You MUST adhere to these principles and constraints when debating, researching, or architecting this idea:\n\n{soul_content}"

    run_id = uuid.uuid4().hex[:8]
    filename = os.path.basename(filepath)

    try:
        result = graph.invoke(
            {
                "run_id": run_id,
                "source_file": filepath,
                "idea": idea_with_context,
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

        print(f"Decision: {decision}")

        # Determine base directory based on decision
        base_dir = APPROVED_DIR if decision == "APPROVED" else REJECTED_DIR
        target_idea_dir = os.path.join(base_dir, filename.replace(".md", ""))
        os.makedirs(target_idea_dir, exist_ok=True)

        # Move original source file
        new_source_path = os.path.join(target_idea_dir, filename)
        
        if decision == "REJECTED":
            # Append rationale to file for historical context
            with open(filepath, "a", encoding="utf-8") as f:
                f.write(f"\n\n### AI Evaluation Rationale\n**Decision**: {decision}\n\n{rationale}\n")
            # Also save rationale as a standalone conclusion file
            rationale_path = os.path.join(target_idea_dir, "evaluation_rationale.md")
            with open(rationale_path, "w", encoding="utf-8") as f:
                f.write(f"# AI Evaluation Rationale\n**Decision**: {decision}\n\n{rationale}\n")
                
        shutil.move(filepath, new_source_path)
        print(f"Moved idea to {new_source_path}")

        # Copy the final tech spec to the root conclusion folder if it exists
        for artifact in result.get("artifacts", []):
            if artifact.get("description") == "Final Technical Specification":
                artifact_src = artifact.get("file_path")
                if artifact_src and os.path.exists(artifact_src):
                    tech_spec_dest = os.path.join(target_idea_dir, "technical_specification.md")
                    shutil.copy2(artifact_src, tech_spec_dest)
                    print(f"Copied tech spec to {tech_spec_dest}")

        # Move the entire artifacts run folder to the target idea folder
        run_artifacts_dir = os.path.join(ARTIFACTS_DIR, run_id)
        artifacts_dest_dir = os.path.join(target_idea_dir, "artifacts")
        
        if os.path.exists(run_artifacts_dir):
            if os.path.exists(artifacts_dest_dir):
                shutil.rmtree(artifacts_dest_dir)
            shutil.move(run_artifacts_dir, artifacts_dest_dir)
            print(f"Moved all artifacts to {artifacts_dest_dir}")

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
