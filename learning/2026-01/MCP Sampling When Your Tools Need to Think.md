---
complexity: Intermediate
date: 2026-01-25 10:14:00-05:00
id: 2f39fa3b-8750-805a-93d0-ca50df8bcf17
processed_by_ai: true
summary: The article explains MCP Sampling, a feature of the Model Context Protocol
  (MCP) that allows AI tools to delegate complex, non-deterministic "thinking" tasks
  back to the user's connected Large Language Model (LLM). This approach simplifies
  development by removing the need for tools to manage their own LLM dependencies
  or hardcode creative logic, offering greater model flexibility.
title: MCP Sampling When Your Tools Need to Think
tools_mentioned:
- Model Context Protocol (MCP)
- goose
- Claude
- Llama
- Python
- TypeScript
- mcp-council-of-mine
topics:
- MCP Sampling
- Model Context Protocol (MCP)
- AI Tools
- Large Language Models (LLMs)
- Software Architecture
- Creative Content Generation
url: https://www.notion.so/MCP-Sampling-When-Your-Tools-Need-to-Think-2f39fa3b8750805a93d0ca50df8bcf17
---

The article [MCP Sampling: When Your Tools Need to Think](https://www.oreilly.com/radar) explains a specific feature of the **Model Context Protocol (MCP)** called **sampling**. While standard MCP tools allow an AI to call a function (like reading a file), **sampling** allows the tool to call the AI back to perform "thinking" tasks.

### Core Concept: "Flipping the Script"

Instead of the AI simply using a tool, the tool delegates complex, non-deterministic tasks back to the user's connected LLM. This removes the need for developers to:

- Manage separate API keys for their tools.

- Hardcode complex logic for creative tasks.

- Lock users into a specific model (the tool uses whatever LLM the user has already configured).

---

### Key Highlights

- **The "Council of Mine" Example:** A practical implementation where an MCP server simulates a [debate among nine AI personas](https://github.com/block/mcp-council-of-mine). It makes 19 total "sampling" calls to the user's LLM to generate opinions, vote, and synthesize a conclusion—all without the server having its own LLM dependency.

- **When to Use It:** It is ideal for creative content generation (summaries, translations), judgment calls (sentiment analysis), and processing unstructured data.

- **When to Avoid It:** It is not recommended for deterministic math, latency-critical paths, or extremely high-volume processing due to round-trip costs.

### Benefits for Developers

- **Simpler Architecture:** Focus on domain logic and orchestration rather than building a full AI application.

- **Model Flexibility:** The tool automatically adapts if the user switches models (e.g., moving from Claude to a local Llama model via [goose](https://block.github.io/goose/)).

Would you like me to find more technical documentation on implementing the `ctx.sample()` call in Python or TypeScript?