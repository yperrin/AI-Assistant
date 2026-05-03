# Idea Graph Refinement Tasks & Suggestions

## Summary of Current State
1. **Graph Architecture**: The basic workflow is fully established and functional. It uses LangGraph to orchestrate a flow from `Researcher` → `Architect` → `Critic` → `Analysis`.
2. **The "Infinite Loop" / Early Exit Issue**: 
   - A `max_loop` condition is implemented in the `route_discussion` function.
   - However, the loop's logic is flawed. The `Analysis` agent currently decides whether to loop by outputting `SEARCH_REQUIRED`. If no search is needed, the graph ends **immediately**, even if the `Critic` heavily dissented and the `Architect` needs to refine the design. It's currently a "Search Loop" rather than a "Refinement Loop".
3. **State & Memory Amnesia**: 
   - The `IdeaAgentState` keeps track of the conversation history via `messages`, but `current_thought`, `current_dissent`, and `additional_information` are completely **overwritten** in every iteration. 
   - Because there is no persistent log of agreed-upon solutions or "resolved decisions", the `Architect` and `Critic` can easily forget what they agreed on in the previous loop and start arguing about the same points again.
4. **Model Configuration**: 
   - Prompts have been successfully externalized to YAML files (`src/prompts/`). 
   - The `Architect`, `Critic`, and `Analysis` agents are currently hardcoded to use `selected_model: "deepseek-r1:14b"` via Ollama. We have decided to stick with this model for now to leverage its deep, RL-based reasoning (thinking phase), which is better suited for architectural analysis than standard dense models.
   - The `Researcher` continues to use `gemini-2.5-flash-lite`.

## Suggestions for Project Completion
1. **Fix the Routing Logic**: The loop shouldn't just be about whether a web search is needed. It should allow the `Architect` to refine the design based on the `Critic`'s feedback. The graph should route:
   - To `Researcher` if new data is needed.
   - To `Architect` if the design needs refinement but no new external data is required.
   - To `END` (or a documentation node) if the `Critic` gives `FINAL_APPROVAL` or if `max_loop` is hit.
2. **Implement a "Decisions Log"**: Add a `resolved_decisions` list to the `IdeaAgentState`. Before the `Architect` writes a new `current_thought`, they should explicitly list out the constraints from the `Critic` that they have resolved. This acts as an evolving technical spec.
3. **Optimize DeepSeek Configuration**: Ensure the `selected_model: "deepseek-r1:14b"` is optimized for the local 16GB GPU by adjusting timeouts and ensuring the `num_ctx` is balanced to avoid VRAM overflow.
4. **Add a Final Documenter Node**: Create a final node (e.g., `TechSpecWriter`) that takes the final `current_thought`, the `resolved_decisions`, and the research, and writes a polished, final Markdown Technical Specification.

## Task List
- [x] **Task 1: Update State Schema**
  Modify `IdeaAgentState` in `src/state/idea.py` to include a `decisions_log` (list of strings) and an explicit `status` field.
- [x] **Task 2: Overhaul the Routing & Loop Logic**
  Update `route_discussion` in `src/graphs/idea.py` to support routing to the `Architect` for refinement, the `Researcher` for data, or `END`. Ensure `max_loop` safely terminates the graph to a final node.
- [x] **Task 3: Refine Prompts to Use Memory**
  Update `idea_architect.yaml` and `idea_critic.yaml` so the Architect explicitly logs how they solved a dissent, and the Critic checks the `decisions_log` before complaining about an already solved issue.
- [x] **Task 4: Optimize DeepSeek for Local Execution**
  Review and adjust the `timeout` and `num_ctx` settings in the YAML files for `deepseek-r1:14b` to ensure stable performance on the 16GB VRAM GPU.
- [x] **Task 5: Add a Final Documentation Node**
  Create a new node that triggers when the loop finishes to synthesize the entire conversation into a structured `technical_specification.md` file.
