from typing import Annotated, TypedDict

from langchain_ollama import ChatOllama
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages


# Define the state schema
class State(TypedDict):
    # 'add_messages' ensures new messages are appended to the list, not overwritten
    messages: Annotated[list, add_messages]

# Initialize the model (Assumes Ollama is running locally)
llm = ChatOllama(model="llama3.1:8b", temperature=0, host="http://localhost:11434")

def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}

# Build the graph
workflow = StateGraph(State)
workflow.add_node("chatbot", chatbot)
workflow.add_edge(START, "chatbot")
workflow.add_edge("chatbot", END)

# Compile the graph
agent = workflow.compile()

if __name__ == "__main__":
    # Test run
    input_state = {"messages": [("user", "Explain why 'uv' is better than 'pip' in two sentences.")]}
    for event in agent.stream(input_state):
        for value in event.values():
            print(value["messages"][-1].content)