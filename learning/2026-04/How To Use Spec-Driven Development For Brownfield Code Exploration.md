---
complexity: Advanced
date: 2026-04-09 17:14:00-04:00
id: 33d9fa3b-8750-80de-8e59-f476841a8499
processed_by_ai: true
summary: This document provides a candid account of implementing Spec Kit for AI-assisted
  engineering in a brownfield enterprise project, detailing a step-by-step workflow
  from constitution definition to code implementation. It highlights challenges, best
  practices, and lessons learned for integrating AI tools into mature systems while
  maintaining quality and architectural integrity.
title: How To Use Spec-Driven Development For Brownfield Code Exploration
tools_mentioned:
- Spec Kit
- GitHub Copilot
- Cursor
- Claude code
- Claude Sonnet 4.0
- Claude Sonnet 4.5
- Jira
- Azure DevOps
- Figma
- Lucid
- Knex
- Express.js
- Amplitude
- npm
- dotnet
topics:
- AI-assisted engineering
- Spec-driven development
- Brownfield projects
- Software development lifecycle
- Code quality
- Large Language Models (LLMs)
- System architecture
- Project management
- Software engineering best practices
url: https://www.notion.so/How-To-Use-Spec-Driven-Development-For-Brownfield-Code-Exploration-33d9fa3b875080de8e59f476841a8499
---

