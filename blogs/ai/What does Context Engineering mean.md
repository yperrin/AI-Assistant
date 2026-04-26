# What does Context Engineering mean

**By:** [Yann Perrin](https://clarivate.atlassian.net/wiki/spaces/LSHT/blog/2026/04/04/328466521/What+does+Context+Engineering+mean)  
**Date:** April 04, 2026  
**Read Time:** 4 min

At the basis of it, context engineering means being able to give the right LLM all the information it needs and no more. Everything else we may discuss is basically how to achieve this.

Context engineering becomes the primary way to solve **hallucinations**. By providing a "source of truth" within the context, you move the model from relying on its fuzzy training memory to performing "open-book" exams where it can cite specific, up-to-date information.

In addition to providing the right information, it is also providing the right information at the right cost. If you always use the most expensive models, even for the most basic tasks, you will be burning through tokens very quickly.

In summary, it boils down to two things:
1. **What information is provided to the LLM:** Prompts + additional information (MCP, RAG, tools, attachments, etc.).
2. **What model is used to process the information.**

---

## Recommendations for Model Selection

While choice of model often comes down to personal habit, different families have unique strengths:
* **Claude and Gemini:** Better at creating UIs.
* **Gemini:** Better at handling massive contexts and multi-modal tasks.
* **Claude and GPT:** Strongest at writing documentation.

### Revised Model Recommendations (April 2026)

| Use Case | Recommended Model | Reasoning |
| :--- | :--- | :--- |
| **Code review (Local)** | GPT-5.3-Codex | Best value at 1x multiplier for catching regressions. |
| **Requirements (Medium)** | Claude Sonnet 4.6 | Best reasoning-to-cost ratio for architectural alignment. |
| **Requirements (Large)** | Claude Opus 4.6 | 3x multiplier is worth it for spotting conflicts in massive repos. |
| **Implementation (Medium)** | Claude Sonnet 4.6 | Highly reliable for feature work and respecting boundaries. |
| **Implementation (Large)** | Claude Opus 4.6 | Best for multi-file refactoring and complex active memory. |
| **User Doc (Medium)** | Gemini 3 Flash | 0.33x multiplier; efficient for technical-to-prose transformation. |
| **User Doc (Large)** | Gemini 3.1 Pro | Massive context window to "read" entire large-scale repos. |
| **Tech Doc (Medium)** | Claude Sonnet 4.6 | Superior at explaining the *intent* behind decisions. |
| **Tech Doc (Large)** | Claude Opus 4.6 | Essential for mapping Medallion or Data Mesh interactions. |

---

## Recommendations for Passing Information

### 1. Inefficient Document Ingestion
* **The Challenge:** Raw PDFs/images contain formatting overhead that inflates token counts.
* **The Solution:** Convert documents to **Markdown** before uploading to reduce the token footprint by up to 20x.

### 2. Conversation Sprawl
* **The Challenge:** Long threads (20–40 turns) fill the context window with "croft," leading to "LLM psychosis" or drifted results.
* **The Solution:** Start fresh conversations every 10–15 turns. Separate *Information Gathering* from *Execution*.

### 3. Redundant API/Agent Calls
* **The Challenge:** Re-sending system prompts and tool definitions every time is expensive.
* **The Solution:** Use **Prompt Caching** to get up to a 90% discount on repeated content.

### 4. Poor Web Research Habits
* **The Challenge:** Native web search in some models can be token-heavy and slow.
* **The Solution:** Use **MCP (Model Context Protocol)** connectors like Perplexity for faster, structured citations with fewer tokens.

### 5. Architectural Laziness in Agents
* **The Challenge:** Giving an agent the "full codebase" when it only needs a specific slice.
* **The Solution:** * Use **RAG** to index references and provide only relevant chunks.
    * **Scope context** to provide the minimum viable info for the specific task.