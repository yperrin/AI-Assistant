---
complexity: Advanced
date: 2026-04-03 07:35:00-04:00
id: 3379fa3b-8750-8066-824a-e5b501d010d5
processed_by_ai: true
summary: This masterclass outlines a five-level playbook for developing and scaling
  portable AI Agent Skills, moving beyond basic prompting to create modular, human-readable
  folders that standardize AI interactions across various tools. It covers skill anatomy,
  essential examples, advanced orchestration patterns, and organizational strategies
  for managing a shared skill library.
title: Agent Skills Masterclass with Nufar Gaspar
tools_mentioned:
- Claude
- Cursor
- Windsurf
- Custom GPTs
- GitHub Copilot
- Codex
- Gemini CLI
- Notion
- Anthropic's Skill Creator
- ChatGPT
topics:
- AI Agent Skills
- Prompt Engineering
- Workflow Automation
- AI Agents
- Skill Development
- Organizational Scaling
- AI Best Practices
url: https://www.notion.so/Agent-Skills-Masterclass-with-Nufar-Gaspar-3379fa3b87508066824ae5b501d010d5
---

In this masterclass, **Nufar Gaspar** provides a practical, five-level playbook for transitioning from basic AI prompting to building sophisticated, portable **Agent Skills**. The core philosophy is that skills are not just instructions but actionable, modular folders that standardize how AI interacts with your specific workflows and data.

---

### **Level 1: The Apprentice – Understanding the Primitive**

