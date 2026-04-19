---
complexity: Advanced
date: 2026-03-22 15:45:00-04:00
id: 32b9fa3b-8750-80f6-866a-de4b48989641
processed_by_ai: true
summary: This document addresses the challenge of compounding failures in multi-step
  AI agentic workflows, proposing "Harness Engineering" as a solution to build highly
  reliable agents. It outlines key components like specialized state machines, virtual
  file systems, sub-agent delegation, and validation loops to achieve professional-grade
  reliability.
title: Andrej Karpathys Math Proves Agent Skills Will Fail. Heres What to Build Instead.
tools_mentioned:
- Gemini Flash
- Gemini Pro
- Supabase
topics:
- AI Agents
- Agentic Workflows
- LLM Reliability
- Harness Engineering
- State Machines
- Virtual File Systems
- Sub-Agent Delegation
- Validation Loops
- Context Management
- AI Architecture
url: https://www.notion.so/Andrej-Karpathy-s-Math-Proves-Agent-Skills-Will-Fail-Here-s-What-to-Build-Instead-32b9fa3b875080f6866ade4b48989641
---

### The Problem: The "March of Nines"

- **Compounding Failure:** In a 10-step agentic workflow, a **90% success rate** per step leads to over **6 failures a day** if run 10 times. To reach professional standards, you need 99.9% reliability per step [00:52 Opens in a new window ](http://www.youtube.com/watch?v=I2K81s0OQto&t=52).

- **Skills vs. Harnesses:** Skills are essentially just prompts. While they improve performance, they lack the "deterministic rails" needed to prevent hallucinations or skipped steps [02:27 Opens in a new window ](http://www.youtube.com/watch?v=I2K81s0OQto&t=147).

---

### The Solution: Harness Engineering

### Key Components of an Effective Harness:

- **Specialized State Machines:** Using fixed or dynamic plans to keep long-running agents on track [12:00 Opens in a new window ](http://www.youtube.com/watch?v=I2K81s0OQto&t=720).

- **Virtual File Systems:** Providing a "scratch pad" (workspace) for agents to read/write files, ensuring resilience if a process needs to restart [13:02 Opens in a new window ](http://www.youtube.com/watch?v=I2K81s0OQto&t=782).

- **Sub-Agent Delegation:** Isolating context by spinning up dedicated LLMs for specific tasks. This prevents "context rot" and allows the use of cheaper, faster models (like **Gemini Flash**) for narrow tasks while keeping a more capable model (like **Gemini Pro**) as the supervisor [13:34 Opens in a new window ](http://www.youtube.com/watch?v=I2K81s0OQto&t=814).

- **Validation Loops:** Programmatically testing outputs (e.g., running code tests or fact-checking against a playbook) and forcing the AI to iterate until it passes [18:20 Opens in a new window ](http://www.youtube.com/watch?v=I2K81s0OQto&t=1100).

### Real-World Demo: Contract Review Harness

1. **Human-in-the-Loop:** Asks the user clarifying questions before starting [06:03 Opens in a new window ](http://www.youtube.com/watch?v=I2K81s0OQto&t=363).

1. **Parallel Processing:** Triggers dozens of sub-agents in parallel to analyze individual clauses, burning over **323,000 tokens** for a deep analysis that would otherwise "rot" a single context window [08:52 Opens in a new window ](http://www.youtube.com/watch?v=I2K81s0OQto&t=532).

1. **Programmatic Output:** Generates a Word document via a fixed template rather than letting the LLM hallucinate the formatting [08:15 Opens in a new window ](http://www.youtube.com/watch?v=I2K81s0OQto&t=495).

---

### 12 Essentials for Designing Harnesses [11:11 Opens in a new window](http://www.youtube.com/watch?v=I2K81s0OQto&t=671)

 | **Feature** | **Description** | 
 | ---- | ---- | 
 | **Architecture** | Choosing between Hierarchical, DAG, or Autonomous swarms. | 
 | **Planning** | Using fixed (deterministic) or dynamic to-do lists. | 
 | **File System** | Managing a workspace for persistent data. | 
 | **Delegation** | Isolating context and using multi-model strategies. | 
 | **Parallelism** | Running non-dependent tasks simultaneously to save time. | 
 | **Guardrails** | Implementing access controls and human approval steps. | 
 | **Memory** | Managing short-term (markdown) and long-term (knowledge graph) data. | 
 | **State Tracking** | Using databases (like **Supabase**) to monitor progress [16:04 Opens in a new window ](http://www.youtube.com/watch?v=I2K81s0OQto&t=964). | 
 | **Code Execution** | Utilizing secure sandboxes for tool calling. | 
 | **Context Mgmt** | Compacting or summarizing to keep the supervisor lean. | 
 | **Human Loop** | Strategic touchpoints for guidance or approval. | 
 | **Validation** | Iterative loops to guarantee high-quality results. |