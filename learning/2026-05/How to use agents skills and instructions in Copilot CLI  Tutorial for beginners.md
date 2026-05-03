---
complexity: Intermediate
date: 2026-05-03 10:07:00-04:00
id: 3559fa3b-8750-800a-bac6-e7f10e63afbd
processed_by_ai: true
summary: 'This document explains how to customize GitHub Copilot CLI to align with
  organizational standards using three primary mechanisms: Instructions, Skills, and
  Custom Agents. This tiered strategy helps ensure AI-generated code and tasks adhere
  to specific patterns and practices, automating governance and maintaining consistency
  across a codebase.'
title: How to use agents skills and instructions in Copilot CLI  Tutorial for beginners
tools_mentioned:
- GitHub Copilot CLI
- Python
- Flask
- React
- Playwright
topics:
- GitHub Copilot CLI customization
- AI code generation
- Organizational coding standards
- Instructions files
- Agent Skills
- Custom Agents
- Automation
- Software development practices
url: https://www.notion.so/How-to-use-agents-skills-and-instructions-in-Copilot-CLI-Tutorial-for-beginners-3559fa3b8750800abac6e7f10e63afbd
---

This analysis covers the GitHub tutorial on customizing GitHub Copilot CLI to align with organizational standards using three primary mechanisms: **Instructions**, **Skills**, and **Agents**.

---

## 1. Executive Summary

