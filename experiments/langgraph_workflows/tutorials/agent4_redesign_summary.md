# LangGraph Design Summary: State Management over Global Variables

## 1. The Problem with Global Variables
In the initial implementation, `document_content` was declared as a global variable. This creates several critical issues:
- **Concurrency:** If multiple users interact with the agent simultaneously, they share the same global variable, causing data corruption.
- **Persistence:** LangGraph’s checkpointing (saving a conversation to a database) cannot track data held in global variables.
- **Unit Testing:** Tests become interdependent because global state persists across different test executions.

## 2. The Final Design: State-Driven Architecture
The improved design utilizes LangGraph's native state management and **Dependency Injection** via `InjectedState`.

### Key Benefits
1. **Thread Safety:** Every conversation has its own isolated instance of `document_content`.
2. **Persistence Support:** If a checkpointer is added, the document content is saved and restored automatically alongside the chat history.
3. **Traceability:** State changes are explicit in the graph's execution path, making debugging significantly easier.

## 3. Full Implementation

```python
from typing import Annotated, Sequence, TypedDict
from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage, ToolMessage
from langchain_core.tools import tool, InjectedState
from langchain_ollama import ChatOllama
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode

# 1. Define the State with all necessary properties
class State(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    document_content: str 

# 2. Tools using dependency injection where needed
@tool
def update(content: str) -> str:
    """ Update function which updates the document content with the provided content """
    # We return the content which will be synced to state by a node
    return content

@tool
def save(filename: str, state: Annotated[dict, InjectedState]) -> str:
    """ Save function which saves the current document content to a file 
        Args:
            filename (str): The name of the markdown file to save the document content to
    """
    # InjectedState provides access to the current graph state
    content = state.get("document_content", "")
    try:
        with open(filename, "w") as f:
            f.write(content)
        return f"Document content saved to {filename}"
    except Exception as e:
        return f"Failed to save document content: {e}"

tools = [update, save]    
ollama = ChatOllama(model="llama3.1:8b", host="http://localhost:11434").bind_tools(tools)

# 3. Nodes and Logic
def chat_node(state: State) -> State:
    # Read content from state instead of global
    doc_content = state.get("document_content", "")
    
    system_message = SystemMessage(content=f"""
        You are a Drafter, a helpful writing assistant. 
        You are going to help the user draft a document. 
        You have access to tools to update and save.
                                   
        The current document content is: {doc_content}
    """)

    user_input = input("what would you like to do? (update/save): ")
    user_message = HumanMessage(content=user_input)

    chatbot_messages = [system_message] + state["messages"] + [user_message]
    response = ollama.invoke(chatbot_messages)
    
    return { "messages": [user_message, response] }

def sync_state(state: State) -> State:
    """ Post-tool node that updates the state based on tool results """
    if not state["messages"]:
        return {}
        
    last_message = state["messages"][-1]
    
    # If the last tool called was 'update', sync its output to document_content
    if isinstance(last_message, ToolMessage) and last_message.name == "update":
        return {"document_content": last_message.content}
    
    return {}

def should_continue(state: State) -> str:
    messages = state["messages"]
    if not messages:
        return "continue"
    for message in reversed(messages):
        if (isinstance(message, ToolMessage) and 
            "saved" in message.content.lower() and
            "document" in message.content.lower()):
            return "end"
    return "continue"

# 4. Graph Construction
graph = StateGraph(State)
graph.add_node("chatbot", chat_node)
graph.add_node("tools", ToolNode(tools=tools))
graph.add_node("sync", sync_state)

graph.add_edge(START, "chatbot")
graph.add_edge("chatbot", "tools")
graph.add_edge("tools", "sync")

graph.add_conditional_edges(
    "sync", 
    should_continue, 
    {
        "continue": "chatbot", 
        "end": END
    }
)

workflow = graph.compile()
```
