# How to customize GitHub Copilot

**By:** [Yann Perrin](https://clarivate.atlassian.net/wiki/spaces/LSHT/blog/2026/04/12/361301805/How+to+customize+GitHub+Copilot)  
**Date:** April 12, 2026  
**Read Time:** 4 min

As we all learn to use GitHub Copilot, all of us are running our own prompts and succeeding in various degree. This is only the first step, necessary for us to learn to speak AI. But as a team and a company, this produces uneven and non-standard results, which can only sustain us during this learning phase. Eventually we need to agree on what the best practices are and try to follow some kind of standards.

This is one of the reasons why we have been pushing **SpecKit**. It creates consistent results across all teams and it makes it easy for us to review other teams outputs. It also reduces the pressure for us to learn how to prompt, as the prompts are provided by SpecKit. We can then focus on passing the information about the use case and not as much on how to pass the information.

On our way to this standardization, there are 3 entities we really need to focus on.

-----

## Tools available

### Custom Prompts

In the GitHub Copilot ecosystem, "custom prompts" generally fall into two categories that help guide the AI's responses without requiring you to repeatedly type the same context:

  * **Custom Instructions:** These define the *how*. They are "always-on" markdown files (like `.github/copilot-instructions.md`) that dictate coding standards, architectural preferences, or rules that apply to your entire workspace or specific file paths.
  * **Prompt Files:** These define the *what*. Prompt files (e.g., `*.prompt.md`) are reusable, standalone prompts for specific, repetitive tasks that you can invoke manually via a slash command in chat.

### Custom Agents

A custom agent is a highly specialized AI persona tailored for a specific development role. Defined in an `.agent.md` file, a custom agent encapsulates its own set of behaviors, instructions, and, crucially, a **restricted set of tools**. For example, you can create a "Planning Agent" that is only permitted to use read-only search tools, preventing it from accidentally editing your code. Custom agents can also be orchestrated to "hand off" tasks to sub-agents, creating complex, multi-step workflows.

### Skills

Agent skills are encapsulated folders containing instructions (`SKILL.md`), scripts, examples, and resources that an AI agent can load dynamically to perform specialized, repeatable tasks. Unlike custom instructions, which are always active, skills are loaded on demand based on relevance. They allow an AI to compose complex workflows—such as executing a specific Python script to convert image formats or debugging a failed GitHub Actions workflow—without bloating the AI's context window.

-----

## Which one to use when

### When to use Custom Prompts (Instructions & Prompt Files)

  * **Enforcing Project-Wide Standards (Custom Instructions):** You want the AI to *always* know that your project uses React functional components and Tailwind CSS, or you need it to strictly avoid deprecated libraries.
  * **Quick, Repetitive Boilerplate (Prompt Files):** You frequently need to generate a specific type of unit test or README file. A prompt file lets you instantly trigger this exact request with a quick slash command.

### When to use Custom Agents

  * **Role-Based Workflows:** You need a "Code Reviewer" persona to aggressively audit your pull requests for OWASP security vulnerabilities before merging.
  * **Orchestrating Multi-Step Projects:** You are building a complex feature and want a "Planner Agent" to research the codebase and outline the architecture, which then seamlessly hands off to an "Implementation Agent."
  * **Restricting Capabilities for Safety:** You want an AI to analyze your database schema via a Model Context Protocol (MCP) tool, but you explicitly want to deny it the ability to execute write commands.

### When to use Agent Skills

  * **Tasks Requiring External Scripts:** You frequently need the AI to optimize images, so you create a skill that contains a specific script (e.g., Python or bash).
  * **Complex Debugging Protocols:** You want the AI to help debug CI/CD pipelines. You can create a skill that teaches the agent the exact multi-step process to fetch and parse GitHub Actions logs.
  * **Domain-Specific Expertise:** You want to provide the AI with a massive reference document, but you don't want to consume thousands of tokens on every single chat message.

-----

## Summary Comparison

| Component | Level of Context | Persistence | Primary File Type | Key Constraint |
| :--- | :--- | :--- | :--- | :--- |
| **Custom Prompt** | Conversation | Ephemeral | `.prompt.md` | Context window size |
| **Custom Agent** | User/Workspace | Persistent Persona | `.agent.md` | Tool permissions |
| **Agent Skill** | System/Repository | Modular Capability | `SKILL.md` (folder) | Metadata accuracy |

| Use Case | Best Approach | Reasoning |
| :--- | :--- | :--- |
| Explaining a one-off legacy function | Custom Prompt | Low repetition; specific context. |
| Ensuring all code follows security rules | Custom Agent | Persistent persona; tool restriction. |
| Running a multi-step AWS deployment | Agent Skill | Procedural logic; script execution. |
| Comparing two specific contracts | Custom Prompt | One-off analysis; transactional. |
| Acting as a React expert for a team | Custom Agent | Shared expertise; role-based guidance. |
| Formatting a standard Weekly Status Report | Agent Skill | Repeatable format; defined procedure. |

-----

## Where do we go from here

There are many public repositories that host these items; [awesome copilot](https://www.google.com/search?q=https://github.com/github-copilot/awesome-copilot) is a popular one. You can also adapt [Claude ones](https://github.com/anthropics/anthropic-cookbook) as the format is standard.

Ideally, we will create our own Clarivate repository for custom prompts/agents/skills to share across projects. This will promote standards and good practices while facilitating onboarding for new recruits.