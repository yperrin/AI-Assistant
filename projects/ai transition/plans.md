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
  * Copilot Spaces
  * Jira skill/MCP and then get PO involved
* GitHub Agentic Workflows: This feature acts as an evolution of CI/CD, allowing you to write automation goals in plain Markdown instead of complex YAML. These workflows deploy agents directly within GitHub Actions to autonomously triage incoming issues, investigate the root causes of CI pipeline failures, and perform repository maintenance
* We need a plan with timelines or Milestones

# Q2 Plans
## SDD - Pallavi
1. OpenSpec analysis
2. (05/06) Document the rollout process
   1. how to setup github repo + automatic code reviews, instructions file
      1. Document existing code (technical)
      2. Developer on-boarding documentation
   2. how to setup the sa repo + workspace
      1. document the code repos
      2. document user guide
      3. document architecture?
   3. choose speckit + openspec based on maturity
      1. provide how to get started for each one
         1. Include wiki steps
         2. Include training video
         3. Include any templates
      2. Set system context
      3. Ownership of the steps to make sure we can be productive
   4. Create a plan for rollout out SDD
      1. New page for status of the rollout per team
      2. have way for teams to document experience (first one, after 6 months)
3. (05/14) Do a tech/talk and Learning channel to advertise the process and choices
4. (06/01) Start on Jira bi-directional synching
5. (06-02) Start on trip to India - Need agenda

## With Rosa - Yann, Pallavi
1. identify the next batch of teams to implement the Rollout
2. Kick off meeting to get it started
   1. <progress value="50" max="100"></progress> Chem Struct 
   2. <progress value="50" max="100"></progress> Off-X 
   3. <progress value="0" max="100"></progress> Commercial Items (Suketa and Ingrid) 
   4. <progress value="0" max="100"></progress> Ontology (Prashant)
   5. <progress value="0" max="100"></progress> PDI

## Training - Yann
1. (05/08) Training Session
   1. Custom prompts/agents/skills. How to include them in a global scope.
   2. Introduce Awesome copilot. Dangers of using on-line scripts.
   3. Introduce a common repo.
   4. Pre-populate with the ones we have
   5. Encourage people to add their own + code review
2. (05/04 - 05/20) Yann - Level 7 

## Devops
1. (Shilpa) Give a list of repos already have RestAssured implement as part of PR.