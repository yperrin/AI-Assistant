---
complexity: Intermediate
date: 2026-03-22 15:47:00-04:00
id: 32b9fa3b-8750-80db-95f8-f11b27d865a7
processed_by_ai: true
summary: This article outlines a framework for creating effective specifications,
  called "Smart Specs," to guide AI coding agents without exceeding their context
  limits, emphasizing an iterative, spec-driven development approach.
title: How to Write a Good Spec for AI Agents
tools_mentioned:
- Claude Code
- Gemini CLI
- npm
- Git
topics:
- AI Agents
- Specification Writing
- Software Development
- Prompt Engineering
- Spec-Driven Development
url: https://www.notion.so/How-to-Write-a-Good-Spec-for-AI-Agents-32b9fa3b875080db95f8f11b27d865a7
---

The article "[How to Write a Good Spec for AI Agents](https://www.oreilly.com/radar)" by Addy Osmani provides a framework for creating specifications that guide AI coding agents (like Claude Code or Gemini CLI) without overwhelming their context limits.

### **The Core Strategy**

Instead of one massive "RFC-style" document, use **Smart Specs**: living artifacts that focus on the "what" and "why," allowing the AI to flesh out the "how" through a gated, iterative process.

---

### **5 Key Principles**

1. **Vision First, Details Later:** Start with a high-level "product brief." Use **Plan Mode** (read-only) to let the AI draft a detailed `spec.md` before writing any code.

1. **Professional Structure:** Organize your spec like a PRD. A successful spec must cover **six core areas**:

	- **Commands:** (e.g., `npm test`, `build`)

	- **Testing:** Frameworks and coverage expectations.

	- **Project Structure:** Where files live.

	- **Code Style:** Naming conventions and snippets.

	- **Git Workflow:** Branching and commit formats.

	- **Boundaries:** What the AI is **forbidden** to touch (e.g., secrets, CI configs).

1. **Modular Context:** Avoid the "curse of instructions" (where AI ignores rules in long prompts). Break tasks into small, focused prompts and use **Subagents** or specialized "Skills" for different domains (Backend vs. Frontend).

1. **Three-Tier Boundaries:** Use a clear traffic-light system for agent autonomy:

	- ✅ **Always do:** (e.g., Run linting)

	- ⚠️ **Ask first:** (e.g., Schema changes)

	- 🚫 **Never do:** (e.g., Commit API keys)

1. **Iterative Evolution:** Treat the spec as code. Update it as the project evolves, use **LLM-as-a-Judge** for subjective reviews, and maintain a robust test suite to provide the agent with immediate feedback loops.

### **The Bottom Line**

Effective AI engineering is moving away from "vibe coding" toward **Spec-Driven Development**. You act as the "Executive in the Loop," providing the roadmap and quality gates while the AI handles the bulk of the implementation.

Would you like me to help you draft a high-level vision for a specific project based on this framework?