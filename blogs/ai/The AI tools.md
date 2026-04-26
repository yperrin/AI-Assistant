# The AI tools

**By:** [Yann Perrin](https://clarivate.atlassian.net/wiki/spaces/LSHT/blog/2026/03/28/303300868/The+AI+tools)  
**Date:** March 28, 2026  
**Read Time:** 4 min

I get that question all the time so I figured I should write about it. I cannot list all of them, of course, but I thought it might be a good idea to at least have a quick discussion about some of them. We have GitHub Copilot, Claude, Codex, Antigravity, Cursor, Windsurf, etc.

We also need to put the tools in the context of the organization's (and the developers') maturity. For the sake of argument:

* **Level 1** - isolated development tasks
* **Level 2** - specialized agents and multi-agents orchestration
* **Level 3** - AI First organization

---

### Level 1: Isolated Development Tasks
**Copilot** seems to be a good tool for Level 1. It has a reasonable cost, but at the basis of it, it is built as an extension to an editor and that brings issues. It seems to be limited in how much context it can support and seems to be struggling when editing more than 10 files. It has a lot of features but ultimately it is a tool meant to support developers with manual intervention on a smaller scale.

### Level 2: Specialized Agents & Orchestration
Level 2 can be a combination of **Cursor** and **Claude** (or **Opex** favored by OpenClaw developer). **Windsurf** seems to be a cheaper version of Cursor. 

Cursor and Claude are not cheap. Those tools are more adept at multi-file context and deep architectural reasoning. They both favor a more agent-native approach and are more capable of providing proactive orchestration, where agents autonomously monitor repository health, investigate CI failures, and propose architectural changes without being prompted for every step. 

* **Opex** seems to be stronger for non-UI projects.
* **Claude** shines with UI projects.
* **Antigravity** is a strong contender, especially with its very interactive way of producing and reviewing artifacts, though it faces strong competition as other tools catch up.

> **Note on Cost:** These tools are not cheap; they include heavy token usage, and it is not unheard of to spend >$100 in one day on a pay-as-you-go plan. Fixed subscription plans often have limits with multiple agents, allowing only one active session at a time.

### Level 3: AI-First Organization
For Level 3, it is a little more complicated. It involves creating company-specific agent teams with tight integration with the company's data, products, and APIs. This should include:
* Specific security guardrails.
* Full audit and traceability for all critical workflows.
* Integration across the entire company structure (not just software engineering).

---

## Final Thoughts
I still believe GitHub Copilot is a little underrated, but at some point, we will hit a certain limit that I am not sure background (CLI) and cloud agents will be able to overcome. Ultimately, even with the CLI, GitHub Copilot has limitations on how well it can handle coordination across 30+ files.

**Updates on my experiments:**
I got my multi-agents loop using **LangGraph** working—agents arguing with themselves until they reach an agreement. However, my local **deepseek-r1** model seems to be crashing docker (time to use the re-try built-in functionality) and I am not yet getting the results I am looking for. Time for prompt engineering.