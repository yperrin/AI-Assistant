---
complexity: Advanced
date: 2026-05-02 18:30:00-04:00
id: 3549fa3b-8750-8080-ae49-dd5509af7ef3
processed_by_ai: true
summary: Andrej Karpathy's talk introduces Software 3.0, where Large Language Models
  (LLMs) act as programmable computers, urging developers to shift from "vibe coding"
  to "agentic engineering." The document emphasizes building agent-first infrastructure
  and verifiable domain capabilities to avoid creating "plumbing" that next-generation
  models will render obsolete.
title: Karpathy Just Told Us What Startups To Build For 2026
tools_mentioned:
- Andrej Karpathy
- OpenAI
- Tesla Autopilot
- monday.com
- Claude
- Codeium
- Cursor
- ChatGPT
- Levercast MCP
- llms.txt
- MCP
topics:
- Software 3.0
- Agentic Engineering
- Large Language Models
- AI Development Strategy
- AI Agents
- Startup Strategy
url: https://www.notion.so/Karpathy-Just-Told-Us-What-Startups-To-Build-For-2026-3549fa3b87508080ae49dd5509af7ef3
---

### Executive Summary

In his recent talk, [Andrej Karpathy](https://www.youtube.com/watch?v=rsaaVXg28-8) outlines a fundamental shift in software development, transitioning from handwritten code (Software 1.0) and neural network training (Software 2.0) to **Software 3.0**, where the large language model (LLM) itself acts as the programmable computer. The core problem highlighted is that many current AI startups are merely building "plumbing"—simple wrappers around tasks that next-generation models will soon perform natively.

To survive and thrive in 2026, builders must pivot from "vibe coding" (casual, prompt-based generation) to **agentic engineering**, which involves structured planning, rigorous review, and building for an "agent-first" world. The high-level solution involves focusing on verifiable domains, creating agent-first infrastructure (like `llms.txt`), and building applications that are only possible through the reasoning capabilities of Software 3.0.

---

### Detailed Transcription

**[00:00 Opens in a new window ](http://www.youtube.com/watch?v=rsaaVXg28-8&t=0)** So Andre Karpathy—he's the guy who literally helped build modern AI, who was at OpenAI, who got Tesla autopilot working, and who coined the term "vibe coding"—he just told us: if you're still building apps the way you were last year, he's got bad news for us. He just gave a brilliant talk; I've spent hours breaking it down to help you understand how it may affect what you build as a developer, founder, or software company.

**[00:24 Opens in a new window ](http://www.youtube.com/watch?v=rsaaVXg28-8&t=24)** Thanks to [monday.com](https://bit.ly/4cgHjDN) for sponsoring this video. In the next few minutes, I'm going to walk you through what he actually said about 2026, what it means for what you should be building, and the four frameworks that I think every AI builder needs to have in their head right now. I'm Rob from Switch Dimension, and if you're trying to build with AI in 2026 and beyond, this might be the most important video you watch this month.

**[00:57 Opens in a new window ](http://www.youtube.com/watch?v=rsaaVXg28-8&t=57)** One of the first things that stood out to me was Karpathy's point about the "December inflection." Round about December, the models' output started to actually just work. He stopped correcting it; he started just trusting the model. He basically went on this "vibe coding bender." If you haven't sat down in the last 60 days and seriously tried to build something end-to-end with Claude, Codeium, or Cursor in agent mode, you are flying blind according to Karpathy.

**[01:41 Opens in a new window ](http://www.youtube.com/watch?v=rsaaVXg28-8&t=101)** Karpathy's biggest takeaway was the idea of **Software 3.0**. His breakdown of the evolution is:

- **Software 1.0:** Handwritten rules (writing out code).

- **Software 2.0:** Training neural networks via large datasets.

- **Software 3.0:** The LLM itself becomes the programmable computer. Your code is the prompt, and the context window is your lever.

**[02:42 Opens in a new window ](http://www.youtube.com/watch?v=rsaaVXg28-8&t=162)** Here's the big shift: we're going to be increasingly using our agents to do work for us. Instead of logging into a traditional SaaS app and going through a workflow, I might just say, "Hey, use the Levercast MCP to carry this out." We need to think about building MCPs, APIs, or agentic workflows so an agent can discover our tools quickly.

**[03:47 Opens in a new window ](http://www.youtube.com/watch?v=rsaaVXg28-8&t=227)** Karpathy's example: Last year, he built an app to turn restaurant menus into "magic" by creating AI representations of the food. This year, he could solve the same problem with just ChatGPT. His point: the "Menu Gen" app doesn't need to exist anymore. A huge percentage of apps people are building right now are just "plumbing" wrapped around what should be a single Software 3.0 prompt.

**[04:58 Opens in a new window ](http://www.youtube.com/watch?v=rsaaVXg28-8&t=298)** **The Test:** Take what you're building and ask, "Could I do this with a single multimodal prompt and the right tool calls or an MCP?" If the answer is yes, you're building plumbing that's about to get eaten by the next model release. Stop or pivot.

**[05:26 Opens in a new window ](http://www.youtube.com/watch?v=rsaaVXg28-8&t=326)** Talking about [monday.com Vibe](https://bit.ly/4cgHjDN): It's a natural language app builder baked directly into the platform. You build applications on top of your existing infrastructure and context (workflows, OKRs). It solves the "last mile" problem by creating bespoke interfaces that write back to your data.

**[06:37 Opens in a new window ](http://www.youtube.com/watch?v=rsaaVXg28-8&t=397)** Next point: Verifiability and building a moat. Models are good at code because it's deterministic and verifiable. Karpathy suggests focusing on domains the large labs aren't covering that still have verifiability: financial trading, supply chain, CI/CD agents, and data cleaning.

**[07:35 Opens in a new window ](http://www.youtube.com/watch?v=rsaaVXg28-8&t=455)** He retires the term "vibe coding" and replaces it with **Agentic Engineering**. This means using specs, plans, managing context windows, and doing proper reviews and unit tests. Karpathy says those who get good at this go 10x faster.

**[09:29 Opens in a new window ](http://www.youtube.com/watch?v=rsaaVXg28-8&t=569)** **The Four Things You Should Build:**

1. **Tools for Understanding:** Build tools that enhance your strategic understanding, not just speed. Use strategy agents with markdown-based context folders.

1. **Agent-First Infrastructure:** Strip away human UI. Build for agents using `llms.txt` so they can figure out how to use your product without human marketing fluff.

1. **Verifiable Domain Capabilities:** Focus on reinforcement learning for niche sub-sectors (supply chain, niche finance) where you can own the capability.

1. **Software 3.0 Native Apps:** Build things that *could not* exist before, like massive knowledge bases that no traditional code could orchestrate.

**[13:00 Opens in a new window ](http://www.youtube.com/watch?v=rsaaVXg28-8&t=780)** On a personal note, I killed three of my own side projects after watching Karpathy's talk. They failed the "Software 3.0 test." It’s better to kill them now than watch them die in three months. Double down on apps that hit all four criteria.

---

### Use Case & Solution Index

 | **Category** | **Use Case** | **Solution / Approach** | 
 | ---- | ---- | ---- | 
 | **Development** | Building apps the "old" way (Software 1.0/2.0). | **Software 3.0:** Treat the LLM as the computer; use prompts as code and context as the lever. | 
 | **Workflow** | Manually logging into SaaS apps for tasks. | **Agentic Orchestration:** Build **MCPs (Model Context Protocol)** and APIs so agents can execute tasks for you. | 
 | **App Validation** | Determining if a startup idea is viable or "plumbing." | **The Menu Gen Test:** If it can be done with a single multimodal prompt and tool calls, pivot or stop. | 
 | **Strategic Focus** | Managing multiple side projects and losing track. | **Strategy Agents:** Maintain a folder of markdown documents describing your domain; use an agent to keep you on track. | 
 | **Industry Moat** | Competing with large frontier AI labs. | **Verifiable Domains:** Focus on deterministic fields like financial trading, supply chain optimization, and CI/CD agents. | 
 | **UI/UX** | Designing for human users only. | **Agent-First Infrastructure:** Implement `llms.txt` files and strip away "human translation" layers to let agents interact directly. | 
 | **Engineering** | Scaling development speed beyond "vibe coding." | **Agentic Engineering:** Implement rigorous specs, plans, and unit/smoke tests within agent workflows. |