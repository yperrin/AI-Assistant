from typing import TypedDict


class ArtifactMetadata(TypedDict):
    file_path: str
    description: str
    agent_source: str


class ResearcherAgentState(TypedDict):
    parent_run_id: str
    run_id: str
    query: str
    research_data: str | None
    artifacts: list[ArtifactMetadata]
