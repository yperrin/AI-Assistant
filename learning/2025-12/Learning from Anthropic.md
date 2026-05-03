---
complexity: Advanced
date: 2025-12-05 17:51:00-05:00
id: 2c09fa3b-8750-80aa-a334-f317edb02d60
processed_by_ai: true
summary: Anthropic has released new beta features for advanced tool use on Claude,
  including Tool Search, Programmatic Tool Calling, and Tool Use Examples, to improve
  efficiency and reduce context window usage. Additionally, Code Execution with MCP
  is introduced as a method for AI agents to interact with tools more efficiently
  by writing and executing code.
title: Learning from Anthropic
tools_mentioned:
- Claude
- Model Context Protocol
topics:
- AI Agents
- Tool Use
- Context Window Management
- AI Efficiency
- Code Execution
- Model Context Protocol
url: https://www.notion.so/Learning-from-Anthropic-2c09fa3b875080aaa334f317edb02d60
---

Reading about Anthropic formal last 2 posts

### Advanced Tool Use on Claude Developer Platform

The Update:

Anthropic has released three new beta features designed to help AI agents work efficiently with hundreds or thousands of tools by allowing them to discover, learn, and execute tools dynamically.

**Key Features:**

- **Tool Search Tool**

	- **Problem:** Loading definitions for every available tool upfront consumes massive amounts of the context window (e.g., 50+ tools can use 70k+ tokens).

	- **Solution:** Agents can now "search" for tools on-demand. Instead of loading everything, the agent finds and loads only the specific tool definitions needed for the task.

	- **Benefit:** Reduces context usage by ~85% and improves tool selection accuracy.

- **Programmatic Tool Calling**

	- **Problem:** Traditional tool use requires a full model inference pass for every single step and floods the context window with raw intermediate data (like large log files).

	- **Solution:** Claude can write Python scripts to orchestrate multiple tool calls at once. Logic like loops, data filtering, and calculations happen in a code sandbox, and only the final result is sent back to the model.

	- **Benefit:** significantly lowers latency, reduces token costs by ~37%, and keeps the context window clean.

- **Tool Use Examples**

	- **Problem:** JSON schemas define valid structures but fail to explain conventions (e.g., "should the date be YYYY-MM-DD or Nov 5?").

	- **Solution:** Developers can now provide concrete "input examples" directly in the tool definition to demonstrate correct usage patterns.

	- **Benefit:** drastically reduces malformed tool calls, improving accuracy from 72% to 90% on complex tasks.

Getting Started:

These features are available in beta now using the advanced-tool-use-2025-11-20 header.

Would you like to see a specific example of how **Programmatic Tool Calling** orchestrates multiple tools?

### Code Execution with MCP

The Problem:

As AI agents connect to more tools via the Model Context Protocol (MCP), they become inefficient. Loading thousands of tool definitions and passing raw intermediate data (like large spreadsheets) through the model's context window spikes costs and latency.

The Solution:

Code Execution with MCP. Instead of standard tool calling, agents write and execute code to interact with MCP servers. Tools are presented as code APIs (e.g., files in a directory) that the agent can import and use programmatically.

**Key Benefits:**

- **Massive Efficiency:** Agents can filter and process data in the code environment, sending only the final result to the model (e.g., reducing 10,000 rows to 5). This can cut token usage by over 98%.

- **On-Demand Access:** Agents "discover" tools by exploring a filesystem, loading only the definitions they need for the specific task rather than everything upfront.

- **Better Logic:** Complex workflows (loops, error handling) are handled in code rather than through multiple expensive model round-trips.

- **Enhanced Privacy:** Sensitive intermediate data stays in the execution environment and never enters the model's context window.