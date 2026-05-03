---
complexity: Intermediate
date: 2025-12-16 20:04:00-05:00
id: 2cc9fa3b-8750-80e5-9486-d2e045569486
processed_by_ai: true
summary: This document details several new features within GitHub Copilot's Agent
  Mode, including the "Todo List" for structured task management, Concurrent Background
  Agents for parallel processing, and advanced editing capabilities like Copilot Edits
  and Next Edit Suggestions. These features aim to enhance developer productivity
  by streamlining workflows and leveraging AI for more intelligent code assistance.
title: GitHub Copilot new features
tools_mentioned:
- GitHub Copilot
- VS Code
- Git Worktrees
topics:
- AI Agents
- Developer Tools
- Task Management
- Parallel Processing
- Code Editing
- Predictive Coding
url: https://www.notion.so/GitHub-Copilot-new-features-2cc9fa3b875080e59486d2e045569486
---

# **Orchestrating Complexity: The "Todo List" Feature in Agent Mode**

The **Todo List** feature, integrated into GitHub Copilot’s Agent Mode, addresses this by introducing a structured, stateful layer to the interaction. It transforms the chat from a stream of consciousness into a managed project plan.
While **Plan Mode** and the **Todo List** might seem like they do the same thing (managing tasks), they serve two different phases of the engineering workflow: **Architecture** vs. **Execution**.

Think of **Plan Mode** as the "Architect" and the **Todo List** as the "Project Manager."

<br/>

# **Parallel Processing: Concurrent Agent Runs on a Single Project**

As AI agents become more capable, the primary bottleneck shifts from *capability* to *latency*. Waiting 60 seconds for an agent to generate a unit test suite is 60 seconds of lost developer time. To address this, VS Code has introduced the ability to run **Concurrent Background Agents**. This allows a developer to dispatch autonomous tasks to background processes while continuing to work interactively in the main editor.

The user explicitly asked "when and how" to use this. The answer lies in understanding the mechanism of **Isolation** via **Git Worktrees**.

Use the new Chat option to select ‘Background Agent’.

<br/>

# **The Evolution of Editing: Copilot Edits and Next Edit Suggestions**

## **Copilot Edits: The "Working Set" Paradigm**

It is vital to distinguish **Copilot Chat** from **Copilot Edits**.

- **Chat** is conversational. You ask a question; it gives an answer. You copy the code.

- **Edits** is transactional. You define a scope; it applies changes.

**The Working Set:** In "Copilot Edits" mode (accessible via `Ctrl+Shift+I` or the dedicated view), you explicitly add files to a **Working Set**. This tells the AI: "These are the only files you should look at, and these are the files you are allowed to touch."

<br/>

## **Next Edit Suggestions (NES): Predictive Coding**

**NES** represents the next generation of "Ghost Text." Traditional ghost text completes the line you are typing. NES predicts the *next* edit you need to make, often in a different part of the file.

**Mechanism:** If you change a function signature from `function add(a, b)` to `function add(a, b, c)`, NES anticipates that you will need to update the function body to use `c`.

<br/>