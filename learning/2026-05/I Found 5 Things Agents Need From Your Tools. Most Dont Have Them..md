---
complexity: Advanced
date: 2026-05-02 15:39:00-04:00
id: 3549fa3b-8750-80f4-a970-f0ab4cb91aac
processed_by_ai: true
summary: This document discusses how to effectively coordinate AI agents by leveraging
  existing enterprise tools as control planes, emphasizing the importance of durable
  state, handoff semantics, auditability, and permissions. It outlines various use
  cases where agents can integrate with systems like issue trackers, CRMs, and ERPs
  to manage tasks and workflows.
title: I Found 5 Things Agents Need From Your Tools. Most Dont Have Them.
tools_mentioned:
- Symphony
- Linear
- Salesforce
- HubSpot
- Zendesk
- Service Now
- SAP
- Oracle
- Jira
- Confluence
- MCP (Model Context Protocol)
topics:
- AI Agents
- Enterprise Systems
- Workflow Automation
- State Management
- Permissions
- Auditability
- Autonomous Coding
- Customer Support
- Sales & Revenue
- Business Process Management
url: https://www.notion.so/I-Found-5-Things-Agents-Need-From-Your-Tools-Most-Don-t-Have-Them-3549fa3b875080f4a970f0ab4cb91aac
---

---

### 1. Executive Summary

---

### 2. Detailed Transcription

> **Note:** This is a condensed, readable version of the full transcript [available here](http://www.youtube.com/watch?v=FDkvRl1RlT0).

- **Durable State:** The context window is not a source of truth; a database record is.

- **Handoff Semantics:** Agents need to know who owns a task and if it's "blocked" or "ready for review."

- **Auditability:** When an agent fails in production, you need the replayable history these tools have logged for decades.

- **Permissions:** Agents should only do what a human assignee is allowed to do; enterprise tools already have these security models.

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

- **Records vs. Content:** Does it store structured data or just text?

- **State Machine:** Does it have defined transitions (e.g., "In Progress" to "Done")?

- **Explicit Ownership:** Is there a specific "Assignee" field?

- **Structural Verbs:** Are actions clear (Assign, Resolve, Block) or just "Reply"?

- **Queryable History:** Can an agent see who changed what and why?