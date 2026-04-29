# Proposal for Transition to AI-Driven Software Development

## Level 1 - Enable Code Reviews for Each Repo

**Why:** Easy to turn on and will start exposing developers to AI feedback. This may also improve quality. Setup a ruleset for the develop branch (or any other branch developers merge their PR to).

**How:** Link to the parent page on [how to do this](https://clarivate.atlassian.net/wiki/spaces/LSHT/pages/116394279)

## Level 2 - Make Sure All Developers Are Setup with Github Copilot

Make sure all the developers have access to github and github copilot, No instructions should be needed here, If they don't, you need to raise a Service Now ticket.

You can review employee status on [Github Copilot usage](https://app.powerbi.com/reportEmbed?reportId=11334176-60a8-451b-933e-8c6112a42f3b&autoAuth=true&ctid=127fa96e-00b4-429e-95f9-72c2828437a4).

Have the developers install Github copilot extension in the editor of their choice. If no extension is possible, they can use the [github copilot CLI](https://docs.github.com/en/copilot/how-tos/set-up/install-copilot-cli).

Here are some instructions:
- Install [in VS Code](https://clarivate.atlassian.net/wiki/spaces/~jerome.gauthier@clarivate.com/pages/96150578)
- Install [in IntelliJ](https://clarivate.atlassian.net/wiki/spaces/PTI/pages/140731668)
- Install [in Visual Studio Code](https://clarivate.atlassian.net/wiki/spaces/~jerome.gauthier@clarivate.com/pages/96150578)

## Level 3 - Create an Instructions File for Each Repo

**Why:** This is the base instructions all agents will be using to understand the project. It will improve the quality of the output generated and smooth out the transition. It will be used by Github Copilot, Github Copilot Agent, Github Spec Kit. You will commit the file and this will ensure consistency also for all code generated in this repository.

**How:** You need to follow these steps:
- Create a new file located in `.github/copilot-instuctions.md`
- You can ask the Github Copilot Chat (Agent mode) to populate the file for you
- Review the content, modify it and add your own information.

Example of a prompt: This will generate the content based on an existing code base. Feel free to add the instructions for the things you already know (like follow standard Java coding practices)

`
    You are an expert pair programmer for a senior development team. Your goal is to write the contents for a copilot-instructions.md file. This file will guide all developers on using GitHub Copilot consistently.
    Describe the core technology stack (e.g., React, Node.js, Python/Django, SQL database) and the main purpose of the application. Include any critical architectural decisions (e.g., using Redux for state, microservices architecture).
    Then a description of the project architecture, framework and dependencies
    Then include information about the project structure and the purpose behind each folder.
    Specify Style and Conventions:
    - Naming: What casing to use for variables, functions, and files (e.g., camelCase for JS variables, snake_case for Python).
    - Commenting: How verbose comments should be. Should it use JSDoc, type hints, or simple inline comments?
    - Code Structure: Preferred import ordering, function size limits, and use of arrow functions vs. regular functions.
    - Testing: What testing framework is used (e.g., Jest, Pytest) and the preferred structure for test files.
    Finally include instructions for good coding practices which follow TDD and clean code.
`

Or on the shorter side
`Your task is to "onboard" this repository to Copilot coding agent by adding a .github/copilot-instructions.md file. This file must contain information describing how a coding agent, seeing the repository for the first time, can work most efficiently. Instructions must be no longer than 2 pages.`

## Level 4 - Analyze Requirements

The goal is not necessarily for you to complete a requirement review using AI but it is a way for us to learn what AI can do and share [our results with the rest to the teams](https://clarivate.atlassian.net/wiki/spaces/LSHT/pages/116397059).

Each team, to complete this level, will need to use the **Ask Model with GitHub Copilot** on the client (or you can ask the agent in GitHub.com site if you prefer) to review a requirement for you and provide some feedback/analysis.

We will be using a prompt engineering method called "iterative prompting" (so the copilot on the client might be a little easier) and ask more than one question about the requirement.

Here are some suggestions, please try your own. I am creating some very simple ones on purpose. You will need to copy the text from the Jira into the context for GitHub to know what you are talking about.
- Review the requirement and ask me any questions you need in order to fully understand it.
- How long do you think it would take to implement this requirement and how many people should I assign to it?

Make sure you complete level 3 on the repository you are trying this on, as it will guide the agent to give you better answers. If you are getting bad answers, think about whether you should be updating the instructions file so you get better answers.

Also you may want to try the same process with different models...

Once you are done, [update this wiki page](https://clarivate.atlassian.net/wiki/spaces/LSHT/pages/116397059) (I provided a template) to share your experience with the rest of the team and check it to see what other people came up with.

## Level 5 - Implementation Plan

Each team, to complete this level, will need to use the **Ask Model with GitHub Copilot** on the client (or you can ask the agent in [GitHub.com](http://GitHub.com) site if you prefer) to review a requirement for you and provide an implementation plan.

We will be using a prompt engineering method called "iterative prompting" (so the copilot on the client might be a little easier) and ask more than one question about the requirement.

Here are some suggestions, please try your own. I am creating some very simple ones on purpose. You will need to copy the text from the Jira into the context for GitHub to know what you are talking about.
- Review the requirement and propose a plan on how I should implement it.
- How long do you think it would take to implement this requirement?

Make sure you complete level 3 on the repository you are trying this on, as it will guide the agent to give you better answers. If you are getting bad answers, think about whether you should be updating the instructions file so you get better answers.

Also you may want to try the same process with different models...

Once you are done, [update this wiki page](https://clarivate.atlassian.net/wiki/spaces/LSHT/pages/116397065) (I provided a template) to share your experience with the rest of the team and check it to see what other people came up with.

## Level 6 - Plan Mode

Once you have a non trivial requirement, you really should be creating an implementation plan using [GitHub Copilot Plan mode](https://code.visualstudio.com/docs/copilot/agents/planning). Read the documentation, a plan.md file is created in your local machine. So you can review it as you build it and change it. When an implementation is complex, it becomes difficult to manage the context over the implementation. A plan can break it down into smaller manageable steps with less pressure on the size of the context needed to implement each step. You can also save the plan with the repo and mark each phase completed as you move through the implementation. It also makes it possible for you to stop and start again later (when your meetings are over).

## Level 7 - Custom Prompts

As we become more adept at writing prompts, instead of re-writing them from scratch, we can create a library of useful ones for the project and share them with the rest of the team. GitHub Copilot includes a way for us to store those [custom prompts](https://code.visualstudio.com/docs/copilot/customization/prompt-files) with our code repository. This promotes good and consistent practices for the project and is the first way we will start re-using knowledge within the project.

## Suggestions for the Next Levels

- Create documentation for existing projects + push to confluence
- Delegate a coding task to the cloud agent
- Create an architecture review agent
- Create a skill which will run unit test cases, integration test cases and provide feedback on potential next action items (not enough code coverage for currently modified files, quick code review)

## Suggested Next Steps

- Identify a team that will drive the process and create a list of use cases AI will be able to help. An initial list of use cases is:
  - Parse AWS log and create actionable outcomes
  - Analyze a requirement and provide review + estimation + breakdown (maybe spec kit)
  - Use AI agent to implement directly small requirements
  - Use script to prepare and create Pull requests
  - After feature is completed, update the product documentation
  - Analyze backlog and identify bugs easy to fix
- Team will then train and offer support to the rest of the teams on how to implement those use cases
- Create a list of useful MCP servers and how to use them
- Create a list of recipes (prompts) or MCP servers that can help us achieve our goals

---