In this episode of the [GitHub Copilot CLI for beginners](http://www.youtube.com/watch?v=-yKALFS5ewY) series, the core focus is ensuring that AI-generated code and tasks adhere to specific organizational patterns and practices.

The video addresses the problem of generic AI responses that may ignore team-specific requirements (like docstrings or specialized templates). To solve this, GitHub introduces a tiered customization strategy:

- **Instructions:** Markdown-based rules that provide context on "what" and "how" to build.

- **Skills:** Automated workflows for lower-level tasks, such as creating standardized pull requests.

- **Custom Agents:** Specialized "workers" designed for complex, project-wide tasks like accessibility or SEO reviews.

By utilizing these tools in harmony, teams can automate repetitive governance and ensure consistency across their codebase.

---

## 2. Detailed Transcription

**[00:04 Opens in a new window ](http://www.youtube.com/watch?v=-yKALFS5ewY&t=4)** In this episode of GitHub Copilot CLI for beginners, we're going to explore instructions files, agents, and skills, which all allow you to ensure that Copilot is following the exact same patterns and practices that your organization has laid out and that you're already following.

**[00:23 Opens in a new window ](http://www.youtube.com/watch?v=-yKALFS5ewY&t=23)** Ensuring Copilot works with existing patterns and practices our organizations have set forth is key to success. To support this, Copilot has several capabilities between instructions files, custom agents, and agent skills to ensure you get the code and activities how you'd have completed them if you did them manually. Let's explore each of these separately, then bring them together at the end to see how they help us form a cohesive strategy.

**[00:54 Opens in a new window ](http://www.youtube.com/watch?v=-yKALFS5ewY&t=54)** Let's start with instructions. Sort of as the name would suggest, instructions are exactly that: instructions to Copilot. They provide Copilot the background of both what we're building and how we're building it. Defined in markdown files, instruction files come in two core varieties: a single centralized `.github/copilot-instructions.md` file which is project-level, and `.instructions` files which allow you to target specific types of files like tests or code used to define APIs.

**[01:25 Opens in a new window ](http://www.youtube.com/watch?v=-yKALFS5ewY&t=85)** Let's make a quick request of Copilot to see the impact of instructions files. I'll ask for an API to be generated which, in the case of my application, is done using Python and Flask. We can see the response is relatively generic; it follows my existing patterns, but let's say our organization requires docstrings. Let's add a `.github/copilot-instructions.md` file. The Copilot instructions file is global to that entire project and always in context. If we explain we always want docstrings, then send the same command, we see the impact of this: a docstring is now included with the function in the generated code.

**[02:04 Opens in a new window ](http://www.youtube.com/watch?v=-yKALFS5ewY&t=124)** Copilot instructions is "table stakes." Every project should have one. It's so important, in fact, that there's a slash command to generate them: `/setup`. This will give you a great starting point from which you can add specifics about your project.

**[02:18 Opens in a new window ](http://www.youtube.com/watch?v=-yKALFS5ewY&t=138)** Now, `.instructions` files allow you to get more specific, targeting individual types of files. In our Flask API, for example, we have specific requirements on how we want those files to be built. By adding a `.instructions` file, we can break down our instructions into smaller chunks. The `apply-to` section accepts a path which will be used by Copilot to determine when to use that provided context. In our case, we've specified Python files in our `server/routes` folder.

**[02:49 Opens in a new window ](http://www.youtube.com/watch?v=-yKALFS5ewY&t=169)** As you might expect, there are common instructions you might want to add, like how to create React components or Playwright tests. There's a collection of instructions files you can quickly add to your project at [gh.io/awesome-copilot](https://www.google.com/search?q=https%3A%2F%2Fgh.io%2Fawesome-copilot).

**[03:04 Opens in a new window ](http://www.youtube.com/watch?v=-yKALFS5ewY&t=184)** Turning our attention to activities and tools we might want to provide Copilot: our agent skills. Skills can be used to tell Copilot both how we want to create that code and how we want to perform lower-level tasks. They are defined with markdown files and even scripts in the `.github/skills` folder. We've got a skill here for creating contributions to a repository. It instructs Copilot to look for contribution guidelines and issue and pull request templates. If those exist, it will use those, or use the templates we've given it as an example to ensure Copilot is doing its best work.

**[03:44 Opens in a new window ](http://www.youtube.com/watch?v=-yKALFS5ewY&t=224)** Skills can be called by using them as slash commands—`/make-contribution` in our case—or dynamically through natural language. When we ask Copilot to make a pull request or PR, it automatically kicks off that skill following the guidance provided. It generates a new branch, an issue, logically groups commits, and eventually creates a PR using the template defined in the repository. And just like before, there are skills available that you can use in your projects at [gh.io/awesome-copilot](https://www.google.com/search?q=https%3A%2F%2Fgh.io%2Fawesome-copilot).

**[04:16 Opens in a new window ](http://www.youtube.com/watch?v=-yKALFS5ewY&t=256)** Now for larger tasks, we have custom agents. Custom agents, defined in markdown files either in `.github/agents` or by your organization, allow you to create specialized workers for particular scenarios. Let's take accessibility as an example. Accessibility is, of course, important, and we always want to get it right. It can also require updates to numerous parts of our application and some specialized skills. Custom agents have their own context and are built for exactly this. Using the `/agent` command, we see the list of agents that are available.

**[05:00 Opens in a new window ](http://www.youtube.com/watch?v=-yKALFS5ewY&t=300)** Let's activate that accessibility agent and ask Copilot to perform a review, identifying the most impactful updates that could be made to our code. Just as before, Copilot diligently performs the task, this time as the accessibility custom agent. Once it generates the suggestions, we can then ask it to apply them, and off it goes.

**[05:24 Opens in a new window ](http://www.youtube.com/watch?v=-yKALFS5ewY&t=324)** Instructions, skills, and agents are all defined as markdown files, and you might be wondering when to use each. It's important to highlight that these are built to be used in harmony with one another rather than an "either/or" approach.

- **Instructions** provide context on how best to generate code—the things Copilot should be considering as it modifies and updates the codebase.

- **Skills** are tools in Copilot's toolbox for performing tasks, like how it should approach running tests and recovering from failures or creating a PR to a project.

- **Agents** are built to handle more complex tasks, like performing search engine optimization or an accessibility review, which might require updates to the entire project.

**[06:05 Opens in a new window ](http://www.youtube.com/watch?v=-yKALFS5ewY&t=365)** Working together, these features ensure tasks are completed correctly—both what needs to be done and how it needs to be done.

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