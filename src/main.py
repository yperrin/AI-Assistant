import uuid

from dotenv import load_dotenv



def main():
    run_id = uuid.uuid4().hex[:8]

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
    from src.graphs.idea import build_idea_graph

    load_dotenv()
    graph = build_idea_graph()
    result = graph.invoke(
        {
            "run_id": run_id,
            "idea": "Is it possible to use langgrapgh to create a process to review ideas",
            "current_thought": "",
            "current_dissent": "",
            "additional_information": "",
            "messages": [],
            "artifacts": [],
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
