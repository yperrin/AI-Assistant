# Idea Processor Tool Documentation

The **Idea Processor** is a LangGraph-based workflow automation tool that processes raw project ideas from your Notion inbox, evaluates their feasibility via a multi-agent debate, and automatically routes them to the appropriate folders.

## Overview
This tool automates the process of idea triage. Instead of manually reviewing every thought synced from Notion, the Idea Processor evaluates each idea, does initial research, drafts a technical specification, and makes an executive "GO / NO-GO" decision.

- **Input:** Markdown files located in `d:\Projects\brain\inbox\ideas\`
- **Outputs:**
  - **APPROVED:** The idea is moved to `d:\Projects\brain\projects\<idea_name>\` alongside a generated `technical_specification.md`.
  - **REJECTED:** The idea is moved to `d:\Projects\brain\inbox\rejected_ideas\`, with the AI's rejection rationale appended to the file.

## Architecture

The workflow uses a cyclic LangGraph state machine consisting of several distinct agent roles:

1. **Researcher:** Uses Google Search (`gemini-2.5-flash-lite`) to find real-world constraints, libraries, and benchmarks related to the idea.
2. **Architect:** Proposes an initial system design based on the idea and research (`deepseek-r1:14b`).
3. **Critic:** Adversarially attacks the Architect's design, pointing out coupling, scalability, or cost issues.
4. **Analysis:** Reviews the Critic's dissent and decides if another iteration of the loop is necessary or if the architecture is ready.
5. **DocWriter:** Synthesizes the finalized architecture into a structured Technical Specification.
6. **Evaluator:** Reviews the final specification against strict feasibility constraints and outputs `FINAL_DECISION: APPROVED` or `FINAL_DECISION: REJECTED`.

## How to Run

1. Ensure your local environment is active:
   ```powershell
   cd d:\Projects\brain\tools\idea_processor
   uv sync
   ```
2. Run the main processing script:
   ```powershell
   uv run python src/main.py
   ```

The script will automatically detect all `.md` files in the inbox, process them sequentially, and output terminal logs detailing the model's decisions.

## State Management (`IdeaAgentState`)
The graph maintains an additive `IdeaAgentState` containing:
- `source_file`: The current file being processed.
- `decisions_log`: A running history of constraints resolved between the Architect and Critic.
- `decision` & `rationale`: The final outcome of the Evaluator node.

## Integration & Future Work
This tool is designed to be chained immediately after the `notion-sync` skill. Once `notion-sync` populates `inbox/ideas/`, the Idea Processor can be triggered to automatically clear the queue.
