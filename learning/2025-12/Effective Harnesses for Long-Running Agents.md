---
complexity: Intermediate
date: 2025-12-06 14:52:00-05:00
id: 2c19fa3b-8750-80b3-98cf-cc097cfcb073
processed_by_ai: true
summary: This document describes a two-fold solution for AI agents, specifically the
  Claude Agent SDK, to manage complex, long-running tasks across multiple limited
  context windows. It involves an Initializer Agent for setup and a Coding Agent for
  incremental progress, leveraging structured feature lists and git history.
title: Effective Harnesses for Long-Running Agents
tools_mentioned:
- Claude Agent SDK
- Puppeteer MCP
- Git
topics:
- AI Agents
- Software Development
- Context Management
- Incremental Progress
- Task Management
url: https://www.notion.so/Effective-Harnesses-for-Long-Running-Agents-2c19fa3b875080b398cfcc097cfcb073
---

This Anthropic blog post discusses a two-fold solution to enable AI agents (specifically the [Claude Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview)) to effectively handle complex, long-running tasks across multiple limited context windows:

- **The Problem:** Agents struggle with long tasks because each session starts without memory of previous work, leading to them trying to do too much at once, running out of context, leaving buggy code, or declaring the project complete prematurely.

- **The Solution Components:**

	1. **Initializer Agent:** This specialized first session sets up the environment by creating a structured feature list (in JSON), an `init.sh` script to run the development server, and an initial git commit.

	1. **Coding Agent:** Every subsequent session is prompted to make **incremental progress** by:

		- Reading the progress log (`claude-progress.txt`) and git history to get up to speed.

		- Choosing only one feature at a time from the structured feature list to implement.

		- Testing features end-to-end using browser automation tools (like Puppeteer MCP).

		- Leaving the environment in a "clean state" by committing progress with descriptive messages and updating the progress file.

The key insight is providing agents with the artifacts and processes (like feature lists and git history) that help them quickly understand the state of the work, much like effective human software engineers.

---

Would you like a deeper dive into either the **Initializer Agent** or the **Coding Agent**'s specific behaviors?