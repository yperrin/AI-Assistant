---
complexity: Intermediate
date: 2026-03-06 19:31:00+05:30
id: 31b9fa3b-8750-80cc-bdcd-c34aab737c81
processed_by_ai: true
summary: This document outlines new features for an agent system, including the ability
  to invoke specific skills using slash commands, provide mid-conversation instructions,
  utilize an integrated browser for web interaction and code execution, fork conversations,
  and execute custom shell commands at various lifecycle points.
title: 5 New VS Code Features for Smarter Agents
tools_mentioned:
- Playwright
- Shell commands
topics:
- Agent capabilities
- AI interaction
- Software development workflows
- Automation
- Conversational AI
url: https://www.notion.so/5-New-VS-Code-Features-for-Smarter-Agents-31b9fa3b875080ccbdcdc34aab737c81
---

- **Agent Skills on Demand**: You can now reference specific agent instructions (skills) using slash commands. For example, using `/frontend-design` ensures the agent follows your predefined style guidelines and architectural standards [00:37 Opens in a new window ](http://www.youtube.com/watch?v=MvwcWWp1NFs&t=37).

- **Message Steering**: You can now provide additional instructions or clarifications while an agent is still working. The agent will incorporate these mid-response, eliminating the need to stop and restart the chat [01:15 Opens in a new window ](http://www.youtube.com/watch?v=MvwcWWp1NFs&t=75).

- **Integrated Browser**: Agents can now autonomously open an integrated browser to navigate pages, verify content, and execute Playwright code to ensure their changes work as expected [01:41 Opens in a new window ](http://www.youtube.com/watch?v=MvwcWWp1NFs&t=101).

- **Fork Conversations**: Use the `/fork` command to create a new session with the full existing history. This allows you to explore alternative directions or designs without losing the context of your original conversation [01:55 Opens in a new window ](http://www.youtube.com/watch?v=MvwcWWp1NFs&t=115).

- **Hook Support**: You can now execute custom shell commands at specific lifecycle points. For instance, you can set a hook to automatically commit pending changes as soon as an agent session stops [02:29 Opens in a new window ](http://www.youtube.com/watch?v=MvwcWWp1NFs&t=149).