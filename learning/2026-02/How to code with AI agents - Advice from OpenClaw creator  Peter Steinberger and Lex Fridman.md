---
complexity: Advanced
date: 2026-02-15 14:51:00-05:00
id: 3089fa3b-8750-80d5-96df-f75fc042915c
processed_by_ai: true
summary: This document outlines key insights for senior developers and leaders on
  working with AI agents, emphasizing a shift from complex orchestrations to concise
  commands, leading agents like a team, and focusing human review on critical business
  logic. It also covers technical philosophies like local CI, main-only commits, and
  voice-first interaction, alongside the importance of "system empathy" and infusing
  agents with personality via a `soul.md` file.
title: How to code with AI agents - Advice from OpenClaw creator  Peter Steinberger
  and Lex Fridman
tools_mentioned:
- soul.md
topics:
- AI Agents
- Software Development
- Team Leadership
- Developer Workflow
- System Design
- Prompt Engineering
- Continuous Integration
url: https://www.notion.so/How-to-code-with-AI-agents-Advice-from-OpenClaw-creator-Peter-Steinberger-and-Lex-Fridman-3089fa3b875080d596dff75fc042915c
---

### Key Takeaways for Senior Developers & Leaders:

- **The Agentic Trap & Zen Place**: Steinberger describes an evolution from short, simple prompts to overly complex multi-agent orchestrations (the "trap"), eventually arriving at a "Zen" state of using concise, high-level commands [02:45 Opens in a new window ](http://www.youtube.com/watch?v=wKy1_KLcxcs&t=165).

- **Leading Agents Like a Team**: Drawing on his management background, he argues that working with agents requires letting go of rigid control over internal implementation (e.g., specific variable names or formatting) to focus on high-level architecture and intent [10:34 Opens in a new window ](http://www.youtube.com/watch?v=wKy1_KLcxcs&t=634).

- **"Ship Code I Don't Read"**: He emphasizes that for "boring" boilerplate (data shifting, UI alignment), he often doesn't read every line, focusing his human review on critical areas like database interactions and business logic [01:35 Opens in a new window ](http://www.youtube.com/watch?v=wKy1_KLcxcs&t=95).

- **System Empathy**: A core skill for the modern engineer is empathizing with the agent's context. This means understanding that they start every session fresh with no knowledge of your project, requiring you to provide clear pointers and guardrails within their context limits [16:26 Opens in a new window ](http://www.youtube.com/watch?v=wKy1_KLcxcs&t=986).

- **Soul.md and Delight**: To differentiate from "dry" enterprise software, Steinberger infuses his agents with personality. He uses a `soul.md` file to define core values and tone, even allowing agents to modify their own "soul" to reflect their evolving role in the project [25:08 Opens in a new window ](http://www.youtube.com/watch?v=wKy1_KLcxcs&t=1508).

### Technical Philosophy:

- **Local CI & Main-Only**: He favors a "YOLO" but pragmatic workflow: no develop branch, always commit to main, and rely on fast local CI to keep the feedback loop tight [13:12 Opens in a new window ](http://www.youtube.com/watch?v=wKy1_KLcxcs&t=792).

- **Voice-First Interaction**: Much of his agentic interaction is done via voice input, treating the process more like a conversation than a manual coding task [14:07 Opens in a new window ](http://www.youtube.com/watch?v=wKy1_KLcxcs&t=847).