---
complexity: Advanced
date: 2025-12-21 11:55:00-05:00
id: 2d09fa3b-8750-80b4-bf11-f9e4aafc0ae5
processed_by_ai: true
summary: Gemini Conductor is a new, free context-driven development framework from
  Google for the Gemini CLI, using a spec-driven approach to manage project context
  and facilitate AI-driven code generation. It integrates with Antigravity, an Agentic
  IDE, to create a "Spec-First Agentic" workflow for robust software development and
  architectural health.
title: Gemini Spec development tool Conductor
tools_mentioned:
- Gemini Conductor
- Gemini CLI
- Antigravity
- VS Code
- npm
- Chrome browser automation
- C#
- Angular Signals
topics:
- AI-driven development
- Context-driven development
- Spec-driven development
- Code generation
- AI agents
- Software architecture
- Integrated Development Environments
- Team collaboration
url: https://www.notion.so/Gemini-Spec-development-tool-Conductor-2d09fa3b875080b4bf11f9e4aafc0ae5
---

**Gemini Conductor** is a new, free context-driven development framework from Google designed for the **Gemini CLI**. It moves away from "vibe coding" (imprecise, prompt-based generation) by using a spec-driven approach that turns user intent and constraints into persistent markdown files within your repository [00:32 Opens in a new window ](http://www.youtube.com/watch?v=rLu_3hpG0b8&t=32).

### Key Features

- **Persistent Context:** Keeps project knowledge inside your repo rather than in chat logs, providing AI agents with consistent project awareness [00:49 Opens in a new window ](http://www.youtube.com/watch?v=rLu_3hpG0b8&t=49).

- **Brownfield Project Support:** Specifically designed to handle existing codebases by maintaining living documents of architecture and guidelines [01:44 Opens in a new window ](http://www.youtube.com/watch?v=rLu_3hpG0b8&t=104).

- **Team Alignment:** Allows you to define tech stacks and workflow preferences once, ensuring all AI-generated contributions follow the same standards [02:27 Opens in a new window ](http://www.youtube.com/watch?v=rLu_3hpG0b8&t=147).

- **Spec-Driven Workflow:** Includes commands for setting up products, creating "tracks" for new features or bugs, and implementing code based on detailed specs [04:21 Opens in a new window ](http://www.youtube.com/watch?v=rLu_3hpG0b8&t=261).

### Getting Started

1. **Install Gemini CLI:** Use `npm install -g @google/gemini-cli` [03:13 Opens in a new window ](http://www.youtube.com/watch?v=rLu_3hpG0b8&t=193).

1. **Install Conductor:** Add the extension via the Gemini CLI gallery command [03:42 Opens in a new window ](http://www.youtube.com/watch?v=rLu_3hpG0b8&t=222).

1. **Setup Project:** Run `/conductor setup` to define your project's foundation and product guidelines [04:14 Opens in a new window ](http://www.youtube.com/watch?v=rLu_3hpG0b8&t=254).

1. **Execute Tasks:** Use `/conductor new-track` to plan a feature and `/conductor implement` to have the AI build it [06:58 Opens in a new window ](http://www.youtube.com/watch?v=rLu_3hpG0b8&t=418).

This tool is particularly useful for managing long-context generation and maintaining high code quality in complex, evolving systems [08:50 Opens in a new window ](http://www.youtube.com/watch?v=rLu_3hpG0b8&t=530).

<br/>

You can use **Gemini Conductor** and **Antigravity** together, but they serve different layers of the development process.

In the Google ecosystem as of late 2025, **Antigravity** is the "Agentic IDE" (the workspace), while **Gemini Conductor** is the "Orchestration Extension" (the methodology and CLI toolkit).

### How they work together

Because Antigravity is a fork of VS Code, it supports Gemini CLI extensions.1 Using them together creates a "Spec-First Agentic" workflow:

1. **Conductor as the "Architect":** You use Conductor (via the terminal inside Antigravity) to run `/conductor:setup`. This generates your persistent Markdown files (`product.md`, `tech-stack.md`, etc.).2

1. **Antigravity as the "General Contractor":** Once Conductor has established the **Track** and the **Plan**, Antigravity’s **Agent Manager** (Mission Control) takes over.3 It reads those Markdown files to understand the architectural boundaries you've set.

1. **The Feedback Loop:** When you run `/conductor:implement`, Antigravity spawns its autonomous agents to fulfill the tasks. These agents can use Antigravity's built-in **Chrome browser automation** to verify the UI changes that Conductor planned.4

### Key Integration Points

 | **Feature** | **Role in the Combo** | 
 | ---- | ---- | 
 | **Markdown Artifacts** | Conductor writes the `plan.md`. Antigravity's agents read this as their source of truth, preventing the "drift" common in long chat sessions. | 
 | **Terminal Integration** | You run Conductor commands (like `/conductor:newTrack`) directly in Antigravity's integrated terminal. | 
 | **Verification** | Conductor defines the test strategy in `workflow.md`; Antigravity’s "Self-Healing" loops execute those tests and fix failures autonomously. | 

### Practical Tip for your Management Style

Since you value **long-term architectural health**, you can use Conductor to define your "Technical Constitution" (your preferred C# patterns, Angular Signal usage, etc.) and then point Antigravity's agents at that file. This ensures that even when you are "hands-off," the autonomous agents are constrained by the boundaries you've established in the repo.

---

**Would you like me to generate a **`**tech-stack.md**`** or a **`**workflow.md**`** specifically formatted for a Gemini Conductor/Antigravity setup?**