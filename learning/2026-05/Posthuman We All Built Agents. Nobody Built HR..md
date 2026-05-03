---
complexity: Advanced
date: 2026-05-03 09:49:00-04:00
id: 3559fa3b-8750-8004-bf88-d4bef2bf9890
processed_by_ai: true
summary: 'This article argues that the enterprise adoption of AI agents is hindered
  by a lack of "HR" or governance infrastructure, not by the agents'' capabilities.
  It proposes an "out-of-band" governance framework with four pillars: identity, authorization,
  observability, and accountability, to manage imperfect agents safely in production.'
title: Posthuman We All Built Agents. Nobody Built HR.
tools_mentioned:
- OAuth 2.0 Token Exchange
topics:
- AI Agents
- Enterprise AI
- AI Governance
- Infrastructure
- Security
- Identity Management
- Authorization
- Observability
- Accountability
- Prompt Injection
- Microservices
url: https://www.notion.so/Posthuman-We-All-Built-Agents-Nobody-Built-HR-3559fa3b87508004bf88d4bef2bf9890
---

This article, [Posthuman: We All Built Agents. Nobody Built HR.](https://www.oreilly.com/radar/posthuman-we-all-built-agents-nobody-built-hr/), by Tyler Akidau, explores the critical infrastructure gap in enterprise AI. While the industry has focused on building more capable agents, it has neglected the "HR" or governance frameworks required to manage them safely in production environments.

---

## 1. Executive Summary

The core thesis is that **AI agents are a fundamentally new kind of coworker**: unpredictable like humans, capable like software, and directable to a fault. Current enterprise adoption has faltered not because models are poor, but because we lack the infrastructure to trust them.

- **The Problem:** Agents combine the worst traits of humans (unpredictability/hallucinations) and software (speed/scale) without the human judgment to push back on bad plans.

- **The High-Level Solution:** Shift from "in-band" governance (relying on prompts or training) to **out-of-band governance**. This means enforcing security, identity, and accountability through infrastructure channels that the agent cannot see, modify, or circumvent.

- **Key Takeaway:** We don't need perfect agents; we need a robust management framework—digital HR—to orchestrate imperfect agents safely.

---

## 2. Detailed Transcription

*Note: The following is a faithful representation of the full content provided in the article transcript.*

### Introduction: The Agentic Wasteland

The "Anthropocene" is ending as AI wins, yet enterprise agentic AI—software that autonomously performs meaningful tasks in production—remains a wasteland of sandboxed demos and "snake oil." Akidau argues this isn't a model problem. Human organizations function with imperfect people because of management frameworks; agents need the same.

### Why Agents are Different

Agents differ from humans in three vital ways:

1. **Unpredictability:** They hallucinate in ways that are structurally indistinguishable from truth and are susceptible to prompt injection.

1. **Machine-Scale Capability:** They possess native fluency in code and APIs, allowing them to execute misunderstandings at speeds no human can match.

1. **Faulty Directability:** They lack human judgment and will faithfully execute a bad or underspecified plan without pushing back.

### The Missing HR Infrastructure

We are in a "panic-in-between" phase. Just as microservices required a service mesh, agents require a governance layer. Akidau proposes the **Out-of-Band Metadata** principle: Governance must be enforced via channels agents cannot access, modify, or circumvent. It must be agent-inaccessible, deterministic, and interoperable.

### The Four Pillars of Agent Governance

1. **Identity:** Agents need **instance-bound** identities (cryptographically unique to a specific task) and **delegation-aware** chains (knowing which human authorized the action).

1. **Authorization:** Moving away from broad human "roles" toward **narrowly scoped, short-lived, and deny-capable** permissions. The effective permission should be the intersection of the agent’s scope and the human's authority.

1. **Observability & Explainability:** We must record **everything**—full-fidelity transcripts of every input and output—out-of-band. This is necessary because LLMs are opaque; you cannot trace logic like a standard `if` statement.

1. **Accountability & Control:** Establishing clear responsibility chains and "kill switches" (surgical revocation of a specific instance) to contain damage and manage costs.

### Conclusion: The Posthuman Workforce

The era defined by how humans shape the world hasn't changed; we are simply onboarding new "agentic coworkers." By building the right infrastructure, we can manage imperfect agents just as we have managed imperfect humans for decades.

---

## 3. Use Case & Solution Index

 | **Use Case / Scenario** | **Proposed Infrastructure Solution** | 
 | ---- | ---- | 
 | **Preventing Prompt Injection** | **Out-of-Band Enforcement:** Move rules out of the system prompt and into deterministic infrastructure the agent cannot see or influence. | 
 | **Limiting "Blast Radius" of Rogue Agents** | **Instance-Bound Identity:** Assign a unique cryptographic ID to every individual task instance so it can be revoked without killing other agents. | 
 | **Handling Excessive Permissions** | **Task-Scoped Auth:** Grant read/write access only to the specific tables/APIs needed for a single job; permissions evaporate upon completion. | 
 | **Audit & Regulatory Compliance** | **Full-Fidelity Transcripts:** Capture every input, output, and tool call (including versions) to reconstruct reasoning for third-party auditors. | 
 | **Human-on-Behalf-Of Actions** | **Hybrid Identity / Token Exchange:** Use standards like [OAuth 2.0 Token Exchange](https://datatracker.ietf.org/doc/html/rfc8693) to propagate the identity of the authorizing human through the agent chain. | 
 | **Controlling Costs & Infinite Loops** | **Resource Quotas & Kill Switches:** Implement infrastructure-level limits on inference budgets and the ability to surgically halt specific "confused" agents. | 
 | **Remediating Bad Data** | **Structured Observability:** Use full transcripts as a roadmap to identify and "undo" specific downstream actions triggered by an agent error. |