At their core, agent skills are **portable folders** containing markdown files, scripts, and resources. Unlike "custom GPTs" that are locked into a single platform, these skills are human-readable, highly portable between tools (like Claude, Cursor, or Windsurf), and can be triggered in two modes [03:43 Opens in a new window ](http://www.youtube.com/watch?v=fs_Y3gvj7lk&t=223):

- **Automatic Discovery:** The agent identifies and invokes the skill based on the user's intent.

- **Manual Trigger:** Humans can manually call skills using slash commands or verbal cues (e.g., "research this topic").

> **Safety Warning:** Because third-party skills often contain executable scripts, they should be treated like software packages. Always verify the source to avoid malicious code executing with your agent's permissions [05:11 Opens in a new window ](http://www.youtube.com/watch?v=fs_Y3gvj7lk&t=311).

### **Level 2: The Builder – Anatomy of an Effective Skill**

Gaspar recommends building a skill when you perform a task more than three times or require highly consistent output [05:55 Opens in a new window ](http://www.youtube.com/watch?v=fs_Y3gvj7lk&t=355). An effective skill should follow this structure [09:38 Opens in a new window ](http://www.youtube.com/watch?v=fs_Y3gvj7lk&t=578):

- **The Trigger:** Use "loud," explicit descriptions so the agent knows exactly when to fire the skill.

- **The Body:** Use **numbered steps** or **bulleted lists**. Be prescriptive for fragile tasks (like coding/DB migrations) but allow creative freedom for strategy or writing tasks [10:44 Opens in a new window ](http://www.youtube.com/watch?v=fs_Y3gvj7lk&t=644).

- **Output Format:** Don't just describe the output; provide a **template or example** (e.g., a specific table structure or document header) [11:35 Opens in a new window ](http://www.youtube.com/watch?v=fs_Y3gvj7lk&t=695).

- **The "Gotcha" Section:** This is the highest-signal content. Explicitly list common model failure points or biases (e.g., "Don't assume attendee seniority based solely on job title") [11:56 Opens in a new window ](http://www.youtube.com/watch?v=fs_Y3gvj7lk&t=716).

### **Level 3: The Arsenal – Essential Skill Examples**

The masterclass highlights four foundational skills for knowledge workers [17:26 Opens in a new window ](http://www.youtube.com/watch?v=fs_Y3gvj7lk&t=1046):

1. **Research with Confidence:** Includes built-in fact-checking and confidence scoring.

1. **Devil’s Advocate:** Systematically stress-tests proposals and identifies blind spots.

1. **Morning Briefing:** Binds personal context (goals, projects, stakeholders) to a daily priority summary.

1. **Board of Advisors:** Simulates perspectives from multiple expert archetypes (e.g., a VC, a CFO, and an entrepreneur).

### **Level 4: The Strategist – Advanced Patterns**

For those managing libraries of 10+ skills, advanced orchestration patterns become necessary [20:07 Opens in a new window ](http://www.youtube.com/watch?v=fs_Y3gvj7lk&t=1207):

- **Dispatcher (Meta-Skill):** A traffic controller that routes requests to the correct skill to avoid "hallucinated" skill selection.

- **Chaining:** Linking the output of one skill (e.g., Research) as the input for another (e.g., Executive Summary) [20:47 Opens in a new window ](http://www.youtube.com/watch?v=fs_Y3gvj7lk&t=1247).

- **Agentic Loops:** Skills that iterate through "Check → Act → Re-check" cycles, useful for ongoing tasks like marketing campaign optimization [21:23 Opens in a new window ](http://www.youtube.com/watch?v=fs_Y3gvj7lk&t=1283).

### **Level 5: The Architect – Organizational Scaling**

The "Architect" level focuses on treating skills as **organizational infrastructure**. Organizations should move away from individuals "reinventing the wheel" in every chat toward a shared, version-controlled skill library [23:31 Opens in a new window ](http://www.youtube.com/watch?v=fs_Y3gvj7lk&t=1411).

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

Companion Data

**What Are Skills?**

At their core, skills are **folders** — not just markdown files — containing instructions, scripts, and resources that give AI agents new capabilities.

- Skills can **run code**, **trigger external systems**, **call APIs**, and **orchestrate multi-step workflows**

- **Two modes:** agents discover & invoke them autonomously, OR humans trigger them manually (`/research this topic`). Skills serve both.

- The problem they solve: system prompts become bloated → performance degrades. Skills load the right knowledge dynamically, only when needed.

**The Portability Breakthrough**

Custom GPTs were locked inside ChatGPT. Skills are **portable, human-readable markdown folders**. Build once, use across tools. No proprietary format, no vendor lock-in. Anyone can read, edit, and maintain a skill — no engineering required.

This is what custom GPTs *should* have been.

**The Ecosystem**

**44+ AI tools** already support skills: Claude Code, Cursor, Windsurf, GitHub Copilot, Codex, Gemini CLI, Notion, and many more. This is becoming a universal standard.

**Two Fundamental Types**

 | **Type** | **What It Does** | **Durability** | 
 | ---- | ---- | ---- | 
 | **Capability Uplift** | Enables new functions the model can't do well on its own | May become obsolete as models improve | 
 | **Encoded Preference** | Sequences existing capabilities according to YOUR workflow | Gets more valuable over time | 

Spend most time on **preference skills**. They encode how YOUR team works.

**Progressive Disclosure**

 | **Layer** | **What Loads** | **Token Cost** | 
 | ---- | ---- | ---- | 
 | 1. Description | ~100 tokens in system prompt | Always loaded | 
 | 2. SKILL.md body | Full instructions | Only when triggered | 
 | 3. Folder contents | Scripts, assets, references | Only when needed | 

⚠ Security Warning

Third-party skills are code that runs with your agent's permissions. Always audit before installing. Treat skill installation like installing a browser extension.

**When to Build a Skill**

- You do something **more than 3 times** with an AI tool

- You keep pasting the same instructions repeatedly

- You want **consistent, reliable output** across sessions

- You want to **enforce standardization** — the skill becomes the single source of truth

- **Growth mindset:** Build for things you *couldn't* do before, not just automating what you already do

**Scoping Rule**

One clear job per skill. If you can't describe what it does in one sentence, it's probably two skills.

**Reuse vs. Create**

Growing libraries exist (Anthropic skills repo: 87K+ GitHub stars). But for your **first skills: build your own.** Browsing marketplaces is tedious, quality varies, and security concerns are real. Building from scratch teaches you the craft faster than adopting someone else's 70%-right skill.

**The Skill Creator Tool**

Claude's built-in tool — but the pattern can be emulated in any tool by building a "skill for building skills." It interviews you, runs evals, does A/B testing, and iteratively improves your skill's description for better triggering.

**Skill Anatomy**

**name **Lowercase, hyphens, max 64 chars. Gerund form: `analyzing-data`, `preparing-meetings`

**description The most critical line. **A **trigger, not a summary. **Write for the model asking "when should I fire?"

Pro tip: make it LOUDER rather than quieter. Write in third person. Include both what it does and when to use it.

**Instructions **Favor **numbered steps or bulleted lists over prose.** Set degrees of freedom: tight for fragile ops, loose for creative tasks.

**Output Format **Show, don't describe. Include a literal template or example.

**Gotcha Section Highest-signal content.** Where does the model go wrong? "I know you'll want to do X — don't."

**Constraints **What NOT to do. Sharp and specific to THIS skill.

Skip This

**Identity / Role section **("Act as a senior analyst...") — legacy prompt engineering pattern. Tell the model what YOUR approach does differently, not what persona to adopt.

**The 5 Skill Killers**

1 **Description doesn't trigger properly** — too vague, too narrow, or wrong personFix: Specific, loud, third-person. "Use when..." format.

2 **Over-defining the process** — railroading instead of guidingFix: Set degrees of freedom. Tight for fragile ops, loose for creative.

3 **Stating the obvious** — wasting tokens on what the model knowsFix: Challenge every paragraph: "Does Claude really need this?"

4 **Missing gotcha section** — not capturing failure patternsFix: Document every failure you've seen. This IS the skill's value.

5 **Monolithic blob** — everything in one fileFix: SKILL.md under 500 lines. Move references to separate files.

**Context Binding: In-Folder vs. External**

 | **Put IN the Folder When...** | **Point Externally When...** | 
 | ---- | ---- | 
 | Context is specific to this skill and travels with it (rubric, template, persona, examples) | Context is shared across skills or changes independently (CLAUDE.md, project docs, stakeholder list) | 

Rule of thumb: "about the skill" = inside. "About you/your org" = outside.

**Showcase: Meeting Prep Skill**

meeting-prep/
├── SKILL.md              *# Core instructions*

├── stakeholder-context.md  *# External pointer*

├── output-template.md      *# Structured brief format*

├── scenarios.md            *# Meetings that go off the rails*

├── examples.md             *# Great vs. mediocre prep*└── skills/
    └── meeting-sim/
        └── SKILL.md        *# Nested: simulate the meeting*

📄meeting-prep/SKILL.md

SKILL.md

Full skill folder (SKILL.md + scenarios.md + output-template.md + meeting-sim/) available in the **Expansion Pack → Blueprints** section below.