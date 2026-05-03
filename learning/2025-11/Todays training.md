---
complexity: Advanced
date: 2025-11-23
id: 2b49fa3b-8750-8057-a1ed-ed9230a34677
processed_by_ai: true
summary: This document discusses using AI tools like GitHub Copilot and Gemini for
  Angular development and AWS cost review, highlights new Angular 21 features, and
  summarizes a presentation on AI as a major platform shift. It also details advanced
  strategies for automating GitHub issue resolution and code reviews using GitHub
  Actions with various AI agents like Claude, OpenAI Codex, and Cursor.
title: Todays Training
tools_mentioned:
- Angular
- Observable
- GitHub Copilot
- GPT 5.1 mini
- Gemini 3.0
- Signal Forms
- OpenAI
- GitHub
- GitHub Actions
- Claude Code
- OpenAI Codex
- Cursor
- GitHub CLI
- SonarQube
topics:
- Web Development
- Angular
- AWS Cost Management
- AI-assisted Development
- UI/UX Design
- AI Strategy
- Technology Trends
- DevOps
- Automation
- Code Review
- AI Agents
- Version Control
url: https://www.notion.so/Today-s-Training-2b49fa3b87508057a1eded9230a34677
---

# Vibe coding

Used Antigravity to vibe code angular application to review AWS costs. Created a dashboard and breaking down the costs by owners. The Observable code was really good and retrieving the data in parallel as well as solving the CORS issue in development mode using proxy configuration.

Not too happy about the overall implementation and not using SignalStore and defining too much logic in the UI component.

Using github Copilot to move the code over the way I like it while not typing any code. One function at a time. Not quite vibe coding, much more controlled but still not writing code. Because of the iterative and small step approach I am able to use GPT 5.1 mini (so not running out of tokens).

I switched to Gemini 3.0 for UI design once the back end was done. UI is ok and clean, not wow but not bad. Gemini was able to go back to the class getting the data to process the additional data necessary for the UI components I wanted.

# Angular 21

Watched a few videos and listen to some podcasts on the new Angular 21 features. What we mostly care about would be Signal Forms are released in experimental mode. This looks really good.

# Some executive comment on AI Eats the World presentation

Here is the TL;DR of the video "Here's the 90 Slide 'AI Eats the World' Talk in 15 Minutes":

The Gist

Host Nate B. Jones summarizes a 90-slide presentation by tech strategist Benedict Evans (formerly of a16z). The core argument is that AI is a major platform shift—similar to the PC, Web, and Smartphone—that will reshape industries without necessarily "deleting" the technologies that came before it.

**Benedict Evans' Core Arguments**

- **AI is a "Moving Target":** We tend to stop calling technology "AI" once it actually works (e.g., databases, search). Today's LLMs are just the current frontier of a long evolution [01:21 Opens in a new window ](http://www.youtube.com/watch?v=iGvJpBWWGOU&t=81).

- **The "Add, Don't Delete" Pattern:** Just as smartphones didn't eliminate laptops, AI will likely layer on top of existing tech stacks rather than replace them entirely [02:17 Opens in a new window ](http://www.youtube.com/watch?v=iGvJpBWWGOU&t=137).

