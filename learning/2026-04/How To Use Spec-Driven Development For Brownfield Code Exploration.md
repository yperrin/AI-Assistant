---
title: How To Use Spec-Driven Development For Brownfield Code Exploration
id: 33d9fa3b-8750-80de-8e59-f476841a8499
url: https://www.notion.so/How-To-Use-Spec-Driven-Development-For-Brownfield-Code-Exploration-33d9fa3b875080de8e59f476841a8499
---

- 280,000 lines of code

- 10 active developers, and

- Established architecture, patterns, and quality standards.


```plain text

Core Principles

• Code duplication is prohibited.

• You must search for existing functions before creating a new one.

• If no reusable functions exist, a new one may be introduced.

• This rule is especially critical for
  *-data-client (database access layer)
  *-api-client (external HTTP service access layer)
```


```plain text
 Standard API Implementation Structure:

 -Router function with request validation
 -Router calls data client and/or API client directly
 -NO business logic layer/service layer.
 -Simple logic can stay in router; complex logic in data clients
```


```plain text
Backend (BFF) Rules

• Routers should not contain try/catch blocks with “log and rethrow” logic, especially for validation.
• Exception handling is centralized and handled by express.js middleware.
```

- Avoid referencing external standards: It might seem useful to write “follow RFC 9457 for error handling,” but this often causes issues. Your project might only follow a part of that standard, and the LLM won’t know the difference. It will assume full compliance and propose implementations aligned with the entire standard, even if that conflicts with your actual practices. Be explicit about the patterns your project truly uses, not theoretical ones.

- Use accurate terminology: Avoid referring to concepts your system doesn’t actually implement. For example, if you don’t use database transactions, avoid calling a sequence of related operations a “transaction.” That term implies ACID properties, and the assistant will model its implementation accordingly. Stick to precise terms that describe what your system really does to prevent confusion and maintain consistency.

- Writing an effective constitution is not an entry-level task. It requires senior engineers who understand the system’s structure, the team’s working patterns, and the reasoning behind architectural choices.

- Allocate 2-3 days for the initial draft, and continue refining it through real-world use. Most of our revisions involved removing unnecessary generated code rather than adding missing parts. Over time, the constitution becomes a living document that evolves with the system.

- Recognize the close relationship between constitution quality and implementation quality. A weak constitution produces inconsistent results, while a strong one yields predictable, maintainable code with less refactoring effort.

- Use the drafting process to audit your own system. When we built ours, we uncovered legacy patterns that conflicted with current standards. The exercise forced us to identify what was canonical, what was obsolete, and what needed to be enforced moving forward. This process not only refined our constitution but deepened our understanding of the system itself.

- **JIRA: **Maintain high-level hierarchy (Epic → Specification → User Stories) with concise descriptions, expected behaviors, and linked visual assets.

- **Spec Kit:** Takes JIRA inputs and generates the detailed breakdown– around 40–50 functional requirements per spec stored in markdown. A business analyst or equivalent reviewer validates these outputs for accuracy.

- Invest time in the clarification step. Skipping it leads to costly rework later. While Spec generation may take minutes, spending 10–20 minutes clarifying and 30–60 minutes reviewing drastically reduces downstream corrections.

- Assign clear BA ownership. BAs/devs acting as BAs should size features, define JIRA requirements, trigger /Spec Kit.specify, and validate generated breakdowns. Spec Kit enhances BA efficiency but cannot replace human judgment.

- Commit to reviewing all generated requirements. Expect to read 40–50 LLM-generated items per feature. The volume may be tedious, but consistent human review remains essential for maintaining accuracy and context.

- **Simpler method:** Provide a screenshot of the architecture diagram directly as input.

- **Our approach: **Use an agent with project context to convert the diagram into a detailed text description enriched with additional technical context. This produces higher-quality plans.

- API contracts with example request and response formats

- Known integration points such as function names, files, and folders

- Other relevant technical decisions

- Technical alignment with your constitution

