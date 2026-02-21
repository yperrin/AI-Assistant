from typing import Annotated, TypedDict

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages


# Define the state schema
class State(TypedDict):
    # 'add_messages' ensures new messages are appended to the list, not overwritten
    messages: Annotated[list, add_messages]

# Initialize the model (Assumes Ollama is running locally)
llm = ChatOllama(model="llama3.1:8b", temperature=0, host="http://localhost:11434")

def chatbot(state: State):
    """ 
        A simple chatbot function that takes the current state (messages) 
        and returns a new state with the model's response appended.
    """
    return {"messages": [llm.invoke(state["messages"])]}

def greeter(state: State):
    """ 
        A simple greeter function that takes the current state (messages) 
        and returns a new state hello added.
    """
    message: HumanMessage = state["messages"][0]
    return {"messages": [HumanMessage(content="hello: " + message.content)]}


# Build the graph
graph = StateGraph(State)
graph.add_node("chatbot", chatbot)
graph.add_node("greeter", greeter)
graph.set_entry_point("chatbot")
graph.set_finish_point("chatbot")

# Compile the graph
agent = graph.compile()

if __name__ == "__main__":
    # Test run
    input_state = {"messages": [
        SystemMessage("You are very opiniated and you don't like 'uv'"), 
        HumanMessage("Explain why 'uv' is better than 'pip' in two sentences.")
    ]}
    for event in agent.stream(input_state):
        for value in event.values():
            print(value["messages"][-1].content)

# 
# Example of Event
# {'chatbot': {'messages': [AIMessage(content='I\'m happy to provide a neutral explanation! However, I must note that both "uv" and "pip" are package managers for Python, and which one is "better" ultimately depends on personal preference and specific use cases.\n\nThat being said, here\'s a brief comparison: "uv" (or more specifically, "poetry" which uses the "uv" resolver) is often preferred by developers who value flexibility and customization in their dependency management, as it allows for more fine-grained control over package dependencies. On the other hand, "pip" is generally easier to use and more widely adopted, making it a good choice for simple projects or those with straightforward dependency requirements.', additional_kwargs={}, response_metadata={'model': 'llama3.1:8b', 'created_at': '2026-02-19T02:07:24.532607148Z', 'done': True, 'done_reason': 'stop', 'total_duration': 88370712096, 'load_duration': 66242881674, 'prompt_eval_count': 26, 'prompt_eval_duration': 1576735541, 'eval_count': 138, 'eval_duration': 20549500366, 'logprobs': None, 'model_name': 'llama3.1:8b', 'model_provider': 'ollama'}, id='lc_run--019c73a5-9041-7d73-a04b-787ba353a543-0', tool_calls=[], invalid_tool_calls=[], usage_metadata={'input_tokens': 26, 'output_tokens': 138, 'total_tokens': 164})]}}
#