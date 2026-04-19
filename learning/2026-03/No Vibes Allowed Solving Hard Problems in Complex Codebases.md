---
complexity: Advanced
date: 2026-03-25 22:03:00-04:00
id: 32f9fa3b-8750-80da-b045-cd35723ad90f
processed_by_ai: true
summary: This document outlines common challenges when using AI agents for software
  development, such as context pollution and outsourced thinking, and proposes the
  R.P.I. (Research, Plan, Implement) framework and other strategies like "Intentional
  Compaction" to improve agent effectiveness and code quality.
title: No Vibes Allowed Solving Hard Problems in Complex Codebases
tools_mentioned:
- grep
- list-files
topics:
- AI Agents
- Software Development
- Prompt Engineering
- Context Management
- Code Quality
- Software Architecture
url: https://www.notion.so/No-Vibes-Allowed-Solving-Hard-Problems-in-Complex-Codebases-32f9fa3b875080dab045cd35723ad90f
---

### The Problem: The "Dumb Zone"

### The Solution: The R.P.I. Framework

- **RESEARCH (Compress Truth):** Use the agent to scan files and establish ground truth. Trust the code, not the documentation.

- **PLAN (Compress Intent):** This is the most critical step. The agent must write a detailed, step-by-step plan. You review and approve the **plan**, not just the final code, to ensure you haven't "outsourced your thinking."

- **IMPLEMENT (Execute Mechanically):** Execute the approved plan, ideally in a **fresh context window** to keep the model in its "smart zone."

### Key Takeaway: "Intentional Compaction"

---

### 1. The "Dumb Zone" (Context Pollution)

- **The Challenge:** As an AI chat progresses, it becomes filled with "contextual noise"—exploration logs, failed attempts, and minor corrections. Eventually, the model reaches a saturation point where it stops following logic and starts producing "slop" or repetitive, hallucinated code.

- **The Address:** **Intentional Compaction.** Horthy suggests that developers must treat context as a scarce resource. Instead of one long thread, you should frequently ask the agent to "summarize the current state and next steps," then **start a brand new chat** using that summary as the starting point. This resets the "Dumb Zone" and keeps the model in its "Smart Zone."

### 2. The "Vibe Coding" Trap (Outsourced Thinking)

- **The Challenge:** Developers often prompt an agent with a high-level goal and immediately ask for code. This leads to the "vibe" approach where the human just checks if the code *looks* right, rather than if the logic is sound. This results in brittle codebases that juniors ship and seniors have to fix.

- **The Address:** **Compression of Intent (The Plan Phase).** Before any code is written, the agent must produce a **[code snippet plan](https://www.google.com/search?q=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DrmvDxxNubIg%26t%3D933s)**. This plan lists the specific files to be changed and the logic to be applied in pseudo-code. The human reviews and approves the *plan* first, ensuring the architectural intent is correct before the mechanical implementation begins.

### 3. Misalignment with "Ground Truth"

- **The Challenge:** Documentation in large, brownfield codebases is often outdated. If an agent relies on a README or a high-level summary, it will produce code that doesn't actually work with the current implementation.

- **The Address:** **Compression of Truth (The Research Phase).** The agent is instructed to perform active research using tools like `grep` or `list-files` to find the actual implementation. Horthy's rule is: "Trust the code, not the docs." The agent must cite specific lines of existing code to prove it understands the environment before proposing a change.

### 4. Regression and "Slop" in PRs

- **The Challenge:** When agents attempt to implement large features at once, they often introduce regressions or "slop" (unnecessary or slightly incorrect code) because the task is too broad for the context window.

- **The Address:** **Mechanical Implementation.** By separating the "Thinking" (Planning) from the "Doing" (Implementation), the implementation phase becomes a mechanical exercise. You take the approved plan into a **fresh context** and ask the agent to execute only that specific plan. This isolation prevents the agent from getting distracted by the complexity of the wider problem.

### 5. Architectural Decay

- **The Challenge:** AI agents tend to follow the "path of least resistance," which can lead to tight coupling and messy abstractions if they aren't guided by a senior-level architecture.

- **The Address:** **Agent-Ready Codebase Patterns.** This involves flattening directory structures and using clear, explicit file headers. By making the architecture "legible" to a model with a limited context window, you reduce the "reasoning hop" required for the agent to make a correct decision.

---

---