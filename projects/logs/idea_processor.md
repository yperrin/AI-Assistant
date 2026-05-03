# LangGraph Idea Processor: Architectural Choices & Lessons Learned

This document summarizes the core learnings, architectural decisions, and technical hurdles overcome during the development of the `idea_processor` multi-agent workflow (derived from the `langgraph_workflows` experimental sandbox).

## 1. Architectural Paradigm: LangGraph vs. n8n
The fundamental choice to build the idea processor in LangGraph rather than a visual workflow tool like n8n stems from the nature of the task: **indeterministic multi-agent reasoning**. 
- **Workflow vs. Cognitive Runtime:** n8n excels at linear data motion and ETL processes. LangGraph serves as a "cognitive runtime" designed for cyclic, recursive logic where agents must reflect, critique, and iterate.
- **State Management:** LangGraph's reducer-driven state (using `TypedDict` and `operator.add`) ensures that multi-agent updates are appended deterministically. In contrast, standard visual tools often suffer from "silent data loss" when handling complex, concurrent conversational state.

## 2. Multi-Agent Debate & Epistemic Personas
To counteract the inherent sycophancy of LLMs (the tendency to agree with the prompt), the system utilizes an adversarial debate pattern inspired by the "Six Thinking Hats."
- **The Architect vs. The Critic:** The core loop relies on an Architect proposing an implementation and a Critic actively stress-testing it for flaws, logical fallacies, and technical debt.
- **Solving State Amnesia:** Early iterations of the graph suffered from an "infinite loop" where the Architect and Critic would argue the same points endlessly. This was solved by implementing a `decisions_log` in the `IdeaAgentState`. The Architect must now explicitly document resolved constraints, creating a persistent memory that the Critic reviews before generating new dissent.

## 3. Dynamic Routing and Cyclic Refinement
The workflow replaces rigid sequential steps with a dynamic state machine:
- **Refinement over Search:** The initial graph incorrectly used a "Search Loop" (only looping if new web data was needed). This was overhauled into a true "Refinement Loop," allowing the Architect to iteratively refine the design based solely on the Critic's feedback until a `FINAL_APPROVAL` or a `max_loop` condition triggers the final Technical Specification synthesis.
- **Context Engineering:** External rules, specifically the user's `soul.md` preferences, are dynamically injected into the `idea` payload before graph invocation. This forces all agents in the loop to align their proposals with strict ecosystem philosophies (e.g., Markdown storage, local AI usage).

## 4. Model Specialization and Hardware Constraints
Running heavy reasoning models locally requires strict resource management.
- **DeepSeek-R1 for Deep Reasoning:** `deepseek-r1:14b` was selected for the Architect, Critic, and Evaluator nodes because its RL-driven `<think>` phase is vastly superior for complex architectural planning.
- **Gemini for Search:** `gemini-2.5-flash-lite` handles the Researcher node, ensuring fast, cheap data retrieval.
- **VRAM and Timeout Optimization:** Injecting massive contexts (like `soul.md` and full debate logs) into DeepSeek on a 16GB VRAM GPU caused the prompt processing time to skyrocket. This resulted in silent `httpx.RemoteProtocolError` timeouts. The solution required explicitly externalizing model configurations into `.yaml` files and increasing the Ollama connection `timeout` to 600+ seconds while carefully balancing the `num_ctx` bounds.

## 5. Artifact Preservation and Traceability
In a highly non-deterministic system, observability is critical.
- **Complete History:** The routing logic was updated to physically move the entire `run_id` folder (containing `search.md`, `analysis.md`, internal thought iterations, and the final `technical_specification.md`) into a dedicated project directory. 
- **Rationale Capture:** Evaluator nodes that fail to parse output correctly (e.g., due to DeepSeek's `<think>` tags obscuring the final decision) previously resulted in lost evaluation rationales. The script was hardened to unconditionally save an `evaluation_rationale.md` file regardless of the final routing decision, ensuring 100% transparency into why an idea was accepted or rejected.

## Conclusion
The graduation of the `idea_processor` from an experimental LangGraph sandbox into a production tool validates the debate-based consensus model. By combining strictly typed state memory, adversarial prompting, and hardware-optimized local LLM orchestration, the system successfully filters and architects raw ideas into robust, philosophically aligned project specifications.
