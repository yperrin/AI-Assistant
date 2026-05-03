---
complexity: Advanced
date: 2026-05-02 15:39:00-04:00
id: 3549fa3b-8750-80f4-a970-f0ab4cb91aac
processed_by_ai: true
summary: This document argues that traditional "boring" enterprise tools like issue
  trackers, CRMs, and ERPs are becoming the essential control planes for AI agents
  in 2026. These tools provide durable state, ownership, audit trails, and permissions,
  which are critical for autonomous agents to perform real-world work and coordinate
  effectively.
title: I Found 5 Things Agents Need From Your Tools. Most Dont Have Them.
tools_mentioned:
- Jira
- Linear
- Symphony
- Bugzilla
- Atlassian
- Rovo MCP server
- Claude
- Salesforce
- HubSpot
- Zendesk
- Service Now
- SAP
- Oracle
- CRMs
- ERPs
topics:
- AI Agents
- Software Infrastructure
- Enterprise Tools
- Workflows
- Coordination
- State Management
- Audit Trails
- Permissions
url: https://www.notion.so/I-Found-5-Things-Agents-Need-From-Your-Tools-Most-Don-t-Have-Them-3549fa3b875080f4a970f0ab4cb91aac
---

This analysis explores the shift in software infrastructure as of 2026, where "boring" enterprise tools like [Jira](http://www.youtube.com/watch?v=FDkvRl1RlT0) and [Linear](http://www.youtube.com/watch?v=FDkvRl1RlT0) are being recontextualized as the essential control planes for AI agents.

---

### 1. Executive Summary

The video argues that the most critical infrastructure for AI agents in 2026 isn't the models themselves, but the "boring" legacy tools used for human coordination. Issue trackers, CRMs, and ERPs provide the **durable state, ownership, and audit trails** that agents lack natively. While the manual "human ceremony" of creating tickets is dying, the underlying data substrate is becoming more valuable. The core takeaway is that **"boring tools are winning"** because they encode the complex coordination logic (state machines, permissions, and dependencies) required for autonomous agents to perform real-world work.

---

### 2. Detailed Transcription

> **Note:** This is a condensed, readable version of the full transcript [available here](http://www.youtube.com/watch?v=FDkvRl1RlT0).

**The Accidental Infrastructure**

[00:00 Opens in a new window ](http://www.youtube.com/watch?v=FDkvRl1RlT0&t=0) This is the story of one of the most surprising software categories of 2026: issue trackers. They were never built for AI, but they happened to encode exactly what agents need: state, ownership, permissions, and history. The issue tracker—the thing people complain about as process overhead—is quietly becoming the most important piece of agent infrastructure.

**The Linear vs. Symphony Contradiction**

[01:22 Opens in a new window ](http://www.youtube.com/watch?v=FDkvRl1RlT0&t=82) Linear's CEO argued that "issue tracking is dead" because agents can read raw context and don't need human translation. However, OpenAI published **Symphony**, an orchestration spec that uses Linear boards as the control plane for autonomous coding agents. The interface for humans might be changing, but the underlying substrate (the state machine) is getting promoted.

**Why Agents Need Issue Trackers**

[06:48 Opens in a new window ](http://www.youtube.com/watch?v=FDkvRl1RlT0&t=408) The shape of tools like Bugzilla (1998) compensatess for human weaknesses like memory gaps and handoff needs. These turn out to be the same weaknesses agents have.

- **Durable State:** The context window is not a source of truth; a database record is.

- **Handoff Semantics:** Agents need to know who owns a task and if it's "blocked" or "ready for review."

- **Auditability:** When an agent fails in production, you need the replayable history these tools have logged for decades.

- **Permissions:** Agents should only do what a human assignee is allowed to do; enterprise tools already have these security models.

**The Anthropic & Atlassian Connection**

[15:21 Opens in a new window ](http://www.youtube.com/watch?v=FDkvRl1RlT0&t=921) If issue trackers are agent substrates, Atlassian owns the largest installed base of agent-readable workstate. Atlassian’s **Rovo MCP server** allows Claude to interact directly with Jira and Confluence. This explains rumors of a potential $40B Anthropic acquisition of Atlassian—it’s about owning the map of how work happens inside the enterprise.

**The Strategy for 2026**

[21:57 Opens in a new window ](http://www.youtube.com/watch?v=FDkvRl1RlT0&t=1317) Every tool should be evaluated by five questions: Does it have records? A state machine? Explicit ownership? Structural verbs? Queryable history? For builders, the goal is making state clean and accessible via APIs or MCP. For leaders, cleaning up messy workflows isn't just hygiene—it's **AI readiness**.

---

### 3. Use Case & Solution Index

 | **Use Case** | **Solution / Agent Strategy** | 
 | ---- | ---- | 
 | **Autonomous Coding** | Use [Symphony](http://www.youtube.com/watch?v=FDkvRl1RlT0) to treat issue tracker boards (like Linear) as the control plane [05:22 Opens in a new window ](http://www.youtube.com/watch?v=FDkvRl1RlT0&t=322). | 
 | **Sales & Revenue** | Leverage **CRMs** (Salesforce/HubSpot) as state machines to research accounts and draft follow-ups within existing deal stages [18:25 Opens in a new window ](http://www.youtube.com/watch?v=FDkvRl1RlT0&t=1105). | 
 | **Customer Support** | Operate through **Service Desks** (Zendesk/Service Now) to utilize existing SLAs, escalation paths, and audit trails [19:02 Opens in a new window ](http://www.youtube.com/watch?v=FDkvRl1RlT0&t=1142). | 
 | **Business Process/ERP** | Use **SAP/Oracle** records to allow agents to handle procurement, payroll, and compliance through defined approval workflows [19:28 Opens in a new window ](http://www.youtube.com/watch?v=FDkvRl1RlT0&t=1168). | 
 | **Coordination of 100+ Agents** | Use the **issue tracker's unit of work** (tickets) to prevent "flat org" problems where agents hold locks or overwrite each other [12:51 Opens in a new window ](http://www.youtube.com/watch?v=FDkvRl1RlT0&t=771). | 
 | **Security & Scoped Access** | Implement **MCP (Model Context Protocol)** servers that respect existing user permissions within Jira or Confluence [14:19 Opens in a new window ](http://www.youtube.com/watch?v=FDkvRl1RlT0&t=859). | 

### Summary Diagnostic for Tools

To determine if a tool is "Agent Infrastructure," ask:

- **Records vs. Content:** Does it store structured data or just text?

- **State Machine:** Does it have defined transitions (e.g., "In Progress" to "Done")?

- **Explicit Ownership:** Is there a specific "Assignee" field?

- **Structural Verbs:** Are actions clear (Assign, Resolve, Block) or just "Reply"?

- **Queryable History:** Can an agent see who changed what and why?