---
complexity: Intermediate
date: 2026-04-15
id: 3439fa3b-8750-8088-89c2-e87ec341e5d2
processed_by_ai: true
summary: This document defines harness engineering for AI systems, outlining its information,
  execution, and feedback layers. It explores the "Big Model" vs. "Big Harness" debate
  and discusses examples like Cursor 3 and Anthropic Managed Agents, emphasizing the
  strategic importance of designing effective environments for models.
title: Harness Engineering 101
tools_mentioned:
- MCP servers
- LlamaIndex
- Cursor 3
- Anthropic Managed Agents
- OpenAI
- Anthropic
- Linear
- Notion
topics:
- Harness Engineering
- AI Systems
- Large Language Models
- Agent Orchestration
- System Design
url: https://www.notion.so/Harness-Engineering-101-3439fa3b8750808889c2e87ec341e5d2
---

### Core Definition

### Key Components of a Harness

- **Information Layer:** Manages memory, context, and external tools (e.g., [MCP servers](https://modelcontextprotocol.io/introduction)).

- **Execution Layer:** Handles task decomposition, agent collaboration, and error recovery (orchestration).

- **Feedback Layer:** Focuses on evaluation, verification, and observability to improve the system over time.

### The "Big Model" vs. "Big Harness" Debate

- **Big Model Thesis:** Model makers (like OpenAI and Anthropic) argue that as models get smarter, complex scaffolding becomes "dead weight" because the model can handle reasoning natively [06:16 Opens in a new window ](http://www.youtube.com/watch?v=OTjZBjq5FPg&t=376).

- **Big Harness Thesis:** Platforms like [LlamaIndex](https://www.llamaindex.ai/) argue that models are "blank slates" and real-world value comes from the complex workflows and proprietary context provided by the harness [06:45 Opens in a new window ](http://www.youtube.com/watch?v=OTjZBjq5FPg&t=405).

### Notable Examples & Trends

- **[Cursor 3](https://www.cursor.com/)****:** Described as a unified workspace that instantiates harness engineering by allowing multiple agents to run in parallel with a seamless handoff between local and cloud environments [03:18 Opens in a new window ](http://www.youtube.com/watch?v=OTjZBjq5FPg&t=198).

- **Anthropic Managed Agents:** A shift toward "disposable harnesses." Anthropic is building a hosted service where the interfaces stay stable even as the underlying harness evolves to match improving model capabilities [15:45 Opens in a new window ](http://www.youtube.com/watch?v=OTjZBjq5FPg&t=945).

- **Convergence:** The video notes that many AI products (Linear, Notion, etc.) are converging on a similar architecture: a **looping agent harness** that uses tools until a business outcome is reached [14:14 Opens in a new window ](http://www.youtube.com/watch?v=OTjZBjq5FPg&t=854).

### Strategic Takeaways

- **For Developers:** Harness engineering is about leveraging configuration points (like `.mmd` files or sandboxed environments) to improve reliability [08:54 Opens in a new window ](http://www.youtube.com/watch?v=OTjZBjq5FPg&t=534).

- **For Leaders:** Success isn't just about picking the "best" model; it's about designing the best environment (harness) in which those models can operate effectively [19:04 Opens in a new window ](http://www.youtube.com/watch?v=OTjZBjq5FPg&t=1144).

<br/>

<br/>

<br/>

<br/>