- Implementation steps consistent with your architecture

- Integration points mapped to existing code

- Define integration specifications precisely: High-level integration notes such as “modify the data client” or “integrate with publisher service” don’t translate well into actionable plans. Spec Kit requires explicit guidance to connect components correctly. Include exact file names, function names, and interaction patterns so the agent understands how parts of the system communicate.

- Author API contracts yourself. Letting Spec Kit infer contracts introduces inconsistencies, especially in edge cases. Define them in your system design with explicit request and response schemas and error-handling expectations, for example:


```plain text

POST /api/feedbacks

Description
Create a feedback entry and finalize attachments by referencing previously uploaded attachment IDs.

Request (application/json)
{
  "rating": "great",
  "comment": "I like your new AI Adoption Radar page",
  "attachments": [
    "3f786f3e-533b-4030-aa2a-47d03f6f5b62"
  ]
}

Responses
201 Created — empty body
400 Bad Request — invalid payload (e.g., missing rating)
```

- **Provide system design upfront:** Supplying architectural context early allows the plan to align with your actual architecture, minimizing rework. Without this input, Spec Kit generates generic, often suboptimal structures that must be revised later.

- **Recognize that plan quality drives everything:** The accuracy of your plan directly affects task and implementation quality. Teams that already have design documentation should always include it as input so Spec Kit can translate it into code-level implementation details.

- **Invest effort in precise design inputs:** Share clear API contracts with request/response examples, explicit integration points (file names, function names), well-defined acceptance criteria (“endpoint returns 200 with valid data” instead of “endpoint works”), and example outputs for complex logic.

- **Use the plan phase appropriately:** For greenfield features, Spec Kit helps generate structure from scratch. For brownfield projects with existing designs, it converts high-level documentation: architecture diagrams, API contracts into concrete file structures, code modifications, and implementation steps. Spending a few extra minutes refining the plan saves hours during development and review.


```plain text

## Phase 1: Project Setup & Dependencies

- [x] T001 Create git feature branch
      002-sidebar-feedback-integration from main

- [x] T002 [P] Add domain-driven feedback directory structure
      to packages/core/src/feedback/

...


## Phase 2: Foundational Infrastructure

- [x] T006 Create Knex database migration for feedback tables in
      db/migrations/20241021_create_feedback_tables.js

- [x] T007 [P] Create shared feedback types in
      packages/core/src/feedback/
      (FeedbackSubmission, FileAttachment, FeedbackRating)

      REVISED: Types now follow core PEntity pattern
      without Zod dependencies

...

- [x] T010 Setup Express router with Backstage plugin integration in
      packages/backend/src/feedback-management/feedback-router.ts
```

- Add specificity where needed. Some tasks are too general (e.g., "implement data client") and lack method-level detail. Adding specifics like required interfaces or data flows improves implementation quality.

- Check dependency accuracy. Validate that parallel and sequential tasks are ordered correctly to prevent blocked progress.

- Reinforce code reuse. Despite the constitution's reuse policy, tasks often default to "create new." Edit them to emphasize "search, reuse, or extend" existing code where applicable.

- **Refine for minor clarifications: **When task descriptions only need better phrasing, additional context, or slight adjustments, refine through prompts instead of editing manually. Use prompt-based refinements and re-run /Speckit.tasks to regenerate. These refinements persist through future iterations and maintain the workflow’s traceability.

- **Avoid manual edits for repeatability: **Direct edits to tasks.md disrupt the regeneration chain. Manual changes are lost when regenerating from an updated plan. Prompt-based refinements preserve both **intent** and **reproducibility** across iterations.

- **Restart for fundamental misalignments: **When issues stem from deeper layers—like flawed constitution logic, incorrect specs, or weak planning—iteration only compounds the problem. Identify the source phase, fix the root cause, and regenerate downstream artifacts. This ensures consistency between your codebase, specs, and evolving constitution.

