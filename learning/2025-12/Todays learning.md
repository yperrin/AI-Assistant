---
title: Todays learning
id: 2bf9fa3b-8750-8033-9bfd-c3137cd51caf
url: https://www.notion.so/Today-s-learning-2bf9fa3b875080339bfdc3137cd51caf
---

- Open AI model node can now do web search and also file search. Files can be uploaded in Open AI and searched in n8n.

- A new major version is about to be released auto-save and more security.

<br/>

- It tries to be agent control first

- A window to manage multiple agents running in parallel

- The concept of artifact with which we can interact with directly and provide feedback in place that the agent will be able to use later.

<br/>

<br/>

- **Agent Manager (Mission Control):** A dashboard/inbox system to simultaneously spawn, monitor, and interact with multiple asynchronous agents (e.g., researcher, front-end mocker, back-end configurator) working on different parts of a project [01:12 Opens in a new window ](http://www.youtube.com/watch?v=VEiumna7MTM&t=72).

- **Asynchronous Feedback:** Enables you to leave inline comments on an agent's plans, task lists, or outputs while it is still running, which the agent will integrate into its plan on the fly. This prevents having to stop or restart the entire task [04:31 Opens in a new window ](http://www.youtube.com/watch?v=VEiumna7MTM&t=271).

- **Artifacts (Agent's Proof of Work):** Structured outputs used to facilitate the human-in-the-loop approach. Key types include:

	- **Tasks:** Outlines what the agent intends to do [07:47 Opens in a new window ](http://www.youtube.com/watch?v=VEiumna7MTM&t=467).

	- **Implementation Plans:** Detailed descriptions and approaches for building [08:14 Opens in a new window ](http://www.youtube.com/watch?v=VEiumna7MTM&t=494).

	- **Walkthroughs:** A running change log and step-by-step sequence of changes the agent made, often including screenshots/recordings [09:16 Opens in a new window ](http://www.youtube.com/watch?v=VEiumna7MTM&t=556).

- **Browser Automation:** Anti-gravity's integrated Chrome browser allows the agent to automatically navigate, click, and test the UI it builds. It can even **self-grade its work** against your guidelines and recommend its own updates, creating an automated UI and performance feedback loop [10:50 Opens in a new window ](http://www.youtube.com/watch?v=VEiumna7MTM&t=650).

- **Custom Workflows:** Allows you to save and reuse structured prompts (similar to slash commands) for repeatable processes, like a multi-phase debugging workflow, ensuring consistent best practices [13:02 Opens in a new window ](http://www.youtube.com/watch?v=VEiumna7MTM&t=782).

- **Review Policy (Always Ask for Review):** The video recommends toggling the setting to **"always ask for a human's review"** when starting, as the "agent decides" option often proceeds without human oversight, which can be risky for critical features [15:54 Opens in a new window ](http://www.youtube.com/watch?v=VEiumna7MTM&t=954).

- **Model Selection:** Use **Gemini 3 Pro** for complex, robust builds or any anti-gravity-specific features, as the models are optimized for their native tools. Use **Claude Sonnet 4.5** as a fallback for complicated debugging, and **GPT-OSS** for simple administrative tasks [18:13 Opens in a new window ](http://www.youtube.com/watch?v=VEiumna7MTM&t=1093).

<br/>

- **Platform Design:** Anti-gravity consists of three main surfaces that allow agents to interact across different parts of a software developer's workflow [01:41 Opens in a new window ](http://www.youtube.com/watch?v=HN-F-OQe6j0&t=101):

	- **Agent Manager:** The central hub for managing multiple agents and tasks, sitting at a higher level than just code [02:16 Opens in a new window ](http://www.youtube.com/watch?v=HN-F-OQe6j0&t=136). It includes an "inbox" to surface commands that require human attention [04:48 Opens in a new window ](http://www.youtube.com/watch?v=HN-F-OQe6j0&t=288).

	- **AI Editor:** The standard code editor (forked from VS Code) with an agent sidebar [02:34 Opens in a new window ](http://www.youtube.com/watch?v=HN-F-OQe6j0&t=154).

	- **Agent Controlled Browser:** A Chrome browser that the agent can actively control (click, scroll, run JavaScript) [03:13 Opens in a new window ](http://www.youtube.com/watch?v=HN-F-OQe6j0&t=193). This enables context retrieval (like authenticated access to Google Docs or GitHub dashboards) and provides verifiable results through screen recordings [03:25 Opens in a new window ](http://www.youtube.com/watch?v=HN-F-OQe6j0&t=205).

- **Motivations and Capabilities:** The product's design is driven by the enhanced capabilities of **Gemini 3 Pro**, which offers better intelligence, reasoning, longer-running tasks, and powerful multimodal functionality [07:10 Opens in a new window ](http://www.youtube.com/watch?v=HN-F-OQe6j0&t=430). Key new capabilities include:

	- **Computer Use:** The ability for the agent to use the browser for research and verification, going beyond just code generation [08:45 Opens in a new window ](http://www.youtube.com/watch?v=HN-F-OQe6j0&t=525).

	- **Multimodal Iteration:** Leveraging image understanding and generation to allow developers to iterate on design mockups directly in image space with the agent [11:18 Opens in a new window ](http://www.youtube.com/watch?v=HN-F-OQe6j0&t=678).

- **Artifacts (New Interaction Pattern):** To handle longer, more complex tasks, the platform introduces **Artifacts** [12:32 Opens in a new window ](http://www.youtube.com/watch?v=HN-F-OQe6j0&t=752).

	- Artifacts are dynamic, visual representations of information that the agent generates, such as a task plan, architecture diagrams, or a final walkthrough/PR description [14:14 Opens in a new window ](http://www.youtube.com/watch?v=HN-F-OQe6j0&t=854).

	- They replace a long stream of conversational "chain of thought" by focusing on a consumable, visual output [13:53 Opens in a new window ](http://www.youtube.com/watch?v=HN-F-OQe6j0&t=833).

	- The system allows for collaborative feedback, letting users leave Google Docs-style comments on plans or Figma-style comments on images for the agent to incorporate mid-task [17:59 Opens in a new window ](http://www.youtube.com/watch?v=HN-F-OQe6j0&t=1079).

- **The Flywheel:** The product is built internally for Google engineers and DeepMind researchers, creating a **research-product flywheel** where using the product informs and improves the models, and better models lead to a more advanced product [20:59 Opens in a new window ](http://www.youtube.com/watch?v=HN-F-OQe6j0&t=1259).

<br/>

## ✨ Major New Features & Enhancements

- **Autosave:** This is a highly requested feature that is finally being introduced (scheduled to launch shortly after the stable release).3

- **Improved UI/UX:**

	- **Updated Canvas Look and Feel:** A visual refresh for the main workflow building canvas.4

	- **Updated Sidebar:** User experience improvements to the sidebar navigation.5

- **Core Improvements:** A core focus on making the platform more **mature, secure, and reliable** than ever before.6

## ⚠️ Important Migration Information

- **Migration Report Tool:** To help with the upgrade, n8n has introduced a **Migration Report tool** (available since version 1.121.0 for Global Admins).8 This tool scans your instance and helps you identify:

	- **Workflow Issues:** Breaking changes that affect specific workflows.9

	- **Instance Issues:** Configuration changes affecting your entire n8n server, such as environment variables.10

- **Security & Cleanup:** Breaking changes are primarily aimed at:

	- Enforcing more robust security measures.11

	- Altering storage backends and configuration processes.12

	- Removing older, legacy components.

- **Support for v1.x:** Version 1.x will continue to receive bug and security fixes for three months after the v2.0 stable release, but no new features.13

---

### 📅 Projected Release Timeline

- **Version 2.0.0 (Beta):** Scheduled for **early December** (e.g., Dec 8th).14

- **Version 2.0.x (Stable):15** Scheduled for **mid-December** (e.g., Dec 15th).16

