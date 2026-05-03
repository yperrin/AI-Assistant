---
complexity: Advanced
date: 2026-03-25 22:03:00-04:00
id: 32f9fa3b-8750-80da-b045-cd35723ad90f
processed_by_ai: true
summary: Dex Horthy from HumanLayer introduces the R.P.I. (Research, Plan, Implement)
  framework to effectively use AI agents in complex, production-grade codebases, addressing
  issues like "context pollution" and "vibe coding" through intentional context compaction
  and detailed planning. The framework emphasizes treating context as a scarce resource
  and ensuring human oversight on the plan before mechanical implementation.
title: No Vibes Allowed Solving Hard Problems in Complex Codebases
tools_mentioned:
- grep
- list-files
topics:
- AI Agents
- Software Development
- Context Management
- Codebase Management
- Software Architecture
- Development Workflow
- Problem Solving
url: https://www.notion.so/No-Vibes-Allowed-Solving-Hard-Problems-in-Complex-Codebases-32f9fa3b875080dab045cd35723ad90f
---

This video features **Dex Horthy** from **HumanLayer** discussing how to move beyond "vibe coding" (relying on intuition and AI magic) to solve hard problems in complex, production-grade codebases.

### The Problem: The "Dumb Zone"

Horthy identifies **Context Pollution** as the primary reason AI agents fail in large repos. As a chat history fills with noisy logs, wandering exploration, and corrections, the model enters a "Dumb Zone" where it starts producing "slop" instead of useful code.

### The Solution: The R.P.I. Framework

To maintain high-quality output, he proposes a structured loop designed to treat context as a scarce resource:

- **RESEARCH (Compress Truth):** Use the agent to scan files and establish ground truth. Trust the code, not the documentation.

- **PLAN (Compress Intent):** This is the most critical step. The agent must write a detailed, step-by-step plan. You review and approve the **plan**, not just the final code, to ensure you haven't "outsourced your thinking."

- **IMPLEMENT (Execute Mechanically):** Execute the approved plan, ideally in a **fresh context window** to keep the model in its "smart zone."

### Key Takeaway: "Intentional Compaction"

Instead of letting one chat run forever, frequently ask the agent to summarize the current state and "compact" the context. Start a **new chat** with that summary to keep the model sharp and focused on the next task.

You can watch the full presentation here: **[No Vibes Allowed: Solving Hard Problems in Complex Codebases](https://www.youtube.com/watch?v=rmvDxxNubIg)**.

In his presentation, **[No Vibes Allowed: Solving Hard Problems in Complex Codebases](https://www.youtube.com/watch?v=rmvDxxNubIg)**, Dex Horthy identifies that the primary failure of AI agents isn't a lack of "intelligence," but rather a failure of **Process and Context Management**.

Here is a detailed breakdown of the challenges he encountered and the specific strategies used to address them:

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

**Would you like me to create a checklist or a "Definition of Done" that you can provide to your teams to ensure they are following this Research-Plan-Implement (RPI) framework?**

---