- **Use the “third refinement” rule as a signal: **If you find yourself making the **third or fourth** “small” fix, stop. Multiple micro-refinements usually mask a structural issue upstream. Restarting from the right phase saves time, preserves quality, and prevents technical debt from creeping into your generation chain.

- **Enable autonomy within controlled boundaries: **Before task breakdown, the agent implemented entire features in a single pass—producing 10–15 files in 20–30 minutes with no visibility into intermediate logic. After task breakdown, work is segmented into small, reviewable units (typically 1–2 files per task), enabling you to monitor progress, identify issues early, and guide corrections mid-implementation.

- **Maintain workflow integrity through repeatability: **The system is designed for reproducible outputs. Use prompt-based refinements to preserve intent and keep the workflow traceable. Avoid manual edits, as they disrupt the regeneration chain and break downstream consistency.

- **Iterate through the system, not around it: **When refinement is needed, use prompts and regeneration commands rather than manual code changes. This approach ensures that every iteration remains consistent with the original specification and constitution.

- **Leverage the cascade effect for systematic regeneration: **The framework ensures that upstream fixes automatically flow downstream. Fixing the **constitution** regenerates the **plan**, **tasks**, and **implementation**. Fixing the **plan** regenerates the **tasks** and **implementation**. Each correction ripples forward, preserving alignment across all phases—this is the true strength of SpecKit’s design.

- Implement Phase 1 → Review → Validate → Correct if needed

- Proceed to Phase 2, same here: Implement → Review → Validate → Correct if needed

- **Constitution violations:**Even when the constitution has explicit rules, the agent doesn't consistently enforce them during code generation. Our example: Constitution explicitly stated "NO try-catch blocks in route handlers - use global middleware." Yet the agent still added try-catch blocks in router handlers.

- Quality varies unpredictably even within the same feature. It's difficult to predict which parts need careful review versus which are production-ready

- Code reuse issues persist: As covered in Constitution and Tasks sections, the agent prefers creating new code over reusing existing modules. Even with "search first" policies, the agent may still miss reusable code or choose inappropriate patterns. Active review is essential to catch duplication before it ships.

- **Define AI’s role as assistance, not autonomy: **SpecKit provides structured AI support, not replacement for developers. Human judgment remains indispensable, reviews are integral to the process, not signs of failure. As the constitution matures, output quality improves, but oversight is always required.

- **Prioritize model intelligence over prompt complexity: **A strong model with a simple prompt consistently outperforms a simple model with a clever prompt. In our experience, newer models (e.g., *Claude Sonnet 4.5*) deliver markedly higher quality, while older ones show clear degradation.

- **Leverage model intelligence for better outcomes: **Smarter models retain context across long implementations, detect code reuse accurately, adhere to constitutions more consistently, and integrate smoothly with existing codebases. The quality gain easily justifies the higher compute cost.

- **Set realistic expectations for refinement: **Maintaining **60–80%** of generated code post-review is an excellent result. Expect **20–40%** refinement to handle missed edge cases, integration adjustments, over-engineered logic, or constitution rule violations.

- **Adopt early, task-based review practices: **Reviewing outputs task-by-task yields better outcomes than end-of-implementation checks. Early validation prevents issue propagation and ensures tighter integration between AI-generated and existing code.

- **Iterate to correct small deviations: **Re-run the same command to regenerate partial outputs when dealing with limited-scope issues like clarifying specifications, refining edge cases, or adjusting minor design details. Iteration helps align outputs without disrupting downstream phases. Be selective, though. Routine technical maintenance (for example, code cleanups or deprecating old APIs) rarely benefits from Spec Kit. For such tasks, local tools or Copilot’s agent mode are faster and more precise. Focus Spec Kit on medium-to-large features where design structure and context matter.

- **Restart to recover from foundational flaws: **When architectural assumptions, system requirements, or constitution definitions are wrong, iteration magnifies the error chain. Restart the step after manually fixing the last validated .md file, or start the entire process from the beginning if upstream artifacts are compromised. Clean restarts realign design logic and restore phase consistency.

