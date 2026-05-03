---
complexity: Intermediate
date: 2026-04-27
id: 34f9fa3b-8750-8077-b55c-f5c56d991e7a
processed_by_ai: true
summary: This document distinguishes between "vibe coding" (quick, prompt-driven prototyping)
  and "professional AI coding" (disciplined, spec-driven engineering), advocating
  for human-driven architectural decisions and detailed specifications for production-grade
  AI development. It outlines a professional workflow involving detailed PRDs, human
  architectural decisions, and AI plan confirmation before execution.
title: I found the line splitting AI coding
tools_mentioned:
- Supabase
- Claude Code
- GitHub Copilot
topics:
- AI Coding
- Software Development Methodologies
- Product Development
- System Design
- AI Agents
- Prompt Engineering
url: https://www.notion.so/I-found-the-line-splitting-AI-coding-34f9fa3b87508077b55cf5c56d991e7a
---

This transcript from [Axel Molist](https://www.youtube.com/watch?v=cutcJRspRhQ) explores the distinction between "vibe coding" (quick, prompt-driven prototyping) and "professional AI coding" (disciplined, spec-driven engineering).

---

### **1. The Two Worlds of AI Coding**

 | **Feature** | **Vibe Coding** | **Professional AI Coding** | 
 | ---- | ---- | ---- | 
 | **Primary Driver** | Prompt-by-prompt "vibes" | Detailed PRDs and Spec Docs | 
 | **Infrastructure** | Chosen by AI (e.g., Supabase) | Human architected | 
 | **Verification** | "If it works, it works" | AI plan confirmation before execution | 
 | **Best For** | Internal tools, simple prototypes | Scalable SaaS, production systems | 
 | **Risk Level** | High technical debt, hard to refactor | Sustainable, documented, secure | 

---

### **2. The Professional Workflow ****[02:33 Opens in a new window](http://www.youtube.com/watch?v=cutcJRspRhQ&t=153)**

For professional-grade output, Axel argues that three things must happen before a single line of code is written:

1. **Detailed PRD & Spec:** Markdown files so tight that three different developers (or AI agents) would build the exact same thing in isolation [02:41 Opens in a new window ](http://www.youtube.com/watch?v=cutcJRspRhQ&t=161).

1. **Human Architectural Decisions:** A human engineer decides on the data models, API structures, and security—not the AI agent [02:58 Opens in a new window ](http://www.youtube.com/watch?v=cutcJRspRhQ&t=178).

1. **The Feedback Loop:** The AI must feed back its understanding and plan ("Here is what I'm about to do") for human approval before starting the build [03:16 Opens in a new window ](http://www.youtube.com/watch?v=cutcJRspRhQ&t=196).

---

### **3. Key Concepts & Case Studies**

- **The "Anti-Ambiguity Agent" ****[05:34 Opens in a new window ](http://www.youtube.com/watch?v=cutcJRspRhQ&t=334)****:** A specialized agent designed to scrutinize PRDs and specs specifically to find and resolve "fuzzy" requirements before passing them to a coding tool like [Claude Code](https://www.anthropic.com/claude).

- **The Commercial Refurbishment Tool ****[01:16 Opens in a new window ](http://www.youtube.com/watch?v=cutcJRspRhQ&t=76)****:** A non-technical user successfully built a contractor management app in a week via vibe coding, but didn't even know what database he was using.

- **The Dental Practice OS ****[06:52 Opens in a new window ](http://www.youtube.com/watch?v=cutcJRspRhQ&t=412)****:** A tech-savvy dentist paired with a senior developer to build a full CRM and billing system in 10 weeks using a professional AI-first methodology.

---

### **4. Maturity Levels of AI Coding ****[08:42 Opens in a new window](http://www.youtube.com/watch?v=cutcJRspRhQ&t=522)**

Referencing Dan Shapiro's framework, Axel outlines the progression of AI integration:

- **Level 0:** Spicy Autocomplete (e.g., GitHub Copilot).

- **Levels 1-2:** Human-driven with AI assistance.

- **Levels 3-4:** AI writes most code; humans focus on PRDs, specs, and reviews.

- **Level 5 ("The Dark Factory"):** AI writes 100% of the code from specs without human intervention [09:13 Opens in a new window ](http://www.youtube.com/watch?v=cutcJRspRhQ&t=553).

> **Key Takeaway:** "The AI is the muscle, the human is the brain. The AI does the typing and the human does the engineering." [03:39 Opens in a new window](http://www.youtube.com/watch?v=cutcJRspRhQ&t=219)