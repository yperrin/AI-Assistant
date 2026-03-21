## Plan: LangGraph Multi-Agent Application Implementation

This plan details the phased implementation of a robust, production-ready multi-agent architecture using LangGraph, building from a simple researcher up to an asynchronous, persistent orchestrator with specialized subgraphs (based on the provided requirements).

**Steps**

### [x] Phase 1: Basic Researcher & Summary Graph
1. Define the lightweight `AgentState` schema including tracking for `ArtifactMetadata` (file path references, avoiding large text blobs in state).
2. Implement the `write_markdown_artifact` tool to enforce deterministic file storage and local I/O.
3. Create the **Research Agent** utilizing Gemini for real-time web grounding.
4. Create the **Writer Agent** utilizing local Ollama for parsing the research data and saving to the file system via the artifact tool.
5. Build and compile the base `StateGraph` linking Researcher -> Writer.

### [ ] Phase 2: Persistence Storage Checkpointing
1. Install and configure `langgraph-checkpoint-postgres` (or `langgraph-checkpoint-sqlite` for initial setup/dev).
2. Wrap the graph compilation with the `checkpointer` configuration to enable thread state recovery.
3. Update state invocations to include `thread_id` to test time-travel and memory across invocations.

### [ ] Phase 3: Queue & Asynchronous Request-Reply Pattern
1. Create a job submission/POST endpoint that captures the user prompt, enqueues the job, and immediately returns a `202 Accepted` with a `job_id`.
2. Implement an execution queue (e.g., Redis layer / Background Worker) that executes the persistent LangGraph in an isolated thread.
3. Create a polling/GET endpoint that checks graph checkpoint status retrieving `job_id` progress without synchronous blocking.

### [ ] Phase 4: Super-Orchestrator & Subgraph Refactoring
1. Abstract the graph from Phase 1 into a `researcher_subgraph`. 
2. Create a high-level **Orchestrator Node** using Ollama/Gemini to analyze incoming tasks.
3. Set up the modern `Command` pattern (or Conditional Edges) to route tasks appropriately based on intent (e.g., "RESEARCH" vs "DEBATE").
4. Add the `researcher_subgraph` as a node in the new global workflow.

### [ ] Phase 5: Idea Evaluator Subgraph
1. Implement a new specialized `evaluator_subgraph` integrating Multi-Agent Personality Shaping (MAPS).
2. Create Optimist and Realist (or Council of Experts) dummy nodes executing a Scatter-Gather or Reflection pattern. 
3. Wire the Evaluator Subgraph into the Orchestrator routing layer.
4. Implement a Human-in-the-Loop (`interrupt_before`) stop on the evaluator subgraph for manual user confirmation before final artifact generation.

**Relevant files**
- `src/state.py` — Schema definitions for `AgentState` and `ArtifactMetadata`.
- `src/tools/file_ops.py` — `write_markdown_artifact` implementation.
- `src/graphs/researcher.py` — Phase 1 and 4 researcher sub-graph logic.
- `src/graphs/evaluator.py` — Phase 5 debate/evaluator subgraph logic.
- `src/graphs/orchestrator.py` — Phase 4 Super-Orchestrator routing graph.
- `src/api/server.py` — Phase 3 Asynchronous API routes for Request/Reply queue and Background workers.
- `src/main.py` — Application entry point and checkpointer configuration.

**Verification**
1. **Phase 1 Check**: Run a test query; verify a local `.md` file is generated, and the graph state contains *only* the path.
2. **Phase 2 Check**: Crash/Interrupt the graph manually; resume utilizing the same `thread_id` to ensure execution picks up successfully from the DB.
3. **Phase 3 Check**: Hit the API with a 60-second task. Ensure the API returns `202` within two seconds and that polling returns successful terminal state at ~60s.
4. **Phase 4 & 5 Check**: Send a complex evaluation task and a simple research task. Verify routing logs show the orchestrator correctly commanding the `evaluator_subgraph` and `researcher_subgraph` respectively.

**Decisions**
- **State Management**: Using lightweight reference tracks instead of heavy string states to optimize token usage.
- **Models**: Gemini for external research (requiring API); Ollama for internal logic/writing (local privacy).
- **Architecture**: Enforced asynchronous APIs to prevent 504 Gateway Timeouts during extensive node executions.