In 2026, GitHub Copilot has transitioned from a simple RAG (Retrieval-Augmented Generation) system to a **Stateful Agentic Pipeline**. When you hit "Enter," it doesn't just look at your open files; it orchestrates a multi-step sequence to verify current project state against historical "memories" and explicit constraints.

Here is the internal lifecycle of a Copilot prompt:

---

### Phase 1: Initialization & Policy Loading
Before the system even looks at your code, it establishes the "Rules of Engagement."

* **Instruction File Merging:** Copilot reads the `.github/copilot-instructions.md` (repo-level) and your personal `%USERPROFILE%/copilot-instructions.md` (user-level). It merges these into a system-level prefix that overrides default LLM behavior.
* **Agentic Memory Retrieval:** It queries the **Agentic Memory Layer** for relevant "snippets" of past interactions in this repo. Unlike a chat history, these are validated "facts" (e.g., "This project uses a specific logging pattern") that Copilot has extracted from previous PRs or sessions.
* **Session Context:** If you are in a persistent session (using the "Agents" tab), it loads the **Plan State**—a JSON-like structure tracking which parts of a multi-step task are completed.

### Phase 2: Intent Analysis & Tool Dispatch
Copilot decides *how* it needs to work.
* **Mode Selection:** It determines if it should stay in **Interactive** (chat), **Plan** (architecting), or **Agent** (autonomous execution) mode.
* **MCP Tool Selection:** Using the **Model Context Protocol (MCP)**, it identifies if it needs to call external "tools" (e.g., searching a Jira board, querying a database schema, or performing a web search) to satisfy the prompt.

### Phase 3: Multi-Layered Retrieval (The "Context Engine")
This is the core "filling" of the prompt, pulling from four distinct scopes:

1.  **Local Buffer (Implicit):** Scans the active file and "neighboring tabs" using **Semantic Proximity**. It doesn't just take the whole file; it takes chunks that are mathematically similar to your prompt.
2.  **Structural Context (LSP):** It uses the Language Server Protocol to "walk the graph." If you mention a class, it automatically pulls the definition and signatures of its dependencies.
3.  **Workspace Index (Global):** For repo-wide questions, it queries a local **Vector Database** (stored in your `.git` or a cloud index) to find semantically related code that isn't currently open.
4.  **Reference Verification:** Crucially, for any "Memory" retrieved in Phase 1, Copilot performs **Real-Time Citation Checking**. It verifies that the code referenced in the memory still exists and hasn't been refactored away.



### Phase 4: Assembly & Constraint Engineering
Copilot must now fit all this data into the LLM's context window (e.g., 128k or 200k tokens).
* **Ranking & Pruning:** It scores every piece of context (Instructions > Memory > Active File > Neighboring Tabs > Search Results) and drops the lowest-ranked items.
* **Summarization (Context Compaction):** If the chat history is long, it uses a smaller "distiller" model to summarize the previous 10 turns into a 1-paragraph "Context Summary" to save tokens.
* **Privacy Scrubbing:** A local "Sentinel" layer scans the final payload for PII, hardcoded secrets, or API keys, replacing them with placeholders (e.g., `[SECRET_REDACTED]`).

### Phase 5: Dispatch & Iteration
* **Inference:** The final "Mega-Prompt" is sent to the model (GPT-4o, Claude 3.7, etc.).
* **Output Post-Processing:** If the model returns a "Plan," Copilot updates the **Session State** and may automatically trigger the next retrieval step if it realizes it's missing a dependency found during the first pass.

---

### Comparison of Context Sources
| Source | Persistence | Usage |
| :--- | :--- | :--- |
| **Active File** | Ephemeral | Immediate logic and syntax. |
| **Instructions.md** | Permanent | Architectural constraints & style guides. |
| **Agentic Memory** | 28-day sliding window | Learned patterns (e.g., "We prefer Medallion layers"). |
| **Session History** | Per-task | The "Why" behind the current set of changes. |

How are you currently managing your `.github/copilot-instructions.md`? I can help you draft a set of rules specifically for maintaining independent boundaries in your **Event-Driven** or **Medallion** architectures.