---
title: Todays Training
id: 2b49fa3b-8750-8057-a1ed-ed9230a34677
url: https://www.notion.so/Today-s-Training-2b49fa3b87508057a1eded9230a34677
---

# Vibe coding

# Angular 21

# Some executive comment on AI Eats the World presentation

- **AI is a "Moving Target":** We tend to stop calling technology "AI" once it actually works (e.g., databases, search). Today's LLMs are just the current frontier of a long evolution [01:21 Opens in a new window ](http://www.youtube.com/watch?v=iGvJpBWWGOU&t=81).

- **The "Add, Don't Delete" Pattern:** Just as smartphones didn't eliminate laptops, AI will likely layer on top of existing tech stacks rather than replace them entirely [02:17 Opens in a new window ](http://www.youtube.com/watch?v=iGvJpBWWGOU&t=137).

- **Models are Commodities:** The AI models themselves are becoming commodity inputs rather than competitive moats. The real value lies in how they are applied, not just in having the "best" model [03:16 Opens in a new window ](http://www.youtube.com/watch?v=iGvJpBWWGOU&t=196).

- **From Miracle to Utility:** We have crossed the threshold where AI is no longer a research experiment but "inevitable infrastructure." It shouldn't be treated as optional R&D anymore [07:02 Opens in a new window ](http://www.youtube.com/watch?v=iGvJpBWWGOU&t=422).

- **Adoption is Path-Dependent:** Where you choose to deploy AI first (your "beachhead") constrains your future options. Don't just pick random tasks; pick workflows that reorganize information flow and unlock downstream possibilities [08:56 Opens in a new window ](http://www.youtube.com/watch?v=iGvJpBWWGOU&t=536).

- **Buyers Have Leverage:** Since models are commodities, companies should avoid "vendor lock-in." The smart play is to build architectures that let you swap models (arbitrage) based on cost and performance rather than marrying one provider like OpenAI [11:04 Opens in a new window ](http://www.youtube.com/watch?v=iGvJpBWWGOU&t=664).

- **AI "Eats the Org Chart":** AI doesn't just automate tasks; it changes who needs to talk to whom. Roles centered on coordination and synthesis may shrink, while decision-making structures will flatten, similar to how spreadsheets empowered finance teams in the 80s [12:13 Opens in a new window ](http://www.youtube.com/watch?v=iGvJpBWWGOU&t=733).

# How to use Github actions to automatically address issues

- **Hybrid Approach (Claude Code):**

	- **How it works:** You trigger Claude with a comment (e.g., `@claude-fix`). Claude analyzes the issue and creates a fix in a new branch, but *does not* automatically create a PR. Instead, it posts a comment with a button for the human to click to create the PR.

	- **Philosophy:** Keeps the human in the loop for final validation before the PR stage. [05:08 Opens in a new window](http://www.youtube.com/watch?v=upwbqZ67UBA&t=308)

- **Deterministic Approach (OpenAI Codex):**

	- **How it works:** The workflow logic (YAML) handles the heavy lifting—creating the branch, committing changes, and opening the PR. The AI (Codex) is only called to generate the specific code patch.

	- **Philosophy:** Offers the most control. The AI is restricted to writing code, while the rigid workflow handles the process management. [10:33 Opens in a new window](http://www.youtube.com/watch?v=upwbqZ67UBA&t=633)

- **Autonomous Approach (Cursor):**

	- **How it works:** A "headless" Cursor agent is given full rein. It uses the GitHub CLI to create the branch, write the code, commit the changes, *and* open the PR entirely on its own.

	- **Philosophy:** "Hands-off" automation. The agent handles the entire lifecycle from issue to PR. [13:21 Opens in a new window](http://www.youtube.com/watch?v=upwbqZ67UBA&t=801)

- **AI Code Reviews:** Medin also sets up workflows where agents review each other's code (e.g., `@claude-review` checks a PR made by Cursor), creating a system of AI peer review. [21:35 Opens in a new window](http://www.youtube.com/watch?v=upwbqZ67UBA&t=1295)

- **Security:** He emphasizes restricting these actions to specific users (e.g., maintainers) so random public users can't trigger your AI agents and drain your API credits. [07:21 Opens in a new window](http://www.youtube.com/watch?v=upwbqZ67UBA&t=441)

- **Cost Efficiency:** For Claude, he demonstrates using a session token from a standard subscription rather than an expensive API key, making the setup much more affordable for individuals. [09:27 Opens in a new window](http://www.youtube.com/watch?v=upwbqZ67UBA&t=567)

- **SonarQube Integration:** He briefly mentions using SonarQube with an MCP (Model Context Protocol) server to let agents run security and quality scans on their own code. [15:13 Opens in a new window](http://www.youtube.com/watch?v=upwbqZ67UBA&t=913)

