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

def format_state(state: IdeaAgentState) -> str:
    return f"""
# Run Details ({state.get('run_id')})
**Iteration:** {state.get('iteration')} / {state.get('max_loop')}
**Messages:** {len(state.get('messages', []))}
**Artifacts:** {len(state.get('artifacts', []))}

## Idea
{state.get('idea')}

## Current Thought
{state.get('current_thought')}

## Current Dissent
{state.get('current_dissent')}

## Additional Information
{state.get('additional_information')}
"""