---
title: How to write a good direct for AI Agents
id: 30e9fa3b-8750-80e2-84cb-d88450f690c4
url: https://www.notion.so/How-to-write-a-good-direct-for-AI-Agents-30e9fa3b875080e284cbd88450f690c4
---

### 5 Principles for AI Agent Specs

1. **High-Level Vision First:** Start with a concise goal and let the AI draft the detailed [SPEC.md](https://www.oreilly.com/radar/how-to-write-a-good-spec-for-ai-agents/). This leverages the AI's strength in elaboration while you maintain control of the vision.

1. **Professional PRD Structure:** Treat the spec like a system design document. Effective specs should explicitly cover:

	- **Commands:** Full executable commands (e.g., npm test).

	- **Testing:** Frameworks and coverage expectations.

	- **Project Structure:** Explicit paths for source, tests, and docs.

	- **Code Style:** One code snippet is worth "three paragraphs of description."

	- **Git Workflow:** Branching and commit conventions.

	- **Boundaries:** Clear "never touch" zones (e.g., secrets, CI configs).

1. **Manage the "Attention Budget":** Use hierarchical summaries or [RAG (Retrieval-Augmented Generation)](https://www.oreilly.com/radar/how-to-write-a-good-spec-for-ai-agents/) for large projects. Don't dump 50 pages of docs; surface only what is relevant to the current task.

1. **Spec-Driven Development:** Integrate specs into a gated workflow:

	- **Specify** (User journeys) → **Plan** (Architecture/Stack) → **Tasks** (Small, reviewable chunks) → **Implement** (Atomic code changes).

1. **Iterative Refinement:** The spec is a "living, executable artifact." Use tools like **Plan Mode** (read-only analysis) to refine the plan before allowing the agent to write any code.

### Key Takeaways for Senior Leadership

- **Vibe Coding vs. AI-Assisted Engineering:** While "vibe coding" is great for prototyping, production-grade systems require the discipline of rigorous specs and human-in-the-loop validation.

- **The "Lethal Trifecta":** Avoid the combination of vague prompts, overlong contexts, and skipping human review, which leads to "house of cards" code—fragile outputs that collapse under edge cases.

- **Single Source of Truth:** A well-maintained spec acts as the management tool for your "army of AI interns," ensuring [long-term architectural health](https://www.oreilly.com/radar/how-to-write-a-good-spec-for-ai-agents/) and team-wide clarity.

<br/>

