import os
import uuid

from dotenv import load_dotenv
load_dotenv()

from src.graphs.idea import build_idea_graph

def main():
    run_id = uuid.uuid4().hex[:8]   
    graph = build_idea_graph()
    result = graph.invoke(
        {
            "run_id": run_id,
            "idea": "I want to create a process to review coding ideas for feasibility and eventually propose the top 2 possible implementations that would allow to implement the solution. Make sure to describe the technology to use for the solutions",
            "current_thought": "",
            "current_dissent": "",
            "additional_information": "",
            "messages": [],
            "artifacts": [],
            "iteration": 0,
            "max_loop": 4,
        }
    )
    print("--- Research Complete ---")
    print(f"{result['current_thought']}")
    print("--- Research Artifacts ---")
    for artifact in result["artifacts"]:
        print(f"Artifact saved: {artifact['file_path']}")
        print(f"  Description: {artifact['description']}")
        print(f"  Source: {artifact['agent_source']}") 


if __name__ == "__main__":
    main()



    """
    from src.graphs.researcher import build_researcher_graph

    load_dotenv()
    graph = build_researcher_graph()

    result = graph.invoke(
        {
            "parent_run_id": run_id,
            "run_id": run_id,
            "query": "What are the latest advancements in quantum computing in 2026?",
            "research_data": None,
            "artifacts": [],
        }
    )
    print("--- Research Complete ---")
    for artifact in result["artifacts"]:
        print(f"Artifact saved: {artifact['file_path']}")
        print(f"  Description: {artifact['description']}")
        print(f"  Source: {artifact['agent_source']}") 
    """