Spec Kit is one of the most ambitious frameworks for bringing order to AI-assisted engineering.  In our earlier post on **[spec driven development](https://www.epam.com/insights/ai/blogs/inside-spec-driven-development-what-githubspec-kit-makes-possible-for-ai-engineering)**, we discussed its potential to close long-standing gaps in AI-assisted workflows by enforcing project standards, feature-level context, enforced decomposition for manageable scope, and review gates for quality control.

But execution is where theory meets resistance. Spec Kit’s documentation is a strong starting point, with clear videos, detailed guides, and prescriptive steps that let you deploy it within hours. You can get it running in hours. The challenge starts when you leave the sandbox. Like the Animal → Dog → Labrador examples in OOP tutorials, the examples teach syntax, not production software engineering.

The gap isn't in the documentation, but context and real expertise. Clean examples work beautifully for greenfield projects, but most teams operate on brownfield codebases shaped by months of evolving decisions, developers making tradeoffs, competing patterns, and non-negotiable quality standards.

This post reflects our journey through that challenge. It isn’t a polished success story, but a candid account of what worked, what didn’t, and how we made Spec Kit fit a live production system where quality couldn’t be compromised.

**About our project & the testing ground**

Our team manages an AI productivity portal that’s been in production for over a year and a half, supporting cross-company AI adoption. It’s a mature system with:

- 280,000 lines of code

- 10 active developers, and

- Established architecture, patterns, and quality standards.

This is mid-complexity enterprise software with all the typical compromises and accumulated decisions that come with real-world systems.

The test case for Spec Kit was adding a user feedback feature to our portal.

**The feature:** feedback button triggers popup form, user selects reaction + adds text + optional file attachment, submit sends email to support team. It had to integrate with existing usage tracking (Amplitude) and follow our established patterns.

This tested whether Spec Kit's workflow could handle brownfield integration. If it could handle a feature with UI components, external integrations, and quality constraints, that would validate the approach works beyond tutorials - on actual enterprise projects with real constraints.

**Using spec kit for feature development: A step by step brownfield implementation**

Through hands-on implementation, we learned that Spec Kit demands both human oversight and upfront effort. It won’t deliver full end-to-end automation. Each phase calls for distinct attention and expertise.

But when you know where to focus, the effort compounds into real results. Here’s what we learned and implemented across each phase:

**Step 1 - Constitution: Project standards and conventions**

The first step in Spec Kit adoption is to build your Constitution — the foundational document that encodes your project’s DNA. It defines the standards, conventions, and architectural principles that shape how your codebase behaves and how the AI assistant operates within it.

You can generate a starting version by running <u>**/Spec Kit.constitution**</u>. This gives you a quick overview of your project’s stack, naming conventions, surface-level patterns, and basic patterns of code analysis.

PS: The assistant prioritizes .md files within your repository - READMEs, documentation, markdown content. These heavily shape your constitution. Outdated docs will create outdated constitution rules. Clean them up before you generate your constitution.

Our first version looked complete on the surface — visually clean and technically sound — but it missed the deeper, project-specific rules that guided real implementation. We refined it through several iterations and identified four categories of rules that made the biggest impact for our feedback feature. Your project’s needs may differ, but these are a solid place to start:

**1. Define your code reuse policy**

Our team quickly learned that “an agent prefers writing over reading.” Its default behavior is to produce new code instead of reusing existing components. During implementation, it even created a new “email-service” directory with duplicate implementation rather than referencing the existing code that was already doing it (and moreover, had the same name). To prevent this, add explicit reuse instructions in your Constitution:

Core Principles


```plain text

Core Principles

• Code duplication is prohibited.

• You must search for existing functions before creating a new one.

• If no reusable functions exist, a new one may be introduced.

• This rule is especially critical for
  *-data-client (database access layer)
  *-api-client (external HTTP service access layer)
```

With this rule in place, Spec Kit now generates task lists that include a “search for existing functionality” step, prompting the agent to look for reusable code before implementation. The results are noticeably better, though not flawless. The agent may still occasionally miss reusable code or reuse inappropriate patterns, so developers need to continue validating outputs.

**2. Document YOUR project architecture**

LLM training data includes countless projects using service layers, middleware patterns, and common architectural approaches. Without explicit instructions, the agent naturally defaults to these common conventions instead of your project’s specific architecture.

In our case, the UI application doesn’t use a service layer because it contains minimal business logic. Our convention is to avoid creating services for entities. However, since router→ service is a widely used pattern, the AI-driven Spec Kit automatically introduced service layers during generation.

We had to correct this by clearly documenting our architecture in the Constitution. This is just one instance; your project may have its own patterns that need similar clarification. Here is how we introduced it into our architecture:

Solution Architecture Patterns


```plain text
 Standard API Implementation Structure:

 -Router function with request validation
 -Router calls data client and/or API client directly
 -NO business logic layer/service layer.
 -Simple logic can stay in router; complex logic in data clients
```

**3. Define your project's forbidden patterns**

We’ve covered what to include in your constitution: code reuse policies and architectural decisions. Equally important is documenting what not to do. Some patterns must be explicitly prohibited to maintain consistency. During implementation, we learned this the hard way.

For example, our constitution clearly stated “No try-catch blocks in route handlers. Use global middleware instead,” yet the agent still added try-catch blocks during implementation.

Here is how we defined our forbidden pattern for try-catch blocks:

Backend (BFF) Rules


```plain text
Backend (BFF) Rules

• Routers should not contain try/catch blocks with “log and rethrow” logic, especially for validation.
• Exception handling is centralized and handled by express.js middleware.
```

**Common pitfalls**

Two critical lessons about what NOT to include in your constitution:

- Avoid referencing external standards: It might seem useful to write “follow RFC 9457 for error handling,” but this often causes issues. Your project might only follow a part of that standard, and the LLM won’t know the difference. It will assume full compliance and propose implementations aligned with the entire standard, even if that conflicts with your actual practices. Be explicit about the patterns your project truly uses, not theoretical ones.

- Use accurate terminology: Avoid referring to concepts your system doesn’t actually implement. For example, if you don’t use database transactions, avoid calling a sequence of related operations a “transaction.” That term implies ACID properties, and the assistant will model its implementation accordingly. Stick to precise terms that describe what your system really does to prevent confusion and maintain consistency.

**Key takeaways**

- Writing an effective constitution is not an entry-level task. It requires senior engineers who understand the system’s structure, the team’s working patterns, and the reasoning behind architectural choices.

- Allocate 2-3 days for the initial draft, and continue refining it through real-world use. Most of our revisions involved removing unnecessary generated code rather than adding missing parts. Over time, the constitution becomes a living document that evolves with the system.

- Recognize the close relationship between constitution quality and implementation quality. A weak constitution produces inconsistent results, while a strong one yields predictable, maintainable code with less refactoring effort.

- Use the drafting process to audit your own system. When we built ours, we uncovered legacy patterns that conflicted with current standards. The exercise forced us to identify what was canonical, what was obsolete, and what needed to be enforced moving forward. This process not only refined our constitution but deepened our understanding of the system itself.

**Step 2 - Spec: Requirements and acceptance criteria**

The Specification phase defines what you want to build before deciding how to build it.

Running <u>**/Spec Kit.specify**</u> generates structured specifications based on a consistent template, breaking each feature into clear user stories and acceptance criteria. This documentation forms the foundation for subsequent technical planning and implementation.

**💡Important note: **Spec Kit does not natively integrate with project management or design tools such as Jira, Azure DevOps, Figma, or Lucid. Although integration is technically possible through an MCP server, it is not supported out of the box. Spec Kit functions independently through its .md file structure, which means synchronization with other systems must be managed manually.

Another critical consideration is the knowledge and context gap. Much of your project knowledge already exists in tools like Jira, ADO Wiki, or Confluence. Spec Kit does not have direct access to this information, so it is your responsibility to connect or transfer the relevant context into its workflow to ensure completeness. Here's how to build the spec:

**1. Prepare a strong feature brief as input**

High-quality specifications begin with clear inputs. Provide all relevant assets that describe the feature: design screens (we used annotated screenshots), supporting documentation, and any existing materials such as JIRA stories or functional outlines.

The specification phase forces structured thinking before implementation. Time spent here prevents confusion, rework, and misalignment later in the pipeline.

**2. Review and refine spec output**

Spec Kit typically generates 3-4 user stories per specification, with roughly 10 functional requirements per user story - resulting in 40-50 total functional requirements per spe division of responsibility:

- **JIRA: **Maintain high-level hierarchy (Epic → Specification → User Stories) with concise descriptions, expected behaviors, and linked visual assets.

- **Spec Kit:** Takes JIRA inputs and generates the detailed breakdown– around 40–50 functional requirements per spec stored in markdown. A business analyst or equivalent reviewer validates these outputs for accuracy.

Spec Kit isn’t a substitute for tracking and planning tools; it’s a complement. Tools like JIRA stay focused on what they do best: status, releases, and visibility, while Spec Kit takes over the heavy lifting of detailed, markdown-based execution breakdowns.

**5. Size your features based on scope and complexity**

From our experience, Spec Kit performs best on features that a single developer can complete in 1-5 days. Its default 3-4 user story structure suits low- to medium-complexity work, where 40-50 functional requirements provide sufficient granularity. The grouping may not always be perfect, but it generally follows a logical pattern.

For larger features, the BA should divide them into multiple specifications before creating corresponding JIRA items. Each specification follows the same format, gets its own JIRA entry, and can be developed in sequence or in parallel. This is where human judgment matters most– determining logical split points and coordinating interdependencies across specs.

**💡Quality warning: **Spec Kit CAN handle larger features or epics, but output quality degrades. Feeding large, complex features into one specification often leads to incomplete or fragmented results, which weakens downstream implementation quality.

**Key takeaways**

- Invest time in the clarification step. Skipping it leads to costly rework later. While Spec generation may take minutes, spending 10–20 minutes clarifying and 30–60 minutes reviewing drastically reduces downstream corrections.

- Assign clear BA ownership. BAs/devs acting as BAs should size features, define JIRA requirements, trigger /Spec Kit.specify, and validate generated breakdowns. Spec Kit enhances BA efficiency but cannot replace human judgment.

- Commit to reviewing all generated requirements. Expect to read 40–50 LLM-generated items per feature. The volume may be tedious, but consistent human review remains essential for maintaining accuracy and context.

**Step 3 - Plan: Technical design and architecture**

Plan phase translates requirements into technical implementation approach. In this step, the Spec Kit analyzes your codebase, pulls context from the constitution, and produces a plan.md file that lists implementation details, file-level changes, and integration points.

💡For small repositories or simple features, the assistant can generate a solid plan from the feature description alone. However, in large, mature systems like ours, with a 1.5-year-old, 180k-line codebase you’ll need to supply a detailed system design as input.

Here's our workflow for doing that effectively:

**1. Provide architectural context upfront**

Designing the architecture for a mid-size feature typically requires one to two days of senior engineering effort. Do not expect the LLM to handle this level of architectural work, LLMs are not yet capable of making design tradeoffs or enforcing project-wide principles.

In our workflow, solution architects create detailed architecture diagrams using Lucid as part of the design phase. When using these diagrams as Spec Kit input, two methods work well:

- **Simpler method:** Provide a screenshot of the architecture diagram directly as input.

- **Our approach: **Use an agent with project context to convert the diagram into a detailed text description enriched with additional technical context. This produces higher-quality plans.

This text-based description becomes one of the inputs for /Spec Kit.plan, alongside the feature specification. Beyond architecture diagrams, also include:

- API contracts with example request and response formats

- Known integration points such as function names, files, and folders

- Other relevant technical decisions

**2. Execute the plan command with full context**

Once all architectural inputs are prepared, run /Spec Kit.plan to generate the implementation plan. The agent combines your constitution, specification, and design context to produce a detailed blueprint for development.

You’ll receive:

- Technical alignment with your constitution

- Implementation steps consistent with your architecture

- Integration points mapped to existing code

Spec Kit also generates a folder and file tree showing what will be created, modified, or removed. This level of visibility helps developers immediately understand the full scope of upcoming changes.

The plan is a guide, not an absolute rulebook. During implementation, the assistant may still modify files beyond the original scope, but the file tree remains a reliable indicator of design intent.

**3. Review the plan collaboratively**

Review the generated plan with architects and senior developers. Verify that the architecture is consistent, no unauthorized layers are introduced, and integration points are accurate. Flag any ambiguous file actions such as “modify utils” for manual verification, especially for new integrations, new data models, or newly exposed API contracts that require architect or tech lead oversight.

Once validated, lock the plan and treat <u>**plan.md**</u> as a contract between architects and devs. After this review, proceed to /Spec Kit.tasks knowing that the structure will hold during execution.

**Common pitfalls**

- Define integration specifications precisely: High-level integration notes such as “modify the data client” or “integrate with publisher service” don’t translate well into actionable plans. Spec Kit requires explicit guidance to connect components correctly. Include exact file names, function names, and interaction patterns so the agent understands how parts of the system communicate.

- Author API contracts yourself. Letting Spec Kit infer contracts introduces inconsistencies, especially in edge cases. Define them in your system design with explicit request and response schemas and error-handling expectations, for example:

API — Create Feedback


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

This level of specificity helps Spec Kit generate more accurate implementation plans.

**Key Takeaways**

- **Provide system design upfront:** Supplying architectural context early allows the plan to align with your actual architecture, minimizing rework. Without this input, Spec Kit generates generic, often suboptimal structures that must be revised later.

- **Recognize that plan quality drives everything:** The accuracy of your plan directly affects task and implementation quality. Teams that already have design documentation should always include it as input so Spec Kit can translate it into code-level implementation details.

- **Invest effort in precise design inputs:** Share clear API contracts with request/response examples, explicit integration points (file names, function names), well-defined acceptance criteria (“endpoint returns 200 with valid data” instead of “endpoint works”), and example outputs for complex logic.

- **Use the plan phase appropriately:** For greenfield features, Spec Kit helps generate structure from scratch. For brownfield projects with existing designs, it converts high-level documentation: architecture diagrams, API contracts into concrete file structures, code modifications, and implementation steps. Spending a few extra minutes refining the plan saves hours during development and review.

**Step 4 - Tasks: Breaking down implementation**

Tasks phase transforms implementation plans into concrete, ordered, executable steps. Run <u>/Spec Kit.tasks</u> on your validated plan to generate the breakdown. Each task includes explicit dependencies, scoped file paths, and clear objectives - typically 1-2 files per task. Here is our workflow:

**1. Run /Spec Kit.tasks on the approved plan**

The command parses your validated plan.md and outputs a checklist grouped by phase (data model, client, API, tests, etc.). Each task specifies exact file paths, ordered dependencies, and implementation scope.

implementation-plan.md


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

**2. Review the task list**

We identified several repeatable pitfalls:

- Add specificity where needed. Some tasks are too general (e.g., "implement data client") and lack method-level detail. Adding specifics like required interfaces or data flows improves implementation quality.

- Check dependency accuracy. Validate that parallel and sequential tasks are ordered correctly to prevent blocked progress.

- Reinforce code reuse. Despite the constitution's reuse policy, tasks often default to "create new." Edit them to emphasize "search, reuse, or extend" existing code where applicable.

**3. Decide when to restart and when to refine**

The **Tasks** phase is where most refinements surface. Issues originating from the constitution, spec, or plan often become visible as file-level inconsistencies or unclear task logic. The key decision is whether to iterate or restart:

- **Refine for minor clarifications: **When task descriptions only need better phrasing, additional context, or slight adjustments, refine through prompts instead of editing manually. Use prompt-based refinements and re-run /Speckit.tasks to regenerate. These refinements persist through future iterations and maintain the workflow’s traceability.

- **Avoid manual edits for repeatability: **Direct edits to tasks.md disrupt the regeneration chain. Manual changes are lost when regenerating from an updated plan. Prompt-based refinements preserve both **intent** and **reproducibility** across iterations.

- **Restart for fundamental misalignments: **When issues stem from deeper layers—like flawed constitution logic, incorrect specs, or weak planning—iteration only compounds the problem. Identify the source phase, fix the root cause, and regenerate downstream artifacts. This ensures consistency between your codebase, specs, and evolving constitution.

- **Use the “third refinement” rule as a signal: **If you find yourself making the **third or fourth** “small” fix, stop. Multiple micro-refinements usually mask a structural issue upstream. Restarting from the right phase saves time, preserves quality, and prevents technical debt from creeping into your generation chain.

**Key Takeaways**

- **Enable autonomy within controlled boundaries: **Before task breakdown, the agent implemented entire features in a single pass—producing 10–15 files in 20–30 minutes with no visibility into intermediate logic. After task breakdown, work is segmented into small, reviewable units (typically 1–2 files per task), enabling you to monitor progress, identify issues early, and guide corrections mid-implementation.

- **Maintain workflow integrity through repeatability: **The system is designed for reproducible outputs. Use prompt-based refinements to preserve intent and keep the workflow traceable. Avoid manual edits, as they disrupt the regeneration chain and break downstream consistency.

- **Iterate through the system, not around it: **When refinement is needed, use prompts and regeneration commands rather than manual code changes. This approach ensures that every iteration remains consistent with the original specification and constitution.

- **Leverage the cascade effect for systematic regeneration: **The framework ensures that upstream fixes automatically flow downstream. Fixing the **constitution** regenerates the **plan**, **tasks**, and **implementation**. Fixing the **plan** regenerates the **tasks** and **implementation**. Each correction ripples forward, preserving alignment across all phases—this is the true strength of SpecKit’s design.

**Step 5 - Implementation: Translating design into working system**

Implementation executes the task breakdown and generates code. The agent generates working code for straightforward implementations, with basic structure following patterns from constitution and existing code. You get progress visibility through task execution, and the agent can execute local CLI commands (npm, dotnet, etc.) when needed.

Here is the workflow:

**1. Execute in controlled phases**

Run <u>**/Spec Kit.implement**</u> task-by-task or phase-by-phase rather than all at once. The command supports selective execution - specific tasks, entire phases, or everything.

Our checkpoint approach:

- Implement Phase 1 → Review → Validate → Correct if needed

- Proceed to Phase 2, same here: Implement → Review → Validate → Correct if needed

This transforms overwhelming complexity into manageable increments.

**2. Fix AI assistant deviations**

As we already highlighted, the AI assistant doesn't always follow instructions - even when constitution, plan, and tasks are explicit. Watch for these deviations:

- **Constitution violations:**Even when the constitution has explicit rules, the agent doesn't consistently enforce them during code generation. Our example: Constitution explicitly stated "NO try-catch blocks in route handlers - use global middleware." Yet the agent still added try-catch blocks in router handlers.

**Task and plan deviations: **Spec Kit doesn't guarantee and validate that implementation actually follows the task plan. The agent may add features not in the plan, skip planned steps, update files not mentioned in plan or implement differently than designed.

**3. Handle unpredictable code quality**

Code quality varies significantly - some generated code is excellent, some is subtly wrong. This adds to the review challenge:

- Quality varies unpredictably even within the same feature. It's difficult to predict which parts need careful review versus which are production-ready

- Code reuse issues persist: As covered in Constitution and Tasks sections, the agent prefers creating new code over reusing existing modules. Even with "search first" policies, the agent may still miss reusable code or choose inappropriate patterns. Active review is essential to catch duplication before it ships.

**4. Switch to AI-assisted engineering**

Given the deviations and quality challenges above, the workflow shifts after initial  implementation. The agent handled the mechanical work - the structured, predictable code generation. Now you handle the critical work - the refinement, quality, and architectural alignment.

This is where you take control back from the AI. Your role becomes similar to a technical lead reviewing a junior developer's implementation: review the implementation carefully, identify what needs correction, then use AI tools (GitHub Copilot, Cursor, Claude code or similar) to help implement those corrections efficiently.

YOU drive the decisions, AI assists with execution. The agent got you basic code - the final step requires human judgment, but you can still use AI tools to accelerate refinements.

**Key Takeaways**

- **Define AI’s role as assistance, not autonomy: **SpecKit provides structured AI support, not replacement for developers. Human judgment remains indispensable, reviews are integral to the process, not signs of failure. As the constitution matures, output quality improves, but oversight is always required.

- **Prioritize model intelligence over prompt complexity: **A strong model with a simple prompt consistently outperforms a simple model with a clever prompt. In our experience, newer models (e.g., *Claude Sonnet 4.5*) deliver markedly higher quality, while older ones show clear degradation.

- **Leverage model intelligence for better outcomes: **Smarter models retain context across long implementations, detect code reuse accurately, adhere to constitutions more consistently, and integrate smoothly with existing codebases. The quality gain easily justifies the higher compute cost.

- **Set realistic expectations for refinement: **Maintaining **60–80%** of generated code post-review is an excellent result. Expect **20–40%** refinement to handle missed edge cases, integration adjustments, over-engineered logic, or constitution rule violations.

- **Adopt early, task-based review practices: **Reviewing outputs task-by-task yields better outcomes than end-of-implementation checks. Early validation prevents issue propagation and ensures tighter integration between AI-generated and existing code.

**What we learned across all phases & steps**

Let’s start with the good news: Spec Kit won’t replace developers, designers, or architects anytime soon. What it changes is how they work. It automates mechanical, structured tasks and leaves humans to make the contextual, architectural, and design judgments that AI still can’t replicate. After running multiple features through all five phases, five consistent lessons emerged:

**The 80/20 rule for automation**

Across every phase, Spec Kit handled about 80% of the structured work automatically. The remaining 20% demanded human input: decisions involving trade-offs, domain context, and project-specific nuances. Spec Kit’s job is to handle predictable, repetitive work so engineers can focus on context, judgement, project-specific nuance, logic, quality, and intent. The best outcomes came when we treated it as a collaboration, not delegation.

**The cumulative quality problem**

Each phase independently delivered roughly 80 percent accuracy. But when you chain five phases together, small imperfections multiply:

**0.8 × 0.8 × 0.8 × 0.8 × 0.8 = 0.33**

By the end of implementation, cumulative quality would drop to about 33 percent without intermediate checks. This is why review gates are not bureaucratic hurdles, but essential data-backed safeguards. Every phase requires validation before moving forward; otherwise, early inaccuracies propagate through the workflow and erode final output quality

**Review fatigue is an unglamorous truth**

Reviewing AI-generated Markdown files is necessary but cognitively tiring. Unlike code or documentation, AI-written text appears grammatical and seemingly reasonable but demands constant scrutiny for factual and architectural accuracy.

Naturally, your focus will drift, and errors might start building in plausible wording.

The best mitigation is structured review—treat each file like a code review, rotate reviewers, and take short breaks. The mental workload doesn’t disappear; it shifts from writing to validation.

We've stated multiple times that engineers must read each and every .md file carefully. We highlighted this with the cumulative quality problem math. But here's what we haven't said: reading AI-generated text is mentally exhausting.

Your focus naturally drifts. The prose is grammatical and seemingly reasonable, but validating it requires sustained concentration. It's not like reading code where patterns jump out. It's not like reading documentation where you're learning. It's validating plausible-sounding text for correctness - and that's cognitively draining.

What to do? How did our team handle this? Honestly - we don't have a perfect solution. Take breaks. Stay sharp. Treat it like code review, not casual reading. Rotate who does reviews if possible. But be prepared: it will be boring. This is the tax you pay for AI assistance - the mental effort shifts from typing to validation, but it doesn't disappear.

**Model Quality is a productivity decision, not a cost choice**

Model intelligence directly influences the 80/20 ratio. Upgrading from Claude Sonnet 4.0 to 4.5 cut our rework time nearly in half. Smarter models hold context through longer implementations, detect code reuse better, follow constitution rules more strictly, and make stronger architectural choices.

The economics are clear: a more capable model costs more per token but saves exponentially more engineering hours. Using cheaper, outdated models often means spending the difference fixing and refactoring their output.

**Fixing output: when to iterate vs when restart**

Through multiple implementations, we identified two effective strategies for correcting workflow errors in Spec Kit:

- **Iterate to correct small deviations: **Re-run the same command to regenerate partial outputs when dealing with limited-scope issues like clarifying specifications, refining edge cases, or adjusting minor design details. Iteration helps align outputs without disrupting downstream phases. Be selective, though. Routine technical maintenance (for example, code cleanups or deprecating old APIs) rarely benefits from Spec Kit. For such tasks, local tools or Copilot’s agent mode are faster and more precise. Focus Spec Kit on medium-to-large features where design structure and context matter.

- **Restart to recover from foundational flaws: **When architectural assumptions, system requirements, or constitution definitions are wrong, iteration magnifies the error chain. Restart the step after manually fixing the last validated .md file, or start the entire process from the beginning if upstream artifacts are compromised. Clean restarts realign design logic and restore phase consistency.

Rule of thumb: After three or four iterative attempts on the same artifact, stop fixing and restart the phase. Fresh context is often the cleanest path to restoring code and architectural integrity.

**What’s next? Build reliable engineering features with Spec Kit**

Spec Kit isn’t magic. It’s a serious engineering tool that rewards preparation, not blind trust. With the right setup: clear constitution, strong architecture, and task-level execution, it makes AI-assisted development measurable, predictable, and scalable. The real shift isn’t in removing humans but in redefining their role. Spec Kit gives AI the structure it needs to behave like part of the team rather than a code generator. It turns good engineering discipline into repeatable, AI-ready workflows.

If you’re exploring Spec-Driven Development or looking to get started, the AI/Run team is here to help you design that foundation and guide your adoption journey.