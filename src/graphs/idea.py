import os
from typing import Literal

from langchain_core.messages.ai import AIMessage
from langchain_ollama import ChatOllama
from langgraph.graph import END, START, StateGraph

from src.tools.file_ops import write_markdown_artifact

model_name = os.getenv("OLLAMA_THINKING_MODEL", "llama3.1:8b")
print(f"Using Ollama thinking model: {model_name}")
llm = ChatOllama(model=model_name, temperature=0.7)

from src.graphs.researcher import build_researcher_graph
from src.state.idea import IdeaAgentState

def analysis_node(state: IdeaAgentState) -> dict:
    """Reviews the idea suggested. Provides feedback on whether more information is needed to create an informed opinion."""
    prompt = f"""You are an analyst evaluating the idea: {state["idea"]}."""
    if state["current_thought"]:
        prompt += f" \nThe current thought is: \n######### \n{state['current_thought']}. \n#########"
    if state["current_dissent"]:
        prompt += f"\nThe current dissent is:  \n######### \n{state['current_dissent']}. \n#########"
    prompt += """ 
        \nReview the current information and determine if some additional information (technical facts or recent data) is needed or more research is required.
        If so, respond with "SEARCH_REQUIRED: [specific information needed]". If not, respond with "NO_SEARCH_REQUIRED".
    """
    print("--- Analysis Node ---")
    response = llm.invoke(prompt)
    print(response.content)
    print("--- Analysis Node ---")
    # Deterministic file write via artifact tool
    subfolder = f"{state['run_id']}/{str(state['iteration'] - 1)}"
    write_markdown_artifact.invoke(
        {"filename": "analysis.json", "content": str(state), "subfolder": subfolder}
    )

    return {"messages": [AIMessage(content=response.content, name="Analyzer")]}


def critic_node(state: IdeaAgentState) -> dict:
    """Analyzes the problem and the current information and provides a comprehensive critic of the current approach."""
    prompt = """
        You are the pragmatic architect. Your job is to evaluate the idea and provide reasons why the current approach may or may not be effective.
        You are to provide detailed information on the potential pitfalls and weaknesses of the current approach. 
        You should be critical and pragmatic in your analysis, providing a realistic assessment of the challenges and limitations of the idea.
        Also provide feedback whether the idea seems to be based on insufficent information and what information would be needed to make a more informed analysis.
        You do not need to critic the idea if you believe the idea is feasible and the current approach is the best option you can come up with.
        Only output any feedback, criticism, why more reseearch may be needed, and what information would be needed to make a more informed analysis. Do not output anything else.
    """
    prompt += f"""\nThe idea you are evaluating is: {state["idea"]}."""
    if state["current_thought"]:
        prompt += f" \nThe current thought is: \n######### \n{state['current_thought']}. \n#########"
    if state["additional_information"]:
        prompt += f"""Incorporate the following additional information into your analysis: \n######### \n{state["additional_information"]}.\n#########"""
    print("--- Critic Node ---")
    response = llm.invoke(prompt)
    print(response.content)
    print("--- Critic Node ---")
    return {"messages": [AIMessage(content=response.content, name="Critic")], "current_dissent": response.content}


def architect_node(state: IdeaAgentState) -> dict:
    """Analyzes the problem and the current information and provides a comprehensive analysis."""
    prompt = """
        You are the idea architect. Your job is to evaluate the idea and provide an analysis of the idea as to pros/cons and feasibility.
        You are optimistic and open-minded in your analysis, providing a hopeful assessment of the potential of the idea while also acknowledging the challenges and limitations of the idea.
        If the idea is deemed to be a good idea, provide suggestions on how the idea could be developed or implemented.
    """
    prompt += f"""\nThe idea you are evaluating is: {state["idea"]}."""
    if state["current_thought"]:
        prompt += f" \nThe current thought is: \n######### \n{state['current_thought']}. \n#########"
    if state["current_dissent"]:
        prompt += """Expand the current thought by incorporating the dissent in order to create a more fully thought out analysis."""
        prompt += f"\nThe current dissent is: \n######### \n{state['current_dissent']}. \n#########"
    if state["additional_information"]:
        prompt += f"""Review this additional information to complement the analysis: \n######### \n{state["additional_information"]}.\n#########"""
    print("--- Architect Node ---")
    response = llm.invoke(prompt)
    print(response.content)
    print("--- Architect Node ---")
    return {
        "messages": [AIMessage(content=response.content, name="Architect")], 
        "current_thought": response.content,
        "current_dissent": "",
        "iteration": state["iteration"] + 1
    }


def research_graph(state: IdeaAgentState) -> dict:
    """The Researcher - External API calls for up-to-date information."""
    if state["messages"] and len(state["messages"]) > 0:
        query = state["messages"][-1].content
    else:
        state["idea"]
        query = f"""
        Create an initial research to gather information on the following idea: {state["idea"]}.
        Find existing information, data, and research related to the idea. Focus on finding recent developments, technical details, and relevant data that can inform the analysis of the idea.
        When appropriate, provide alternative solutions to approach the idea and analyze their pros and cons.
        Provide a summary of the most relevant and up-to-date information you can find on the idea, including any recent advancements, technical details, and data that can inform the analysis of the idea.
        """
    research_graph = build_researcher_graph()
    print("--- Research Node ---")
    response = research_graph.invoke(
        {
            "parent_run_id": state["run_id"],
            "run_id": str(state["iteration"]),
            "query": query,
            "research_data": None,
            "artifacts": [],
        }
    )

    # Ensure response["research_data"] is properly structured
    research_data = response.get("research_data", "")
    if isinstance(research_data, dict):
        research_data_content = research_data.get("content", "")
    else:
        research_data_content = str(research_data)
    return {
        "artifacts": response["artifacts"], 
        "additional_information": research_data_content,
        "messages": [AIMessage(content=research_data_content, name="Researcher", role="assistant")]
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
    workflow.add_node("Architect", architect_node)
    workflow.add_node("Critic", critic_node)
    workflow.add_node("Researcher", research_graph)
    workflow.add_node("Analysis", analysis_node)

    workflow.add_edge(START, "Researcher")
    workflow.add_edge("Researcher", "Architect")
    workflow.add_edge("Architect", "Critic")
    workflow.add_edge("Critic", "Analysis")
    workflow.add_conditional_edges("Analysis", route_discussion, {"Researcher": "Researcher", "continue": END})

    return workflow.compile()
