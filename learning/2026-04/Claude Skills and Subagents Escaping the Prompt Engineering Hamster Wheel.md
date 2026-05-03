---
complexity: Advanced
date: 2026-04-05 14:50:00-04:00
id: 3399fa3b-8750-8078-8b1a-fff1c39d39d0
processed_by_ai: true
summary: This article explores how to move beyond repetitive manual prompting by using
  Claude Skills and Subagents to manage context and costs effectively. It details
  how Skills offer reusable, markdown-based instructions with progressive disclosure,
  and Subagents provide specialized, isolated context windows to improve efficiency
  and reduce token usage.
title: Claude Skills and Subagents Escaping the Prompt Engineering Hamster Wheel
tools_mentioned:
- Claude
- GitHub
- MCP
topics:
- AI Agents
- Prompt Engineering
- Context Management
- Cost Optimization
- Large Language Models
- Software Architecture
url: https://www.notion.so/Claude-Skills-and-Subagents-Escaping-the-Prompt-Engineering-Hamster-Wheel-3399fa3b875080788b1afff1c39d39d0
---

The article "[Claude Skills and Subagents: Escaping the Prompt Engineering Hamster Wheel](https://towardsdatascience.com/claude-skills-and-subagents-escaping-the-prompt-engineering-hamster-wheel/)" by [Ruben Broekx](https://towardsdatascience.com/claude-skills-and-subagents-escaping-the-prompt-engineering-hamster-wheel/) explores how to move beyond repetitive manual prompting by using **Skills** and **Subagents** to manage context and costs effectively.

---

### **Core Concepts**

- **The "Hamster Wheel":** The inefficient cycle of manually rewriting or copy-pasting complex prompts for repetitive tasks.

- **Claude Skills:** Reusable, markdown-based instruction sets (stored in `.claude/skills/`) that Claude can auto-invoke. They use **Progressive Disclosure** to save tokens:

	1. **Metadata:** Name and description loaded at startup (~100 tokens).

	1. **Skill Body:** Detailed instructions loaded only when the skill is relevant (~5,000 tokens).

	1. **Referenced Files:** External docs or scripts read only on demand.

- **Subagents:** Specialized "child agents" with isolated context windows. They handle specific tasks (like GitHub PRs) and then discard their intermediate reasoning, returning only the final result to the main agent.

### **Key Advantages**

 | **Feature** | **MCP (Model Context Protocol)** | **Claude Skills** | 
 | ---- | ---- | ---- | 
 | **Focus** | Capabilities (The "What") | Expertise (The "How") | 
 | **Loading** | Eager (All metadata loaded upfront) | Lazy (Loaded only when needed) | 
 | **Cost** | High overhead ($160+/mo in idle tokens) | Minimal; scales with actual usage | 

---

### **Strategic Shifts**

The author argues that AI development has shifted from building "better models" to building **better infrastructure**. By treating agents as "functions"—self-contained units with specific inputs, tools, and outputs—developers can build complex, maintainable, and cost-efficient AI systems.

> **The takeaway:** Use MCP for tool access, Skills for domain expertise, and Subagents to maintain a clean, efficient context window.

Would you like me to dive deeper into the technical structure of a `skill.md` file or explain how to set up the subagent workflow mentioned in the article?