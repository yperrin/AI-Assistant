---
complexity: Advanced
date: 2026-04-03 07:35:00-04:00
id: 3379fa3b-8750-8066-824a-e5b501d010d5
processed_by_ai: true
summary: This document provides a comprehensive guide to designing, building, and
  scaling AI agent skills, covering their anatomy, essential examples, advanced patterns
  like chaining and agentic loops, and organizational strategies for discovery, validation,
  and lifecycle management. It emphasizes treating skills like software packages and
  highlights their role in dynamic knowledge loading to prevent prompt bloat.
title: Agent Skills Masterclass with Nufar Gaspar
tools_mentioned:
- Anthropic's Skill Creator
- play.brief.ai
- The AI Daily Brief (AI Breakdown)
- CLAUDE.md
topics:
- AI Agents
- Agent Skills
- Prompt Engineering
- Workflow Automation
- Skill Design
- Organizational Scaling
- AI Best Practices
url: https://www.notion.so/Agent-Skills-Masterclass-with-Nufar-Gaspar-3379fa3b87508066824ae5b501d010d5
---

---

### **Level 1: The Apprentice – Understanding the Primitive**

- **Automatic Discovery:** The agent identifies and invokes the skill based on the user's intent.

- **Manual Trigger:** Humans can manually call skills using slash commands or verbal cues (e.g., "research this topic").

> **Safety Warning:** Because third-party skills often contain executable scripts, they should be treated like software packages. Always verify the source to avoid malicious code executing with your agent's permissions [05:11 Opens in a new window ](http://www.youtube.com/watch?v=fs_Y3gvj7lk&t=311).

### **Level 2: The Builder – Anatomy of an Effective Skill**

- **The Trigger:** Use "loud," explicit descriptions so the agent knows exactly when to fire the skill.

- **The Body:** Use **numbered steps** or **bulleted lists**. Be prescriptive for fragile tasks (like coding/DB migrations) but allow creative freedom for strategy or writing tasks [10:44 Opens in a new window ](http://www.youtube.com/watch?v=fs_Y3gvj7lk&t=644).

- **Output Format:** Don't just describe the output; provide a **template or example** (e.g., a specific table structure or document header) [11:35 Opens in a new window ](http://www.youtube.com/watch?v=fs_Y3gvj7lk&t=695).

- **The "Gotcha" Section:** This is the highest-signal content. Explicitly list common model failure points or biases (e.g., "Don't assume attendee seniority based solely on job title") [11:56 Opens in a new window ](http://www.youtube.com/watch?v=fs_Y3gvj7lk&t=716).

### **Level 3: The Arsenal – Essential Skill Examples**

1. **Research with Confidence:** Includes built-in fact-checking and confidence scoring.

1. **Devil’s Advocate:** Systematically stress-tests proposals and identifies blind spots.

1. **Morning Briefing:** Binds personal context (goals, projects, stakeholders) to a daily priority summary.

1. **Board of Advisors:** Simulates perspectives from multiple expert archetypes (e.g., a VC, a CFO, and an entrepreneur).

### **Level 4: The Strategist – Advanced Patterns**

- **Dispatcher (Meta-Skill):** A traffic controller that routes requests to the correct skill to avoid "hallucinated" skill selection.

- **Chaining:** Linking the output of one skill (e.g., Research) as the input for another (e.g., Executive Summary) [20:47 Opens in a new window ](http://www.youtube.com/watch?v=fs_Y3gvj7lk&t=1247).

- **Agentic Loops:** Skills that iterate through "Check → Act → Re-check" cycles, useful for ongoing tasks like marketing campaign optimization [21:23 Opens in a new window ](http://www.youtube.com/watch?v=fs_Y3gvj7lk&t=1283).

### **Level 5: The Architect – Organizational Scaling**

 | **Phase** | **Action Item** | 
 | ---- | ---- | 
 | **Discovery** | Conduct work audits to find repetitive tasks or "wish list" items. | 
 | **Validation** | Use "peer reviews" where team members stress-test each other's skills. | 
 | **Lifecycle** | **Deprecate** skills when they become stale (Gaspar suggests a 1-month review cycle) [26:27 Opens in a new window ](http://www.youtube.com/watch?v=fs_Y3gvj7lk&t=1587). | 

---

### **Resources & References**

- **Companion Data & Templates:** [play.brief.ai](https://www.google.com/search?q=https%3A%2F%2Fplay.brief.ai)

- **Podcast/Show Info:** [The AI Daily Brief (AI Breakdown)](https://aidailybrief.ai/)

- **Anthropic's Skill Creator:** Mentioned as a powerful tool for interviewing users to extract expertise and run benchmarks [09:13 Opens in a new window ](http://www.youtube.com/watch?v=fs_Y3gvj7lk&t=553).

- **Original Video:** [Agent Skills Masterclass with Nufar Gaspar](https://www.youtube.com/watch?v=fs_Y3gvj7lk)

<br/>

- Skills can **run code**, **trigger external systems**, **call APIs**, and **orchestrate multi-step workflows**

- **Two modes:** agents discover & invoke them autonomously, OR humans trigger them manually (`/research this topic`). Skills serve both.

- The problem they solve: system prompts become bloated → performance degrades. Skills load the right knowledge dynamically, only when needed.

 | **Type** | **What It Does** | **Durability** | 
 | ---- | ---- | ---- | 
 | **Capability Uplift** | Enables new functions the model can't do well on its own | May become obsolete as models improve | 
 | **Encoded Preference** | Sequences existing capabilities according to YOUR workflow | Gets more valuable over time | 

 | **Layer** | **What Loads** | **Token Cost** | 
 | ---- | ---- | ---- | 
 | 1. Description | ~100 tokens in system prompt | Always loaded | 
 | 2. SKILL.md body | Full instructions | Only when triggered | 
 | 3. Folder contents | Scripts, assets, references | Only when needed | 

- You do something **more than 3 times** with an AI tool

- You keep pasting the same instructions repeatedly

- You want **consistent, reliable output** across sessions

- You want to **enforce standardization** — the skill becomes the single source of truth

- **Growth mindset:** Build for things you *couldn't* do before, not just automating what you already do

 | **Put IN the Folder When...** | **Point Externally When...** | 
 | ---- | ---- | 
 | Context is specific to this skill and travels with it (rubric, template, persona, examples) | Context is shared across skills or changes independently (CLAUDE.md, project docs, stakeholder list) |