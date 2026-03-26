import operator
from typing import Annotated, List, TypedDict

from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages

from src.state.researcher import ArtifactMetadata


class IdeaAgentState(TypedDict):
    run_id: str
    idea: str
    current_thought: str
    current_dissent: str
    additional_information: str
    messages: Annotated[List[BaseMessage], add_messages]
    artifacts: Annotated[List[ArtifactMetadata], operator.add]
    iteration: int
    max_loop: int

    def __str__(self):
        import json

        return json.dumps({
            "run_id": self.run_id,
            "idea": self.idea,
            "current_thought": self.current_thought,
            "current_dissent": self.current_dissent,
            "additional_information": self.additional_information,
            "messages": len(self.messages),
            "artifacts": len(self.artifacts),
            "iteration": self.iteration,
            "max_loop": self.max_loop
        })