---
complexity: Intermediate
date: 2026-05-03 11:04:00-04:00
id: 3559fa3b-8750-8000-9a6e-e2cd514e4624
processed_by_ai: true
summary: This document outlines the concept of "skills" for AI agents, which are modular,
  reusable instructions and assets designed to extend agent capabilities, prevent
  prompt bloat, and standardize workflows. It covers the anatomy of effective skills,
  advanced patterns like chaining and loops, and strategies for building and managing
  organizational skill libraries.
title: Skill Master Class
tools_mentioned: []
topics:
- AI Agents
- Skill Development
- Prompt Engineering
- Workflow Automation
- Knowledge Management
- System Design
- Best Practices
url: https://www.notion.so/Skill-Master-Class-3559fa3b875080009a6ee2cd514e4624
---

## Executive Summary

---

## Detailed Transcription

### 1. Apprentice: Understanding the Skill Landscape

- Skills can run code, trigger external systems, call APIs, and orchestrate multi-step workflows.

- **Two modes:** Agents discover and invoke them autonomously, or humans trigger them manually (e.g., `/research this topic`).

- **The Problem:** System prompts become bloated, causing performance to degrade. Skills load knowledge dynamically only when needed.

- **Capability Uplift:** Enables new functions the model can't do well alone. (May become obsolete as models improve).

- **Encoded Preference:** Sequences existing capabilities according to YOUR workflow. (Gets more valuable over time).

1. **Description:** (~100 tokens) Always loaded in the system prompt to help the agent decide when to trigger.

1. **SKILL.md body:** Full instructions loaded only when triggered.

1. **Folder contents:** Scripts and assets loaded only when needed.

---

### 2. Builder: Anatomy of an Effective Skill

- You do something more than 3 times.

- You keep pasting the same instructions.

- You want consistent, reliable, and standardized output.

- **Scoping Rule:** One clear job per skill. "If you can't describe it in one sentence, it's probably two skills."

- **Name:** Lowercase, hyphens (e.g., `preparing-meetings`).

- **Description:** A "trigger," not a summary. Write in third person: "Use when..."

- **Instructions:** Numbered steps/bullets. Set "degrees of freedom" (tight for fragile ops, loose for creative).

- **Output Format:** Show, don't describe. Use templates.

- **Gotcha Section:** Highest signal content. Document where models usually fail.

- **Constraints:** What NOT to do.

1. Description doesn't trigger properly.

1. Over-defining the process (railroading).

1. Stating the obvious.

1. Missing the "Gotcha" section.

1. Monolithic blobs (keep SKILL.md under 500 lines).

---

### 3. Arsenal: Your Starter Kit

1. `research-with-confidence/SKILL.md` (Capability)

1. `devils-advocate/SKILL.md` (Preference)

1. `morning-briefing/SKILL.md` (Preference)

1. `board-of-advisors/SKILL.md` (Preference)

---

### 4. Strategist: Advanced Patterns

- **Skill Dispatcher:** Routes requests to the right skill when libraries grow (10-15+ skills).

- **Skill Chaining:** Output of one skill becomes the input for the next.

- **Loop Skills:** Iterative "check-act-check" cycles.

- **Agentic Loops:** Spawning sub-agents to maintain state.

- **The Litmus Test:** If you have to edit the output after the skill runs, the skill is broken.

- **Re-evaluate:** When models update, tools change, or results degrade.

---

### 5. Architect: Organizational Skill Libraries

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