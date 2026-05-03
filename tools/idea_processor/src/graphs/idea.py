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
    content = response.content
    print(content)
    print("--- Architect Node End ---")

    # Extract decisions from the response
    new_decisions = []
    if "RESOLVED_DECISIONS:" in content:
        try:
            # Get everything after RESOLVED_DECISIONS:
            decision_text = content.split("RESOLVED_DECISIONS:")[-1].strip()
            # Split by lines and clean up
            lines = decision_text.split("\n")
            for line in lines:
                line = line.strip()
                if line.startswith("-") or line.startswith("*"):
                    new_decisions.append(line.lstrip("-* ").strip())
                elif not line: # Stop at first empty line after the list
                    if new_decisions: break
                elif len(new_decisions) > 0: # If we already found some and hit a non-list line, stop
                    break
        except Exception as e:
            print(f"Error parsing decisions: {e}")

    return {
        "messages": [AIMessage(content=content, name="Architect")], 
        "current_thought": content,
        "current_dissent": "",
        "decisions_log": new_decisions,
        "status": "refining"
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

    import re
    # Handle case where response.content is a list
    content = response.content
    if isinstance(content, list):
        content = "\n".join(content)
        
    # Clean up massive blocks of spaces that Gemini sometimes generates with grounding
    content = re.sub(r' {3,}', '  ', content).strip()
    
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


def doc_node(state: IdeaAgentState) -> dict:
    """Synthesizes the final results into a technical specification."""
    pm = PromptManager("idea_documenter")
    llm = pm.get_llm()
    messages = pm.render_prompts(state)

    print(f"--- DocWriter Node Start (Model: {pm.get_model_name()}) ---")
    response = llm.invoke(messages)
    content = response.content
    print("--- DocWriter Node End ---")

    # Save the final specification as an artifact
    subfolder = f"{state['run_id']}/final"
    path = write_markdown_artifact.invoke(
        {"filename": "technical_specification.md", "content": content, "subfolder": subfolder}
    )

    artifact = {
        "file_path": path,
        "description": "Final Technical Specification",
        "agent_source": "documenter",
    }

    return {
        "messages": [AIMessage(content=content, name="Documenter")],
        "artifacts": [artifact],
        "status": "evaluating"
    }


def evaluator_node(state: IdeaAgentState) -> dict:
    """Evaluates the final specification and makes a GO/NO-GO decision."""
    pm = PromptManager("idea_evaluator")
    llm = pm.get_llm()
    messages = pm.render_prompts(state)

    print(f"--- Evaluator Node Start (Model: {pm.get_model_name()}) ---")
    response = llm.invoke(messages)
    content = response.content
    print("--- Evaluator Node End ---")

    decision = "PENDING"
    rationale = content

    if "FINAL_DECISION: APPROVED" in content:
        decision = "APPROVED"
    elif "FINAL_DECISION: REJECTED" in content:
        decision = "REJECTED"

    return {
        "decision": decision,
        "rationale": rationale,
        "status": "completed"
    }


def route_discussion(state: IdeaAgentState) -> Literal["Researcher", "Architect", "DocWriter"]:
    last_message = state["messages"][-1]
    
    # 1. Check for Max Iterations
    if state["iteration"] > state["max_loop"]:
        print("--- Routing: Max iterations reached. Documenting. ---")
        return "DocWriter"
    
    # 2. Check for Search Requirement
    if "SEARCH_REQUIRED:" in last_message.content:
        print("--- Routing: Search required. ---")
        return "Researcher"
    
    # 3. Check for Approval
    if "NO_SEARCH_REQUIRED" in last_message.content:
        print("--- Routing: Final approval reached. Documenting. ---")
        return "DocWriter"
    
    # 4. Default: Refine Architecture
    print("--- Routing: Continuing refinement. ---")
    return "Architect"


def build_idea_graph():
    """Builds and compiles the idea agent graph -> Writer graph."""
    workflow = StateGraph(IdeaAgentState)
    retry_policy = RetryPolicy(initial_interval=15.0, max_attempts=3)
    workflow.add_node("Architect", architect_node, retry=retry_policy)
    workflow.add_node("Critic", critic_node, retry=retry_policy)
    workflow.add_node("Researcher", research_node, retry=retry_policy)
    workflow.add_node("Analysis", analysis_node, retry=retry_policy)
    workflow.add_node("DocWriter", doc_node, retry=retry_policy)
    workflow.add_node("Evaluator", evaluator_node, retry=retry_policy)

    workflow.add_edge(START, "Researcher")
    workflow.add_edge("Researcher", "Architect")
    workflow.add_edge("Architect", "Critic")
    workflow.add_edge("Critic", "Analysis")
    
    # The heart of the refinement loop
    workflow.add_conditional_edges(
        "Analysis", 
        route_discussion, 
        {
            "Researcher": "Researcher", 
            "Architect": "Architect", 
            "DocWriter": "DocWriter"
        }
    )

    workflow.add_edge("DocWriter", "Evaluator")
    workflow.add_edge("Evaluator", END)

    return workflow.compile()
