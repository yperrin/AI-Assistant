---
complexity: Intermediate
date: 2025-12-06 14:52:00-05:00
id: 2c19fa3b-8750-80b3-98cf-cc097cfcb073
processed_by_ai: true
summary: This document outlines a multi-session agentic workflow designed to tackle
  long development tasks by addressing the limitations of single-session agents. It
  proposes an Initializer Agent to set up the environment and a Coding Agent to make
  incremental progress, maintain memory, and ensure a clean state after each session.
title: Effective Harnesses for Long-Running Agents
tools_mentioned:
- JSON
- init.sh
- git
- Puppeteer MCP
topics:
- AI Agents
- Agentic Workflows
- Software Development
- Incremental Development
- Persistent Memory
url: https://www.notion.so/Effective-Harnesses-for-Long-Running-Agents-2c19fa3b875080b398cfcc097cfcb073
---

- **The Problem:** Agents struggle with long tasks because each session starts without memory of previous work, leading to them trying to do too much at once, running out of context, leaving buggy code, or declaring the project complete prematurely.

- **The Solution Components:**

	1. **Initializer Agent:** This specialized first session sets up the environment by creating a structured feature list (in JSON), an `init.sh` script to run the development server, and an initial git commit.

	1. **Coding Agent:** Every subsequent session is prompted to make **incremental progress** by:

		- Reading the progress log (`claude-progress.txt`) and git history to get up to speed.

		- Choosing only one feature at a time from the structured feature list to implement.

		- Testing features end-to-end using browser automation tools (like Puppeteer MCP).

		- Leaving the environment in a "clean state" by committing progress with descriptive messages and updating the progress file.

---