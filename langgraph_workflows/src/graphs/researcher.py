from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from langgraph.graph import END, StateGraph

from src.state.researcher import ResearcherAgentState
from src.tools.file_ops import write_markdown_artifact


def research_node(state: ResearcherAgentState) -> dict:
    """Uses Gemini to perform web-grounded research on the query."""
    import os
    model_name = os.getenv("GOOGLE_SEARCH_MODEL", "gemini-2.5-flash-lite")
    llm = ChatGoogleGenerativeAI(model=model_name, temperature=0.4)
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
                    "7. Critical Analysis: Where applicable, include a brief critical analysis of the information found, highlighting potential biases or gaps in the data. "
                )
            ),
            HumanMessage(content=state["query"]),
        ],
        tools=[{"google_search": {}}],
    )

    # Handle case where response.content is a list
    content = response.content
    if isinstance(content, list):
        content = "\n".join(content)

    # Deterministic file write via artifact tool
    subfolder = f"{state['run_id']}"
    if state['parent_run_id']:
        subfolder = f"{state['parent_run_id']}/{subfolder}"
    write_markdown_artifact.invoke(
        {"filename": "search.md", "content": content, "subfolder": subfolder}
    )
    return {"research_data": content}


def writer_node(state: ResearcherAgentState) -> dict:
    """Uses Ollama to format research data into Markdown and save via the artifact tool."""
    import os
    model_name = os.getenv("OLLAMA_SEARCH_MODEL", "llama3.1:8b")
    model_host = os.getenv("OLLAMA_HOST", "http://localhost:11434")
    llm = ChatOllama(model=model_name, temperature=0.3, host=model_host)
    response = llm.invoke(
        [
            SystemMessage(
                content=(
                    "You are a technical writer. "
                    "Format the provided research data into a well-structured Markdown report. "
                    "Use headings, bullet points, and sections. "
                    "Output ONLY the Markdown content, no preamble."
                    "The report will be componsed of multiple sections, each with a header and content. The sections are: "
                    "1. Overview: A brief summary of the topic. "
                    "2. Key Findings: Bullet points of the most important information discovered. "
                    "3. Analysis: A deeper dive into the implications of each of the findings, including any trade-offs or critical insights and a detailed analysis. "
                    "4. Risks and Uncertainties: Highlight any potential risks, uncertainties, or areas where information was lacking. "
                    "5. Areas for additional research: Suggestions for areas that require further investigation, additional or alternative approaches, or unanswered questions. "
                )
            ),
            HumanMessage(
                content=f"Format the following research into a Markdown report:\n\n{state['research_data']}"
            ),
        ]
    )
    # Handle case where response.content is a list
    content = response.content
    if isinstance(content, list):
        content = "\n".join(content)
    
    # Deterministic file write via artifact tool
    subfolder = f"{state['run_id']}"
    if state['parent_run_id']:
        subfolder = f"{state['parent_run_id']}/{subfolder}"
    path = write_markdown_artifact.invoke(
        {"filename": "report.md", "content": content, "subfolder": subfolder}
    )
    artifact = {
        "file_path": path,
        "description": f"Research report: {state['query']}",
        "agent_source": "researcher_writer",
    }
    return {"artifacts": [artifact]}


def build_researcher_graph():
    """Builds and compiles the Researcher agent graph -> Writer graph."""
    workflow = StateGraph(ResearcherAgentState)
    workflow.add_node("researcher", research_node)
    workflow.add_node("writer", writer_node)

    workflow.set_entry_point("researcher")
    workflow.add_edge("researcher", "writer")
    workflow.add_edge("writer", END)

    return workflow.compile()
