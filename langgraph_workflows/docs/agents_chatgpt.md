Below is a **LangGraph-native architecture plan** for your multi-agent system with Planner → Researcher → Critic → Implementer.
I’ll focus on:

* Graph topology (how agents coordinate)
* State design (most important part)
* Routing logic
* Minimal but realistic code skeletons
* Extension patterns (tree research, MAPS debate, safe execution)

This is designed so you can **implement incrementally** without building everything at once.

---

# 1) High-Level Architecture

### Workflow

```
User Query
    ↓
Planner (Supervisor)
    ↓ (route)
Researcher  → Critic → Planner
Implementer → Critic → Planner
Debate Loop (Critic personas)
    ↓
Final Synthesizer (Planner)
```

### Responsibilities

| Agent       | Responsibility               |
| ----------- | ---------------------------- |
| Planner     | Task decomposition + routing |
| Researcher  | Tree-style web research      |
| Critic      | MAPS debate + reflection     |
| Implementer | Code generation + execution  |

---

# 2) LangGraph State Design (Critical)

LangGraph works best when state is explicit.

```python
from typing import TypedDict, List, Dict, Optional

class AgentState(TypedDict):
    user_query: str
    plan: Optional[str]
    sub_tasks: List[str]
    current_task: Optional[str]
    research_results: List[Dict]
    code: Optional[str]
    execution_output: Optional[str]
    critiques: List[str]
    final_answer: Optional[str]
    next_agent: Optional[str]
```

Key ideas:

* Planner writes `plan`, `sub_tasks`, `next_agent`
* Researcher appends to `research_results`
* Critic appends to `critiques`
* Implementer writes `code` + `execution_output`

---

# 3) Model Setup

```python
from langchain_openai import ChatOpenAI

planner_llm = ChatOpenAI(model="gpt-4o-mini")
research_llm = ChatOpenAI(model="gpt-4o-mini")
critic_llm = ChatOpenAI(model="gpt-4o-mini")
coder_llm = ChatOpenAI(model="gpt-4o-mini")  # replace with coder model if available
```

---

# 4) Planner Node (Supervisor)

### Function

* Break query into tasks
* Decide route

```python
def planner_node(state: AgentState):
    prompt = f"""
User goal: {state['user_query']}

Create:
1) A plan
2) Subtasks
3) Decide next agent:
   - research
   - implement
   - finish

Respond as JSON.
"""

    response = planner_llm.invoke(prompt).content

    # Assume parsed JSON
    data = json.loads(response)

    return {
        "plan": data["plan"],
        "sub_tasks": data["subtasks"],
        "current_task": data["subtasks"][0] if data["subtasks"] else None,
        "next_agent": data["next_agent"]
    }
```

---

# 5) Researcher Node (Tree-Like Exploration)

### Tool: Tavily

```python
from langchain_community.tools.tavily_search import TavilySearchResults

search_tool = TavilySearchResults(k=5)
```

### Tree Logic

Each research iteration:

1. Search
2. Summarize
3. Generate follow-up questions

```python
def researcher_node(state: AgentState):
    task = state["current_task"]

    results = search_tool.invoke(task)

    summary_prompt = f"""
Summarize the key findings for:
{task}

Also generate 2 follow-up research questions.
"""

    summary = research_llm.invoke(summary_prompt).content

    state["research_results"].append({
        "task": task,
        "results": results,
        "summary": summary
    })

    return {
        "research_results": state["research_results"],
        "next_agent": "critic"
    }
```

To make it truly tree-like later:

* Push follow-up questions into `sub_tasks`

---

# 6) Critic Node (MAPS Debate)

We create **two personas**.

```python
optimist_prompt = """
You are an Optimist expert.
Highlight strengths, feasibility, and opportunities.
"""

pessimist_prompt = """
You are a Pessimist expert.
Identify risks, flaws, missing info, and hallucinations.
"""
```

```python
def critic_node(state: AgentState):
    content = f"""
Plan: {state.get('plan')}
Research: {state.get('research_results')}
Code: {state.get('code')}
"""

    opt = critic_llm.invoke(optimist_prompt + content).content
    pes = critic_llm.invoke(pessimist_prompt + content).content

    critique = f"Optimist:\n{opt}\n\nPessimist:\n{pes}"
    state["critiques"].append(critique)

    return {
        "critiques": state["critiques"],
        "next_agent": "planner"
    }
```

This creates a **reflection loop**.

---

# 7) Implementer Node (Code + Execution)

### Safe execution example

```python
import subprocess
import tempfile

def run_code(code: str):
    with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as f:
        f.write(code.encode())
        path = f.name

    result = subprocess.run(
        ["python", path],
        capture_output=True,
        text=True,
        timeout=10
    )

    return result.stdout + result.stderr
```

### Node

```python
def implementer_node(state: AgentState):
    task = state["current_task"]

    prompt = f"""
Write Python code for:
{task}

Return only code.
"""

    code = coder_llm.invoke(prompt).content
    output = run_code(code)

    return {
        "code": code,
        "execution_output": output,
        "next_agent": "critic"
    }
```

Replace with E2B/Docker later.

---

# 8) Routing Logic

LangGraph conditional edges:

```python
def router(state: AgentState):
    return state["next_agent"]
```

---

# 9) Build the Graph

```python
from langgraph.graph import StateGraph, END

graph = StateGraph(AgentState)

graph.add_node("planner", planner_node)
graph.add_node("research", researcher_node)
graph.add_node("critic", critic_node)
graph.add_node("implement", implementer_node)

graph.set_entry_point("planner")

graph.add_conditional_edges(
    "planner",
    router,
    {
        "research": "research",
        "implement": "implement",
        "finish": END
    }
)

graph.add_edge("research", "critic")
graph.add_edge("implement", "critic")
graph.add_edge("critic", "planner")

app = graph.compile()
```

---

# 10) Run It

```python
result = app.invoke({
    "user_query": "Build a stock price analysis tool",
    "research_results": [],
    "critiques": [],
    "sub_tasks": []
})

print(result["final_answer"])
```

---

# 11) Recommended Build Phases

### Phase 1 (MVP)

* Planner
* Researcher
* Critic loop

### Phase 2

* Tree research (add follow-up tasks)

### Phase 3

* Implementer + sandbox

### Phase 4 (Advanced)

* Memory (vector DB)
* Parallel MAPS debate
* Tool selection agent

---

# 12) Advanced Enhancements (Agentic Patterns)

## A. True Tree Research

Planner pushes:

```python
state["sub_tasks"].extend(followups)
```

## B. Parallel Debate

Use:

```python
graph.add_node("optimist", optimist_node)
graph.add_node("pessimist", pessimist_node)
graph.add_edge("optimist", "critic_merge")
graph.add_edge("pessimist", "critic_merge")
```

## C. Confidence-Based Stop

Critic returns:

```
confidence: 0-1
```

Planner finishes if `> 0.85`.

---

# 13) Final Architecture Summary

This design gives you:

* Supervisor orchestration
* Recursive research
* Multi-persona reflection (MAPS)
* Safe execution
* Iterative refinement loop

This is very close to architectures used in:

* GPT-Researcher
* Devin-like systems
* Enterprise agent platforms

---

# 14) If you want to go further

I can provide:

* A **production-ready folder structure**
* **Parallel multi-agent LangGraph**
* **Memory + vector DB integration**
* A **Devin-style autonomous engineer architecture**

Just ask:

> “Design this as a production-grade autonomous system”

and I’ll take this to the next level.
