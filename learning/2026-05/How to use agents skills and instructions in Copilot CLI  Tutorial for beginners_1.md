---
complexity: Advanced
date: 2026-05-03 10:07:00-04:00
id: 3559fa3b-8750-800a-bac6-e7f10e63afbd
processed_by_ai: true
summary: This document outlines how to leverage GitHub Copilot's advanced features,
  including Instructions, Skills, and Custom Agents, to automate development workflows,
  enforce coding standards, and perform specialized tasks like accessibility or SEO
  audits. It provides use cases and solutions for integrating these features into
  a project's development lifecycle.
title: How to use agents skills and instructions in Copilot CLI  Tutorial for beginners
tools_mentioned:
- Copilot
- React
- Playwright
topics:
- GitHub Copilot
- Code Generation
- Development Workflows
- Automation
- AI Agents
- Coding Standards
- Accessibility
- SEO
url: https://www.notion.so/How-to-use-agents-skills-and-instructions-in-Copilot-CLI-Tutorial-for-beginners-3559fa3b8750800abac6e7f10e63afbd
---

---

## 1. Executive Summary

- **Instructions:** Markdown-based rules that provide context on "what" and "how" to build.

- **Skills:** Automated workflows for lower-level tasks, such as creating standardized pull requests.

- **Custom Agents:** Specialized "workers" designed for complex, project-wide tasks like accessibility or SEO reviews.

---

## 2. Detailed Transcription

- **Instructions** provide context on how best to generate code—the things Copilot should be considering as it modifies and updates the codebase.

- **Skills** are tools in Copilot's toolbox for performing tasks, like how it should approach running tests and recovering from failures or creating a PR to a project.

- **Agents** are built to handle more complex tasks, like performing search engine optimization or an accessibility review, which might require updates to the entire project.

---

## 3. Use Case & Solution Index

### Use Case: Enforcing Coding Standards (e.g., Docstrings)

- **Solution:** Use a project-level **Instructions File** (`.github/copilot-instructions.md`). This provides a global context that persists across the entire project.

- **Action:** Use the `/setup` slash command to generate a base template.

### Use Case: Specialized File Formatting (e.g., API Routes)

- **Solution:** Use **Targeted Instructions Files** (`.instructions`). These use an `apply-to` field to specify paths (like `server/routes/*.py`) so Copilot only uses those specific rules when working on relevant files.

### Use Case: Automating Pull Request Workflows

- **Solution:** Implement **Agent Skills**. Define a skill in `.github/skills` that checks for `CONTRIBUTING.md` and PR templates.

- **Action:** Trigger via natural language (e.g., "Make a PR") or a custom slash command to automate branch creation, commit grouping, and template population.

### Use Case: Performing Specialized Audits (e.g., Accessibility)

- **Solution:** Deploy **Custom Agents**. Create a specialized worker in `.github/agents` with a dedicated context for accessibility or SEO.

- **Action:** Use the `/agent` command to select the specific worker and have it perform a comprehensive review and apply fixes across the codebase.

### Use Case: Finding Pre-made Configurations

- **Solution:** Visit the community repository at [gh.io/awesome-copilot](https://www.google.com/search?q=https%3A%2F%2Fgh.io%2Fawesome-copilot) to download pre-defined instructions and skills for React, Playwright, and more.