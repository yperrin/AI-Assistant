from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from langgraph.graph import END, StateGraph

from src.state import AgentState
from src.tools.file_ops import write_markdown_artifact


def research_node(state: AgentState) -> dict:
    """Uses Gemini to perform web-grounded research on the query."""
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0.3)
    response = llm.invoke(
        [
            SystemMessage(
                content=(
                    "You are an expert Technical Research Analyst. Your goal is to provide a comprehensive, fact-based synthesis of the requested topic using the google_search tool. "
                    "Follow these execution rules: "
                    "1. Search Strategy: Perform multiple search queries if necessary to capture different angles (e.g., technical specs, recent news, expert critiques). "
                    "2. Data Integrity: Prioritize primary sources, official documentation, and reputable industry analysis. "
                    "3. Structure: Organize information using clear headers, bullet points, and tables for data comparison. "
                    "4. Citations: You MUST provide direct URL links for every key fact or claim made. Append references at the end of sections or inline as [Source Name](URL). "
                    "5. Depth: Do not just summarize; analyze the 'why' and 'how.' For technical topics, focus on architectural implications and trade-offs. "
                    "6. Conciseness: Use professional, 'to the point' language. Avoid conversational filler or redundant introductory phrases. "
                )
            ),
            HumanMessage(content=state["query"]),
        ],
        tools=[{"google_search": {}}],
    )
    return {"research_data": response.content}


def writer_node(state: AgentState) -> dict:
    """Uses Ollama to format research data into Markdown and save via the artifact tool."""
    llm = ChatOllama(model="llama3.1:8b", temperature=0, host="http://localhost:11434")
    response = llm.invoke(
        [
            SystemMessage(
                content=(
                    "You are a technical writer. "
                    "Format the provided research data into a well-structured Markdown report. "
                    "Use headings, bullet points, and sections. "
                    "Output ONLY the Markdown content, no preamble."
                )
            ),
            HumanMessage(
                content=f"Format the following research into a Markdown report:\n\n{state['research_data']}"
            ),
        ]
    )

    # Deterministic file write via artifact tool
    safe_name = state["query"][:50].strip().replace(" ", "_").lower()
    subfolder = f"{state['run_id']}/research_reports"
    path = write_markdown_artifact.invoke(
        {"filename": safe_name, "content": response.content, "subfolder": subfolder}
    )

    artifact = {
        "file_path": path,
        "description": f"Research report: {state['query']}",
        "agent_source": "ollama_writer",
    }
    return {"artifacts": [artifact]}


def build_researcher_graph():
    """Builds and compiles the Phase 1 Researcher -> Writer graph."""
    workflow = StateGraph(AgentState)
    workflow.add_node("researcher", research_node)
    workflow.add_node("writer", writer_node)

    workflow.set_entry_point("researcher")
    workflow.add_edge("researcher", "writer")
    workflow.add_edge("writer", END)

    return workflow.compile()
