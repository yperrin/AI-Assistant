---
complexity: Intermediate
date: 2026-03-28 09:06:00-04:00
id: 3319fa3b-8750-807d-a652-fdeabc051c15
processed_by_ai: true
summary: This document outlines a four-layer approach to AI code review, combining
  automated checks, local AI agents, CI integration, and human oversight to improve
  code quality. It also provides practical tips for leveraging AI in code review,
  such as configuring deterministic hooks and using custom review files.
title: How I Use AI To Review AI Code
tools_mentioned:
- Git hooks
- npm test
- RuboCop
- Claude Code
- Code Rabbit
- OpenAI Codex
topics:
- AI Code Review
- Software Development
- Code Quality
- Automation
- Continuous Integration
url: https://www.notion.so/How-I-Use-AI-To-Review-AI-Code-3319fa3b8750807da652fdeabc051c15
---

---

### The 4 Layers of AI Code Review

 | **Layer** | **Focus** | **Key Tools/Methods** | 
 | ---- | ---- | ---- | 
 | **1. Automate the Obvious** | Catch syntax, linting, and formatting issues immediately. | Git hooks, `npm test`, RuboCop, security scanners. | 
 | **2. Local AI Review** | Use an agent to review another agent's output before committing. | [Claude Code](https://www.youtube.com/hashtag/claudecode) custom commands, [Code Rabbit](https://coderabbit.ai/) CLI. | 
 | **3. Automated CI Checks** | A "safety net" that scans PRs as soon as they are opened. | [OpenAI Codex](https://www.google.com/search?q=https%3A%2F%2Fopenai.com%2Fblog%2Fopenai-codex%2F) (GitHub integration), [Code Rabbit](https://coderabbit.ai/). | 
 | **4. Human Oversight** | High-level context, business logic, and critical architecture. | Manual peer review for high-risk changes (e.g., migrations). | 

---

### Key Takeaways & Tips

- **Be Suspicious:** Always assume AI-generated code has bugs. The speaker notes that 70% of teams report worse code quality after adopting AI because they skip the review phase [00:04 Opens in a new window ](http://www.youtube.com/watch?v=As2xy_cSx00&t=4).

- **Deterministic Hooks:** Configure [Claude Code](https://www.youtube.com/hashtag/claudecode) to run local scripts (linting/tests) automatically after it finishes a task [04:02 Opens in a new window ](http://www.youtube.com/watch?v=As2xy_cSx00&t=242).

- **Custom Review Files:** Use a `review.md` file in your repository to give AI agents project-specific guidelines (e.g., "Don't log PII" or "Check for race conditions") [06:16 Opens in a new window ](http://www.youtube.com/watch?v=As2xy_cSx00&t=376).

- **Group Findings:** When prompting a reviewer agent, ask it to categorize issues as **Must Fix** (critical) vs. **Minor** to avoid "noise" [09:10 Opens in a new window ](http://www.youtube.com/watch?v=As2xy_cSx00&t=550).

- **Local Execution:** Never push AI code without running it locally first to ensure the application actually starts and the UI isn't broken [05:25 Opens in a new window ](http://www.youtube.com/watch?v=As2xy_cSx00&t=325).

<br/>