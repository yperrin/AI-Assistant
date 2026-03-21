from typing import TypedDict


class ArtifactMetadata(TypedDict):
    file_path: str
    description: str
    agent_source: str


class AgentState(TypedDict):
    run_id: str
    query: str
    research_data: str | None
    artifacts: list[ArtifactMetadata]
