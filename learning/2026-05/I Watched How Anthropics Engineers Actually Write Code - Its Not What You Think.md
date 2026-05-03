---
complexity: Advanced
date: 2026-05-03 14:55:00-04:00
id: 3559fa3b-8750-80d5-b3be-e06a069a8652
processed_by_ai: true
summary: This document discusses "vibe coding," a concept where AI fully generates
  code, and how to implement it responsibly in production. It emphasizes engineers
  acting as Product Managers for AI, focusing on leaf-node features, and prioritizing
  automated verifiability to keep pace with exponential AI growth.
title: I Watched How Anthropics Engineers Actually Write Code - Its Not What You Think
tools_mentioned:
- Anthropic
- Cursor
- GitHub Copilot
- Claude
- Claude Code
- Compilers
- Claude 3.7
- Claude 4
topics:
- AI Code Generation
- Vibe Coding
- Software Engineering
- AI Agents
- Technical Debt
- Automated Testing
- Production Systems
url: https://www.notion.so/I-Watched-How-Anthropic-s-Engineers-Actually-Write-Code-It-s-Not-What-You-Think-3559fa3b875080d5b3bee06a069a8652
---

This video features [Erik Schluntz](http://www.youtube.com/watch?v=N3ITC-XjGqA), a researcher at [Anthropic](https://www.anthropic.com/), discussing the concept of "**vibe coding**"—fully delegating code generation to AI—and how to implement it responsibly within production environments.

### 1. Key Point Extraction

- **Defining "Vibe Coding":** Erik adopts [Andrej Karpathy's](https://twitter.com/karpathy) definition: fully giving in to the vibes, embracing exponentials, and "forgetting the code even exists" [01:33 Opens in a new window ](http://www.youtube.com/watch?v=N3ITC-XjGqA&t=93). It moves beyond tools like [Cursor](https://www.cursor.com/) or [GitHub Copilot](https://github.com/features/copilot) by removing the human from the line-by-line review bottleneck.

- **The "Exponential" Necessity:** AI task capacity is doubling roughly every seven months. To keep pace with models capable of generating a week's worth of work in seconds, engineers must transition from manual reviewers to high-level system verifiers [03:13 Opens in a new window ](http://www.youtube.com/watch?v=N3ITC-XjGqA&t=193).

- **Responsible Implementation (The PM Role):** Effective vibe coding requires the engineer to act as a **Product Manager for Claude** [10:02 Opens in a new window ](http://www.youtube.com/watch?v=N3ITC-XjGqA&t=602). This involves spending significant time (15–20 minutes) building a comprehensive plan, specification, and context artifact before letting the AI execute [10:56 Opens in a new window ](http://www.youtube.com/watch?v=N3ITC-XjGqA&t=656).

- **Leaf Node Strategy:** To mitigate technical debt, engineers should focus vibe coding on "leaf nodes"—end features or "bells and whistles" that other parts of the system do not depend on [08:20 Opens in a new window ](http://www.youtube.com/watch?v=N3ITC-XjGqA&t=500). Core architecture (the "trunk") should still be deeply understood and human-verified [08:58 Opens in a new window ](http://www.youtube.com/watch?v=N3ITC-XjGqA&t=538).

- **Verifiability over Readability:** Instead of reading every line, engineers should design systems with **verifiable checkpoints**, such as stress tests and easily human-verifiable inputs/outputs, to ensure correctness without needing to understand the underlying implementation [13:19 Opens in a new window ](http://www.youtube.com/watch?v=N3ITC-XjGqA&t=799).

- **Real-World Application:** Anthropic successfully merged a **22,000-line change** to their production reinforcement learning codebase that was heavily AI-written by using targeted leaf-node implementation and rigorous automated stress testing [12:11 Opens in a new window ](http://www.youtube.com/watch?v=N3ITC-XjGqA&t=731).

---

### 2. Source Attribution

 | **Fact / Concept** | **Source / Reference** | 
 | ---- | ---- | 
 | **Vibe Coding Definition** | [Andrej Karpathy](https://twitter.com/karpathy) (referenced at [01:33 Opens in a new window ](http://www.youtube.com/watch?v=N3ITC-XjGqA&t=93)) | 
 | **Building Effective Agents** | [Research Paper/Guide by Erik Schluntz & Barry Zhang](https://www.anthropic.com/research/building-effective-agents) (referenced at [00:24 Opens in a new window ](http://www.youtube.com/watch?v=N3ITC-XjGqA&t=24)) | 
 | **AI Coding Tools** | [Claude](https://claude.ai/), [Cursor](https://www.cursor.com/), [GitHub Copilot](https://github.com/features/copilot), [Claude Code](https://www.google.com/search?q=https%3A%2F%2Fdocs.anthropic.com%2Fen%2Fdocs%2Fagents-and-tools%2Fclaude-code) | 
 | **Compiler Analogy** | Historical distrust of [Compilers/Assembly](https://en.wikipedia.org/wiki/Compiler) (referenced at [04:18 Opens in a new window ](http://www.youtube.com/watch?v=N3ITC-XjGqA&t=258)) | 
 | **Anthropic Research** | [Reinforcement Learning Codebase](https://www.anthropic.com/news/claudes-constitution) (referenced at [12:11 Opens in a new window ](http://www.youtube.com/watch?v=N3ITC-XjGqA&t=731)) | 
 | **Model References** | Claude 3.7 and Claude 4 (internal/upcoming) [09:34 Opens in a new window](http://www.youtube.com/watch?v=N3ITC-XjGqA&t=574) | 

### 3. Summary

The presentation argues that the traditional software engineering bottleneck—human review of every line—is unsustainable in the face of exponential AI growth. By adopting a **"Product Manager" mindset**, focusing on **leaf-node isolation**, and prioritizing **automated verifiability** over manual code reading, teams can drastically increase output (reducing two-week tasks to one day) without compromising production stability.