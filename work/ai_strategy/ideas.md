# Overall Ideas
## Development Teams
* Get the whole team to go through AI levels
* We need a document with approved practices
  * SKills/custom agents/prompts library - in a common repo
  * Hooks
  * Semantic Code Search
  * Global vs local configuration
  * Sub-agents
  * Multi-Agent Orchestration (Subagents): Advanced setups stop treating Copilot as a single entity and instead use a parent-child architecture. A primary orchestrator agent can use the runSubagent tool to delegate specific subtasks to specialized custom agents
  * Evaluate OpenSpec for long term and brownfield SDD
* Training VS Code + GitHub copilot
  * Local vs CLI vs Cloud
  * Memory

## Non-Development Teams (PO, DM, Architects)
* Involve SAs to rollout to other projects
* How to involve POs and DMs in the process
* Involve devops to clean the pipeline + GitHub
  * PR run integrations tests
  * Automate UAT deployments
  * Automate creating QAP report + release notes
  * Automate production deployments
* We need a document with approved practices
  * How to involve people in the team
  * Do we want to institutionalize n8n?
  * How should we form teams for new projects
* Review manual processes and reduce the amount we have to do (Automation)
* We need a list of things to evaluate
  * Copilot Spaces - so far not good enough - Pallavi ran out of space quickly with her project
  * Jira skill/MCP and then get PO involved
  * Code reviews - currently run on PRs - what can we do to improve this? Is there a risk of AI "agreeing" with each other?
      * Need to provide some training courses for developers on how to conduct code reviews
      * review intent and plan rather than actual code changes
      * Automate architecture review of the code - cross project architecture considerations
      * find tools to help with local code reviews
         * https://dev.to/heraldofsolace/the-best-ai-code-review-tools-of-2026-2mb3
         * https://github.com/tirth8205/code-review-graph
    
* GitHub Agentic Workflows: This feature acts as an evolution of CI/CD, allowing you to write automation goals in plain Markdown instead of complex YAML. These workflows deploy agents directly within GitHub Actions to autonomously triage incoming issues, investigate the root causes of CI pipeline failures, and perform repository maintenance

