Below is a **LangGraph-native debate architecture** designed specifically for your goal:

> Multiple agents debate → converge → output **1–2 best ideas** + **what was debated and why**

This design focuses on:

* Structured debate (not just chat)
* Strong personality diversity
* Convergence mechanism (critical)
* Clean LangGraph implementation

---

# 1) Recommended Debate Agent Set

You don’t want many agents.
**4–6 well-designed roles outperform large swarms.**

## Core Debate Agents

### 1) Ideator (Creator)

**Personality:** Creative, bold, opportunity-focused
**Role:** Generate initial solution ideas
**Bias:** Innovation over feasibility

---

### 2) Realist (Practical Engineer)

**Personality:** Pragmatic, execution-focused
**Role:** Evaluate feasibility, cost, timeline
**Bias:** “Can this actually be built?”

---

### 3) Skeptic (Risk Analyst)

**Personality:** Critical, risk-averse
**Role:** Identify failure modes, hidden risks, edge cases
**Bias:** Worst-case thinking

---

### 4) Optimizer (Strategist)

**Personality:** Efficiency-driven
**Role:** Improve ideas instead of rejecting them
**Bias:** Refinement over replacement

---

### 5) Judge (Decision Maker)

**Personality:** Neutral, structured
**Role:**

* Compare debated ideas
* Select **Top 1–2**
* Provide **debate summary**
* Explain **why chosen**

---

# Why this works

You get:

| Function        | Agent     |
| --------------- | --------- |
| Idea generation | Ideator   |
| Reality check   | Realist   |
| Risk control    | Skeptic   |
| Iteration       | Optimizer |
| Convergence     | Judge     |

This is a **MAPS-style structured debate**, not chaotic conversation.

---

# 2) Debate Workflow

```
User Goal
   ↓
Ideator → generates N ideas
   ↓
Realist evaluates
   ↓
Skeptic attacks
   ↓
Optimizer improves
   ↓
Judge selects Top 1–2
   ↓
Final Output:
- Winning ideas
- What was debated
- Key tradeoffs
```

Optional: loop Optimizer → Skeptic → Judge for multiple rounds.

---

# 3) LangGraph State Design

```python
from typing import TypedDict, List, Dict

class DebateState(TypedDict):
    user_goal: str
    ideas: List[Dict]
    evaluations: List[str]
    risks: List[str]
    improvements: List[str]
    debate_log: List[str]
    final_selection: List[Dict]
    next_agent: str
```

Each idea:

```python
{
    "title": "",
    "description": "",
    "score": {}
}
```

---

# 4) LLM Setup

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
```

---

# 5) Agent Prompts + Nodes

---

## 5.1 Ideator Node

```python
import json

def ideator_node(state: DebateState):
    prompt = f"""
Goal: {state['user_goal']}

Generate 3 distinct solution ideas.
Return JSON:
[
  {{ "title": "", "description": "" }}
]
"""

    response = llm.invoke(prompt).content
    ideas = json.loads(response)

    state["debate_log"].append("Ideator generated ideas.")

    return {
        "ideas": ideas,
        "next_agent": "realist"
    }
```

---

## 5.2 Realist Node

```python
def realist_node(state: DebateState):
    prompt = f"""
Evaluate feasibility, cost, and complexity.

Ideas:
{state['ideas']}

Be practical and concise.
"""

    evaluation = llm.invoke(prompt).content

    state["debate_log"].append("Realist evaluation:\n" + evaluation)

    return {
        "evaluations": state["evaluations"] + [evaluation],
        "next_agent": "skeptic"
    }
```

---

## 5.3 Skeptic Node

```python
def skeptic_node(state: DebateState):
    prompt = f"""
Identify risks, failure modes, and hidden assumptions.

Ideas:
{state['ideas']}
Evaluations:
{state['evaluations']}
"""

    risks = llm.invoke(prompt).content

    state["debate_log"].append("Skeptic risks:\n" + risks)

    return {
        "risks": state["risks"] + [risks],
        "next_agent": "optimizer"
    }
```

---

## 5.4 Optimizer Node

```python
def optimizer_node(state: DebateState):
    prompt = f"""
Improve the ideas based on risks and feasibility feedback.

Ideas:
{state['ideas']}
Risks:
{state['risks']}
Evaluations:
{state['evaluations']}

Return improved ideas as JSON list.
"""

    response = llm.invoke(prompt).content
    improved = json.loads(response)

    state["debate_log"].append("Optimizer refined ideas.")

    return {
        "ideas": improved,
        "next_agent": "judge"
    }
```

---

## 5.5 Judge Node (Convergence)

This is the most important node.

```python
def judge_node(state: DebateState):
    prompt = f"""
Select the BEST 1 or 2 ideas.

Provide:
- Selected ideas (JSON)
- Why they won
- Key tradeoffs debated

Ideas:
{state['ideas']}
Debate Log:
{state['debate_log']}
"""

    result = llm.invoke(prompt).content

    state["debate_log"].append("Judge decision.")

    return {
        "final_selection": result,
        "next_agent": "finish"
    }
```

---

# 6) Build the LangGraph

```python
from langgraph.graph import StateGraph, END

def router(state: DebateState):
    return state["next_agent"]

graph = StateGraph(DebateState)

graph.add_node("ideator", ideator_node)
graph.add_node("realist", realist_node)
graph.add_node("skeptic", skeptic_node)
graph.add_node("optimizer", optimizer_node)
graph.add_node("judge", judge_node)

graph.set_entry_point("ideator")

graph.add_conditional_edges(
    "ideator", router,
    {"realist": "realist"}
)

graph.add_conditional_edges(
    "realist", router,
    {"skeptic": "skeptic"}
)

graph.add_conditional_edges(
    "skeptic", router,
    {"optimizer": "optimizer"}
)

graph.add_conditional_edges(
    "optimizer", router,
    {"judge": "judge"}
)

graph.add_conditional_edges(
    "judge", router,
    {"finish": END}
)

app = graph.compile()
```

---

# 7) Run Example

```python
result = app.invoke({
    "user_goal": "Create a profitable AI SaaS for small businesses",
    "ideas": [],
    "evaluations": [],
    "risks": [],
    "improvements": [],
    "debate_log": [],
    "final_selection": [],
    "next_agent": "ideator"
})

print(result["final_selection"])
```

---

# 8) Optional Enhancements (Recommended)

### A. Multi-round debate

Add loop:

```
Judge → if confidence < 0.8 → Optimizer
```

---

### B. Parallel Critics

Run Realist + Skeptic in parallel for speed.

---

### C. Scoring System

Judge returns:

```
{
  idea: score (impact, feasibility, risk)
}
```

---

# 9) Final Architecture Summary

This design gives you:

* Structured debate (not chat chaos)
* Personality diversity
* Risk control
* Iterative improvement
* Convergence to **Top 1–2 ideas**
* Full **debate trace**

This is similar to:

* AI Venture Studio architectures
* Strategy co-pilot systems
* Decision intelligence agents

---

If you want the **next level**, I can design:

* A **self-looping autonomous debate system**
* **Parallel multi-agent voting**
* A **production-grade architecture (memory + persistence)**
* A **Devin-style strategic decision engine**

Just ask:

> “Make this a production-grade LangGraph debate system”
