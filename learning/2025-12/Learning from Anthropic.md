---
title: Learning from Anthropic
id: 2c09fa3b-8750-80aa-a334-f317edb02d60
url: https://www.notion.so/Learning-from-Anthropic-2c09fa3b875080aaa334f317edb02d60
---

### Advanced Tool Use on Claude Developer Platform

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

### Code Execution with MCP

- **Massive Efficiency:** Agents can filter and process data in the code environment, sending only the final result to the model (e.g., reducing 10,000 rows to 5). This can cut token usage by over 98%.

- **On-Demand Access:** Agents "discover" tools by exploring a filesystem, loading only the definitions they need for the specific task rather than everything upfront.

- **Better Logic:** Complex workflows (loops, error handling) are handled in code rather than through multiple expensive model round-trips.

- **Enhanced Privacy:** Sensitive intermediate data stays in the execution environment and never enters the model's context window.

