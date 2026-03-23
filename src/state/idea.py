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
    max_loop: int
