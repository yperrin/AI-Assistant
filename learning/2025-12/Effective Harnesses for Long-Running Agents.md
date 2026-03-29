---
title: Effective Harnesses for Long-Running Agents
id: 2c19fa3b-8750-80b3-98cf-cc097cfcb073
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

