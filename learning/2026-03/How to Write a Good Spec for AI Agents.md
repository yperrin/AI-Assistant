---
complexity: Advanced
date: 2026-03-22 15:47:00-04:00
id: 32b9fa3b-8750-80db-95f8-f11b27d865a7
processed_by_ai: true
summary: 'This document outlines a core strategy for leveraging AI agents in software
  development, emphasizing a structured approach with five key principles: vision-first
  planning, professional specification structure, modular context, clear three-tier
  boundaries, and iterative evolution of the spec as code. It focuses on optimizing
  AI interaction for robust project development.'
title: How to Write a Good Spec for AI Agents
tools_mentioned:
- npm
topics:
- AI in Software Development
- Software Engineering
- Project Management
- AI Agent Strategy
- Development Workflow
- Prompt Engineering
- Specification Design
url: https://www.notion.so/How-to-Write-a-Good-Spec-for-AI-Agents-32b9fa3b875080db95f8f11b27d865a7
---

### **The Core Strategy**

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