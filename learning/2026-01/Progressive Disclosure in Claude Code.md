---
title: Progressive Disclosure in Claude Code
id: 2e79fa3b-8750-80c3-8064-e842fa1a304a
url: https://www.notion.so/Progressive-Disclosure-in-Claude-Code-2e79fa3b875080c38064e842fa1a304a
---

### **The Core Problem: Context Bloat**

- **Massive Token Burn:** Sending thousands of tokens of tool schemas with every request [01:41 Opens in a new window ](http://www.youtube.com/watch?v=DQHFow2NoQc&t=101).

- **Degraded Performance:** Large contexts can reduce the model's accuracy [02:03 Opens in a new window ](http://www.youtube.com/watch?v=DQHFow2NoQc&t=123).

- **Higher Costs:** Constant re-sending of tool definitions is expensive [02:37 Opens in a new window ](http://www.youtube.com/watch?v=DQHFow2NoQc&t=157).

### **The Solution: Progressive Disclosure**

- **On-Demand Discovery:** Instead of seeing all tools, the model uses a "tool search tool" to find what it needs only when it needs it [01:35 Opens in a new window ](http://www.youtube.com/watch?v=DQHFow2NoQc&t=95).

- **Massive Efficiency:** Anthropic reported an **85% reduction** in token usage [01:48 Opens in a new window ](http://www.youtube.com/watch?v=DQHFow2NoQc&t=108), while Cloudflare saw a **98.7% reduction** by using a TypeScript-based sandbox approach [06:23 Opens in a new window ](http://www.youtube.com/watch?v=DQHFow2NoQc&t=383).

- **Bash & Filesystem:** The new paradigm treats the filesystem and [Bash](https://www.youtube.com/watch?v=DQHFow2NoQc) as the primary interface. Tools are stored as files, and memory is handled via simple markdown files (like `CLAUDE.md`) rather than complex vector databases [11:18 Opens in a new window ](http://www.youtube.com/watch?v=DQHFow2NoQc&t=678).

### **Practical Application in Claude Code**

- **Skills Directory:** You can create a `skills` folder where each file contains "front matter" (a brief description) that is disclosed to the model. The full content is only loaded if the model decides it needs that specific skill [11:42 Opens in a new window ](http://www.youtube.com/watch?v=DQHFow2NoQc&t=702).

- **Experimental MCP CLI:** There is an experimental flag in Claude Code to enable tool search capabilities, allowing the agent to manage vast libraries of MCP servers without hitting context limits [07:38 Opens in a new window ](http://www.youtube.com/watch?v=DQHFow2NoQc&t=458).

