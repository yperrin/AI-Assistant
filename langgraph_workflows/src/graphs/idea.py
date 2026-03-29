import os
from typing import Literal

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.messages.ai import AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from langgraph.graph import END, START, StateGraph
from langgraph.types import RetryPolicy

from src.tools.file_ops import write_markdown_artifact

model_name = os.getenv("OLLAMA_THINKING_MODEL", "llama3.1:8b")
print(f"Using Ollama thinking model: {model_name}")
llm = ChatOllama(model=model_name, temperature=0.7)

from src.graphs.researcher import build_researcher_graph
from src.state.idea import IdeaAgentState

def analysis_node(state: IdeaAgentState) -> dict:
    system_prompt = """You are an analyst evaluating ideas.
    Review the current information and determine if some additional information (technical facts or recent data) is needed or more research is required.
    If so, respond with "SEARCH_REQUIRED: [specific information needed]". If not, respond with "NO_SEARCH_REQUIRED"."""
    
    user_prompt = f"The idea is: {state['idea']}."
    if state["current_thought"]:
        user_prompt += f"\n\nThe current thought is:\n#########\n{state['current_thought']}\n#########"
    if state["current_dissent"]:
        user_prompt += f"\n\nThe current dissent is:\n#########\n{state['current_dissent']}\n#########"

    print("--- Analysis Node Start ---")
    response = llm.invoke([
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_prompt)
    ])
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
    system_prompt = """You are the pragmatic architect. Your job is to evaluate the idea and provide reasons why the current approach may or may not be effective.
    You are to provide detailed information on the potential pitfalls and weaknesses of the current approach. 
    You should be critical and pragmatic in your analysis, providing a realistic assessment of the challenges and limitations of the idea.
    Also provide feedback whether the idea seems to be based on insufficent information and what information would be needed to make a more informed analysis.
    You do not need to critic the idea if you believe the idea is feasible and the current approach is the best option you can come up with.
    Only output any feedback, criticism, why more reseearch may be needed, and what information would be needed to make a more informed analysis. Do not output anything else."""
    
    user_prompt = f"The idea you are evaluating is: {state['idea']}."
    if state["current_thought"]:
        user_prompt += f"\n\nThe current thought is:\n#########\n{state['current_thought']}\n#########"
    if state["additional_information"]:
        user_prompt += f"\n\nIncorporate the following additional information into your analysis:\n#########\n{state['additional_information']}\n#########"
        
    print("--- Critic Node Start ---")
    response = llm.invoke([
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_prompt)
    ])
    print(response.content)
    print("--- Critic Node End ---")
    return {
        "messages": [AIMessage(content=response.content, name="Critic")], 
        "current_dissent": response.content,
    }


def architect_node(state: IdeaAgentState) -> dict:
    """Analyzes the problem and the current information and provides a comprehensive analysis."""
    system_prompt = """You are the idea architect. Your job is to evaluate the idea and provide an analysis of the idea as to pros/cons and feasibility.
    You are optimistic and open-minded in your analysis, providing a hopeful assessment of the potential of the idea while also acknowledging the challenges and limitations of the idea.
    If the idea is deemed to be a good idea, provide suggestions on how the idea could be developed or implemented."""
    
    user_prompt = f"The idea you are evaluating is: {state['idea']}."
    if state["current_thought"]:
        user_prompt += f"\n\nThe current thought is:\n#########\n{state['current_thought']}\n#########"
    if state["current_dissent"]:
        user_prompt += "\n\nExpand the current thought by incorporating the dissent in order to create a more fully thought out analysis."
        user_prompt += f"\nThe current dissent is:\n#########\n{state['current_dissent']}\n#########"
    if state["additional_information"]:
        user_prompt += f"\n\nReview this additional information to complement the analysis:\n#########\n{state['additional_information']}\n#########"
        
    print("--- Architect Node Start ---")
    response = llm.invoke([
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_prompt)
    ])
    print(response.content)
    print("--- Architect Node End ---")
    return {
        "messages": [AIMessage(content=response.content, name="Architect")], 
        "current_thought": response.content,
        "current_dissent": "",
    }


def research_node(state: IdeaAgentState) -> dict:
    """Uses Gemini to perform web-grounded research on the query."""
    import os
    model_name = os.getenv("GOOGLE_SEARCH_MODEL", "gemini-2.5-flash-lite")
    llm = ChatGoogleGenerativeAI(model=model_name, temperature=0.4)
    if state["messages"] and len(state["messages"]) > 0:
        query = state["messages"][-1].content
    else:
        query = f"""
        Create an initial research to gather information on the following idea: {state["idea"]}.
        Find existing information, data, and research related to the idea. Focus on finding recent developments, technical details, and relevant data that can inform the analysis of the idea.
        When appropriate, provide alternative solutions to approach the idea and analyze their pros and cons.
        Provide a summary of the most relevant and up-to-date information you can find on the idea, including any recent advancements, technical details, and data that can inform the analysis of the idea.
        """
    print("--- Researcher Node Start---")
    response = llm.invoke(
        [
            SystemMessage(
                content=(
                    "You are an expert Technical Research Analyst. Your goal is to provide a comprehensive, fact-based synthesis of the requested topic using the google_search tool. "
                    "Follow these execution rules: "
                    "1. Search Strategy: Perform multiple search queries if necessary to capture different angles (e.g., technical specs, recent news, expert critiques). "
                    "2. Data Integrity: Prioritize primary sources, official documentation, and reputable industry analysis. "
                    "3. Structure: Organize information using clear headers, bullet points, and tables for data comparison. "
                    "4. Depth: Do not just summarize; analyze the 'why' and 'how.' For technical topics, focus on architectural implications and trade-offs. "
                    "5. Conciseness: Use professional, 'to the point' language. Avoid conversational filler or redundant introductory phrases. "
                    "6. Critical Analysis: Where applicable, include a brief critical analysis of the information found, highlighting potential biases or gaps in the data. "
                    "7. Make suggestions as to what additional information would be needed to make a more informed analysis. "
                )
            ),
            HumanMessage(content=query),
        ],
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
