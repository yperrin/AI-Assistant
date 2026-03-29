---
title: MCP Sampling When Your Tools Need to Think
id: 2f39fa3b-8750-805a-93d0-ca50df8bcf17
url: https://www.notion.so/MCP-Sampling-When-Your-Tools-Need-to-Think-2f39fa3b8750805a93d0ca50df8bcf17
---

### Core Concept: "Flipping the Script"

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

