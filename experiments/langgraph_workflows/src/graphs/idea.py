from typing import Literal
from langchain_core.messages.ai import AIMessage
from langgraph.graph import END, START, StateGraph
from langgraph.types import RetryPolicy

from src.tools.file_ops import write_markdown_artifact
from src.tools.prompt_manager import PromptManager
from src.state.idea import IdeaAgentState

def analysis_node(state: IdeaAgentState) -> dict:
    pm = PromptManager("idea_analysis")
    llm = pm.get_llm()
    messages = pm.render_prompts(state)

    print(f"--- Analysis Node Start (Model: {pm.get_model_name()}) ---")
    response = llm.invoke(messages)
    print(response.content)
    print("--- Analysis Node End ---")
    
    # Deterministic file write via artifact tool
    from src.state.idea import format_state
    subfolder = f"{state['run_id']}/{str(state['iteration'])}"
    content = f"""
{format_state(state)}

## Analysis
{response.content}
"""
    write_markdown_artifact.invoke(
        {"filename": "analysis.md", "content": content, "subfolder": subfolder}
    )

    return {
        "messages": [AIMessage(content=response.content, name="Analyzer")],
        "iteration": state["iteration"] + 1
    }


def critic_node(state: IdeaAgentState) -> dict:
    """Analyzes the problem and the current information and provides a comprehensive critic of the current approach."""
    pm = PromptManager("idea_critic")
    llm = pm.get_llm()
    messages = pm.render_prompts(state)

    print(f"--- Critic Node Start (Model: {pm.get_model_name()}) ---")
    response = llm.invoke(messages)
    print(response.content)
    print("--- Critic Node End ---")
    return {
        "messages": [AIMessage(content=response.content, name="Critic")], 
        "current_dissent": response.content,
    }


def architect_node(state: IdeaAgentState) -> dict:
    """Analyzes the problem and the current information and provides a comprehensive analysis."""
    pm = PromptManager("idea_architect")
    llm = pm.get_llm()
    messages = pm.render_prompts(state)

    print(f"--- Architect Node Start (Model: {pm.get_model_name()}) ---")
    response = llm.invoke(messages)
    print(response.content)
    print("--- Architect Node End ---")
    return {
        "messages": [AIMessage(content=response.content, name="Architect")], 
        "current_thought": response.content,
        "current_dissent": "",
    }


def research_node(state: IdeaAgentState) -> dict:
    """Uses Gemini to perform web-grounded research on the query."""
    pm = PromptManager("idea_researcher")
    llm = pm.get_llm()
    messages = pm.render_prompts(state)
    print(f"--- Researcher Node Start (Model: {pm.get_model_name()}) ---")
    response = llm.invoke(
        messages,
        tools=[{"google_search": {}}],
    )

    # Handle case where response.content is a list
    content = response.content
    if isinstance(content, list):
        content = "\n".join(content)
    print(content)
    print("--- Researcher Node End ---")

    # Deterministic file write via artifact tool
    subfolder = f"{state['run_id']}/{str(state['iteration'])}"
    path = write_markdown_artifact.invoke(
        {"filename": "search.md", "content": content, "subfolder": subfolder}
    )

    if state["messages"] and len(state["messages"]) > 0:
        query = state["messages"][-1].content
    else:
        query = f"Initial research for: {state['idea']}"
    artifact = {
        "file_path": path,
        "description": f"Research report: {query}",
        "agent_source": "researcher_writer",
    }
    return {
        "artifacts": [artifact], 
        "additional_information": content,
        "messages": [AIMessage(content=content, name="Researcher", role="assistant")]
    }


def route_discussion(state: IdeaAgentState) -> Literal["Researcher", "continue"]:
    last_message = state["messages"][-1]
    # Check if the agent asked for a web search
    if "SEARCH_REQUIRED:" in last_message.content:
        return "Researcher"
    # If the discussion has gone on long enough, finalize
    if state["iteration"] > state["max_loop"]:
        return "continue"
    return "continue"


def build_idea_graph():
    """Builds and compiles the idea agent graph -> Writer graph."""
    workflow = StateGraph(IdeaAgentState)
    retry_policy = RetryPolicy(initial_interval=15.0, max_attempts=3)
    workflow.add_node("Architect", architect_node, retry=retry_policy)
    workflow.add_node("Critic", critic_node, retry=retry_policy)
    workflow.add_node("Researcher", research_node, retry=retry_policy)
    workflow.add_node("Analysis", analysis_node, retry=retry_policy)

    workflow.add_edge(START, "Researcher")
    workflow.add_edge("Researcher", "Architect")
    workflow.add_edge("Architect", "Critic")
    workflow.add_edge("Critic", "Analysis")
    workflow.add_conditional_edges("Analysis", route_discussion, {"Researcher": "Researcher", "continue": END})

    return workflow.compile()
