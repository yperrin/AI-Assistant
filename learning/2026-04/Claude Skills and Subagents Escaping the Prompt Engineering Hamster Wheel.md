---
title: Claude Skills and Subagents Escaping the Prompt Engineering Hamster Wheel
id: 3399fa3b-8750-8078-8b1a-fff1c39d39d0
url: https://www.notion.so/Claude-Skills-and-Subagents-Escaping-the-Prompt-Engineering-Hamster-Wheel-3399fa3b875080788b1afff1c39d39d0
---

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

> **The takeaway:** Use MCP for tool access, Skills for domain expertise, and Subagents to maintain a clean, efficient context window.

