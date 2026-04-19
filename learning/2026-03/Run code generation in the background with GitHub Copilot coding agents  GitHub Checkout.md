---
complexity: Intermediate
date: 2026-03-31 21:36:00-04:00
id: 3359fa3b-8750-8023-af2b-e682630ec580
processed_by_ai: true
summary: This document outlines key features and updates for an agent system, emphasizing
  cloud-based execution via GitHub Actions, advanced model selection (e.g., Claude
  3.5 Sonnet), integrated quality and security checks, custom agent definitions, and
  multi-interface support. It also details seamless transitions between cloud and
  local environments and hints at future capabilities like private drafting and non-coding
  tasks.
title: Run code generation in the background with GitHub Copilot coding agents  GitHub
  Checkout
tools_mentioned:
- GitHub Actions
- Claude 3.5 Sonnet
- Claude 3 Opus
- Copilot Code Review
- GitHub CodeQL
- GitHub Advisory Database
- GitHub.com
- VS Code
- GitHub CLI
topics:
- AI Agents
- Cloud Computing
- Software Development
- Code Quality
- Security Scanning
- GitHub Actions
url: https://www.notion.so/Run-code-generation-in-the-background-with-GitHub-Copilot-coding-agents-GitHub-Checkout-3359fa3b87508023af2be682630ec580
---

### Key Features & Updates

- **Background Execution:** Unlike local agents, it runs in the cloud (using GitHub Actions as the compute layer). You can trigger a task, close your laptop, and return later to a completed Pull Request [02:20 Opens in a new window ](http://www.youtube.com/watch?v=S1ch_6fjp5M&t=140).

- **Model Selection:** Users (Pro and Pro Plus) can now choose their underlying model, such as **Claude 3.5 Sonnet** or **Claude 3 Opus** for more complex reasoning [01:34 Opens in a new window ](http://www.youtube.com/watch?v=S1ch_6fjp5M&t=94).

- **Integrated Quality & Security:** * **Self-Review:** The agent uses **Copilot Code Review** to critique its own code before you ever see it [03:34 Opens in a new window ](http://www.youtube.com/watch?v=S1ch_6fjp5M&t=214).

	- **Security Scanning:** Includes automated **GitHub CodeQL** scanning (for vulnerabilities), **Secret Scanning**, and dependency checks via the **GitHub Advisory Database** [04:15 Opens in a new window ](http://www.youtube.com/watch?v=S1ch_6fjp5M&t=255).

- **Custom Agents:** You can define specific "personalities" or workflows (e.g., a "Performance Optimizer") by adding agent definitions directly into an `.github/agents` directory in your repo [05:43 Opens in a new window ](http://www.youtube.com/watch?v=S1ch_6fjp5M&t=343).

- **Multi-Interface Support:** Trigger and monitor agents via **GitHub.com** (the "Agents" panel), **VS Code**, or the **GitHub CLI** [01:12 Opens in a new window ](http://www.youtube.com/watch?v=S1ch_6fjp5M&t=72).

### Seamless Transitions

- **Cloud to Local:** You can use the CLI to "tail" cloud logs or "check out" the agent's branch to continue its work on your local machine [08:45 Opens in a new window ](http://www.youtube.com/watch?v=S1ch_6fjp5M&t=525).

- **Local to Cloud:** Conversely, you can start a task in your terminal and "delegate" it to the cloud to free up your local environment [09:52 Opens in a new window ](http://www.youtube.com/watch?v=S1ch_6fjp5M&t=592).

### Future Roadmap

- **Private Drafting:** Soon, agents will be able to work privately without immediately opening a PR, allowing you to review their plan or results first [11:01 Opens in a new window ](http://www.youtube.com/watch?v=S1ch_6fjp5M&t=661).

- **Non-Coding Tasks:** Expansion into repository reporting, bug summarization, and work planning [12:04 Opens in a new window ](http://www.youtube.com/watch?v=S1ch_6fjp5M&t=724).

---