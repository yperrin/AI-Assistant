---
title: Agent Harnesses and vibe coding
id: 2d09fa3b-8750-806a-9d80-db228bc9cc1c
url: https://www.notion.so/Agent-Harnesses-and-vibe-coding-2d09fa3b8750806a9d80db228bc9cc1c
---

### The Evolution of AI Interaction

- **Prompt Engineering (2020):** Optimizing single interactions with an LLM.

- **Context Engineering (Recent):** Managing entire sessions or context windows to provide the right data at the right time.

- **Agent Harnesses (Current/Future):** Connecting multiple context windows and specialized agents to handle complex, end-to-end tasks with checkpoints and human-in-the-loop validation.

### Key Components of a Harness

- **Initializer Agents:** Set the stage by creating feature lists, project specs (PRDs), and scaffolding the environment.

- **Persistent Memory:** Utilizing **Git logs**, **file systems**, and dedicated "progress files" to ensure context is handed off correctly between sessions without "memory loss".

- **Guardrails & Validation:** Automating testing and regression checks between steps to ensure the agent hasn't gone "off the rails".

### The Two Major Roadblocks

1. **Bounded Attention:** LLMs still suffer from "context rot" or the "dumb zone" when overwhelmed. Current summarization for handoffs often misses critical details.

1. **Compounding Errors:** A 95% reliable agent drops to ~36% reliability over 20 steps. For true "vibe coding," systems need near 99.9% reliability, which is only achievable through strategic human-in-the-loop checkpoints.