- **Models are Commodities:** The AI models themselves are becoming commodity inputs rather than competitive moats. The real value lies in how they are applied, not just in having the "best" model [03:16 Opens in a new window ](http://www.youtube.com/watch?v=iGvJpBWWGOU&t=196).

**Nate’s 4 Strategic Takeaways**

- **From Miracle to Utility:** We have crossed the threshold where AI is no longer a research experiment but "inevitable infrastructure." It shouldn't be treated as optional R&D anymore [07:02 Opens in a new window ](http://www.youtube.com/watch?v=iGvJpBWWGOU&t=422).

- **Adoption is Path-Dependent:** Where you choose to deploy AI first (your "beachhead") constrains your future options. Don't just pick random tasks; pick workflows that reorganize information flow and unlock downstream possibilities [08:56 Opens in a new window ](http://www.youtube.com/watch?v=iGvJpBWWGOU&t=536).

- **Buyers Have Leverage:** Since models are commodities, companies should avoid "vendor lock-in." The smart play is to build architectures that let you swap models (arbitrage) based on cost and performance rather than marrying one provider like OpenAI [11:04 Opens in a new window ](http://www.youtube.com/watch?v=iGvJpBWWGOU&t=664).

- **AI "Eats the Org Chart":** AI doesn't just automate tasks; it changes who needs to talk to whom. Roles centered on coordination and synthesis may shrink, while decision-making structures will flatten, similar to how spreadsheets empowered finance teams in the 80s [12:13 Opens in a new window ](http://www.youtube.com/watch?v=iGvJpBWWGOU&t=733).

# How to use Github actions to automatically address issues

Here is the TL;DR of the video "GitHub is the Future of AI Coding (Here's Why)" by Cole Medin:

The Core Argument

Cole Medin argues that while AI will handle most coding in the future, we still need an "orchestration layer" to manage tasks, version control, and track changes. He posits that GitHub (or similar platforms like GitLab) is the perfect solution for this, serving as the central hub where human developers manage a team of AI coding agents.

This is how to use different AI Agents (CLIs I think) to do something similar to Github Copilot Agent and using Github actions to coordinate the steps to run to address Github Issues with varying degrees of human in the loop.

The Strategy: 3 Approaches to AI Integration

Medin demonstrates how to integrate AI coding assistants directly into GitHub Actions to fix issues and review Pull Requests (PRs). He showcases three different "agents" to illustrate three distinct workflow philosophies:

- **Hybrid Approach (Claude Code):**

	- **How it works:** You trigger Claude with a comment (e.g., `@claude-fix`). Claude analyzes the issue and creates a fix in a new branch, but *does not* automatically create a PR. Instead, it posts a comment with a button for the human to click to create the PR.

	- **Philosophy:** Keeps the human in the loop for final validation before the PR stage. [05:08 Opens in a new window](http://www.youtube.com/watch?v=upwbqZ67UBA&t=308)

- **Deterministic Approach (OpenAI Codex):**

	- **How it works:** The workflow logic (YAML) handles the heavy lifting—creating the branch, committing changes, and opening the PR. The AI (Codex) is only called to generate the specific code patch.

	- **Philosophy:** Offers the most control. The AI is restricted to writing code, while the rigid workflow handles the process management. [10:33 Opens in a new window](http://www.youtube.com/watch?v=upwbqZ67UBA&t=633)

- **Autonomous Approach (Cursor):**

	- **How it works:** A "headless" Cursor agent is given full rein. It uses the GitHub CLI to create the branch, write the code, commit the changes, *and* open the PR entirely on its own.

	- **Philosophy:** "Hands-off" automation. The agent handles the entire lifecycle from issue to PR. [13:21 Opens in a new window](http://www.youtube.com/watch?v=upwbqZ67UBA&t=801)

**Key Features & Takeaways**

- **AI Code Reviews:** Medin also sets up workflows where agents review each other's code (e.g., `@claude-review` checks a PR made by Cursor), creating a system of AI peer review. [21:35 Opens in a new window](http://www.youtube.com/watch?v=upwbqZ67UBA&t=1295)

- **Security:** He emphasizes restricting these actions to specific users (e.g., maintainers) so random public users can't trigger your AI agents and drain your API credits. [07:21 Opens in a new window](http://www.youtube.com/watch?v=upwbqZ67UBA&t=441)

- **Cost Efficiency:** For Claude, he demonstrates using a session token from a standard subscription rather than an expensive API key, making the setup much more affordable for individuals. [09:27 Opens in a new window](http://www.youtube.com/watch?v=upwbqZ67UBA&t=567)

- **SonarQube Integration:** He briefly mentions using SonarQube with an MCP (Model Context Protocol) server to let agents run security and quality scans on their own code. [15:13 Opens in a new window](http://www.youtube.com/watch?v=upwbqZ67UBA&t=913)