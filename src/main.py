import uuid

from dotenv import load_dotenv

from src.graphs.researcher import build_researcher_graph


def main():
    load_dotenv()
    graph = build_researcher_graph()
    run_id = uuid.uuid4().hex[:8]

    result = graph.invoke(
        {
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


if __name__ == "__main__":
    main()
