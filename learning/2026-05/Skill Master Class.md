---
complexity: Advanced
date: 2026-05-03 11:04:00-04:00
id: 3559fa3b-8750-8000-9a6e-e2cd514e4624
processed_by_ai: true
summary: This document explores the concept of "Skills" as portable, human-readable
  markdown folders that enhance AI agent capabilities, moving beyond bloated system
  prompts and custom GPTs. It advocates for "Progressive Disclosure" and "Preference
  Skills" to standardize AI interactions, prevent vendor lock-in, and improve performance
  across various AI platforms.
title: Skill Master Class
tools_mentioned:
- Cursor
- Claude Code
- GitHub Copilot
- ChatGPT
- Windsurf
topics:
- AI Agents
- Skills (AI)
- Prompt Engineering
- AI Tooling
- Portability
- Workflow Automation
- Organizational Knowledge Management
- Agentic Systems
- Progressive Disclosure
url: https://www.notion.so/Skill-Master-Class-3559fa3b875080009a6ee2cd514e4624
---

## Executive Summary

The [Skills Master Class](https://play.aidailybrief.ai/episodes/skills-master-class/) explores the evolution of AI interactions from "bloated" system prompts to **Skills**—portable, human-readable markdown folders that give agents dynamic capabilities. The core problem addressed is the performance degradation and "vendor lock-in" associated with custom GPTs and massive instructions.

The high-level solution is a shift toward **Progressive Disclosure**, where agents load only the necessary context (scripts, APIs, and specific instructions) when triggered. This framework emphasizes "Preference Skills"—which encode unique organizational workflows—over simple "Capability Uplifts," ensuring that AI becomes a standardized, portable tool across different platforms like Cursor, Claude Code, and GitHub Copilot.

---

## Detailed Transcription

### 1. Apprentice: Understanding the Skill Landscape

**What are Skills?**

At their core, skills are *folders*—not just markdown files—containing instructions, scripts, and resources that give AI agents new capabilities.

- Skills can run code, trigger external systems, call APIs, and orchestrate multi-step workflows.

- **Two modes:** Agents discover and invoke them autonomously, or humans trigger them manually (e.g., `/research this topic`).

- **The Problem:** System prompts become bloated, causing performance to degrade. Skills load knowledge dynamically only when needed.

**The Portability Breakthrough**

Custom GPTs were locked inside ChatGPT. Skills are portable markdown folders. Build once, use across tools. No proprietary format or vendor lock-in. Anyone can read, edit, and maintain a skill without engineering knowledge.

**The Ecosystem**

Over 44+ AI tools support skills (Claude Code, Cursor, Windsurf, GitHub Copilot, etc.), making this a universal standard.

**Two Fundamental Types**

- **Capability Uplift:** Enables new functions the model can't do well alone. (May become obsolete as models improve).

- **Encoded Preference:** Sequences existing capabilities according to YOUR workflow. (Gets more valuable over time).

**Progressive Disclosure Layers**

1. **Description:** (~100 tokens) Always loaded in the system prompt to help the agent decide when to trigger.

1. **SKILL.md body:** Full instructions loaded only when triggered.

1. **Folder contents:** Scripts and assets loaded only when needed.

---

### 2. Builder: Anatomy of an Effective Skill

**When to Build a Skill**

- You do something more than 3 times.

- You keep pasting the same instructions.

- You want consistent, reliable, and standardized output.

- **Scoping Rule:** One clear job per skill. "If you can't describe it in one sentence, it's probably two skills."

**Skill Anatomy**

- **Name:** Lowercase, hyphens (e.g., `preparing-meetings`).

- **Description:** A "trigger," not a summary. Write in third person: "Use when..."

- **Instructions:** Numbered steps/bullets. Set "degrees of freedom" (tight for fragile ops, loose for creative).

- **Output Format:** Show, don't describe. Use templates.

- **Gotcha Section:** Highest signal content. Document where models usually fail.

- **Constraints:** What NOT to do.

**The 5 Skill Killers**

1. Description doesn't trigger properly.

1. Over-defining the process (railroading).

1. Stating the obvious.

1. Missing the "Gotcha" section.

1. Monolithic blobs (keep SKILL.md under 500 lines).

---

### 3. Arsenal: Your Starter Kit

The class identifies 4 skills every knowledge worker should have (customized to their specific context):

1. `research-with-confidence/SKILL.md` (Capability)

1. `devils-advocate/SKILL.md` (Preference)

1. `morning-briefing/SKILL.md` (Preference)

1. `board-of-advisors/SKILL.md` (Preference)

---

### 4. Strategist: Advanced Patterns

**Advanced Patterns**

- **Skill Dispatcher:** Routes requests to the right skill when libraries grow (10-15+ skills).

- **Skill Chaining:** Output of one skill becomes the input for the next.

- **Loop Skills:** Iterative "check-act-check" cycles.

- **Agentic Loops:** Spawning sub-agents to maintain state.

**Testing & Optimization**

- **The Litmus Test:** If you have to edit the output after the skill runs, the skill is broken.

- **Re-evaluate:** When models update, tools change, or results degrade.

---

### 5. Architect: Organizational Skill Libraries

**The Opportunity**

Skills allow for the standardization of execution and knowledge. Organizations are now using "Skill Hackathons" to build shared libraries, preventing employees from "reinventing the wheel" in every AI chat.

**The Plugin Model**

The future is "Plugins": A bundle of skills + MCP (Model Context Protocol) connections (e.g., a "Sales Review" plugin containing the skill + CRM access + specific VP templates).

**The 5-Stage Process**

1. **Discovery:** Audit work to see where instructions are repeated.

1. **Curation:** Prioritize by frequency and impact.

1. **Validation:** A/B test against unstructured prompting.

1. **Bundling:** Package into team-wide or org-wide bundles.

1. **Ownership:** Assign Subject Matter Experts (SMEs) to maintain and review quarterly.

---

## Use Case & Solution Index

### Meeting Management

- **Use Case:** Preparing for complex meetings with multiple stakeholders.

- **Solution:** A `meeting-prep` skill folder containing a core `SKILL.md`, a `stakeholder-context.md`, and a `meeting-sim` sub-skill to simulate potential "off the rails" scenarios.

### Research & Analysis

- **Use Case:** Performing deep-dives while avoiding hallucinations or shallow summaries.

- **Solution:** `research-with-confidence` skill that enforces specific source-checking and utilizes "Skill Chaining" (Research -> Devil's Advocate -> Executive Summary).

### Content & Quality Assurance

- **Use Case:** Ensuring marketing or recruitment content matches brand style and compliance.

- **Solution:** **Loop Skills** that draft content, review it against a style guide, revise, and check for compliance before flagging for human approval.

### Competitive Intelligence

- **Use Case:** Monitoring competitor changes daily without manual browsing.

- **Solution:** **Agentic Loops** that scan competitor sites, compare findings to a baseline, and alert the user only on meaningful changes.

### Organizational Knowledge Management

- **Use Case:** Onboarding new team members or standardizing output across a global team.

- **Solution:** **Organizational Skill Libraries** curated by SMEs, providing a "single source of truth" for how the team interacts with AI.