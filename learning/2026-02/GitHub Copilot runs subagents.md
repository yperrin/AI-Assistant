---
complexity: Intermediate
date: 2026-02-05 17:08:00-05:00
id: 2fe9fa3b-8750-8088-95b3-f2e7c5a86a7d
processed_by_ai: true
summary: This document describes subagents, specialized AI assistants that manage
  isolated tasks, preventing the main chat from becoming chaotic. They operate independently,
  return final results, and can be customized for specific roles.
title: GitHub Copilot runs subagents
tools_mentioned:
- '#runSubagent tool'
- Copilot Chat
- Git worktrees
topics:
- AI Assistants
- Context Management
- Task Automation
- Software Development Workflow
url: https://www.notion.so/GitHub-Copilot-runs-subagents-2fe9fa3b8750808895b3f2e7c5a86a7d
---

- **Isolated Context Management:** Subagents act as separate, specialized AI assistants with their own context windows. This prevents your main chat conversation from becoming "spaghetti" (too large and chaotic) by offloading tasks like file analysis, refactoring, or researching a specific file to a side session.

- **#runSubagent Tool:** You can trigger these, or Copilot may automatically initiate them, using the `#runSubagent` tool, especially for complex, multi-step tasks.

- **Independent Operation:** Subagents run in the background without pausing your main workflow and often work in separate Git worktrees to avoid polluting your workspace until the work is finalized.

- **Result Handoff:** Once a subagent finishes, it returns only the final results (diffs, summaries, test results) back to your main Copilot Chat session.

- **Customization:** You can define custom subagents (using `.agent.md` files) to handle specific roles like testing, documentation, or code review.