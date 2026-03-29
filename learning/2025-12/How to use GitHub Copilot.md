---
title: How to use GitHub Copilot
id: 2c69fa3b-8750-80f1-8de1-d67eb723ab4b
url: https://www.notion.so/How-to-use-GitHub-Copilot-2c69fa3b875080f18de1d67eb723ab4b
---

<br/>

### **The Three Core Components**

- **Custom Instructions** `[04:03]`

	- **What they are:** High-level context about your specific project (e.g., tech stack, architectural patterns, coding rules).

	- **Where they live:** You can create a `.github/instructions` file in your project or use a global user file.

	- **How they work:** They are automatically inserted at the *end* of the System Prompt for every request, ensuring the AI always knows your project's specific context.

- **Prompt Files** `[07:00]`

	- **What they are:** Reusable, pre-written prompts for repetitive tasks (e.g., "Explain this bug," "Write a unit test").

	- **Key Feature:** You can hardcode a specific AI model (e.g., GPT-4, Claude 3.5 Sonnet) into the file. This lets you auto-switch to a smarter model for hard tasks without manually changing settings.

	- **How they work:** They are inserted into the *User Prompt* (not the System Prompt) at the time of the specific request.

- **Custom Agents** `[12:09]`

	- **What they are:** specialized "personas" you can switch to (like "Plan Mode" or "Beast Mode") that have unique identities and behaviors.

	- **How they work:** They act as a new system layer, defining how the AI should behave overall (e.g., "You are a planning agent, do not write code, only outline steps"). They sit at the very bottom of the System Prompt.

### **The "Pro" Workflow Strategy** `[15:08]`

1. **Plan (Premium Model):** Use a **Prompt File** that forces a high-end model (like Claude 3.5 Opus) to create a detailed, step-by-step coding plan.

1. **Generate (Premium Model):** Use another prompt to have the high-end model write the actual code into a temporary Markdown document (not the codebase yet), ensuring high-quality logic.

1. **Implement (Cheap Model):** Use a **Custom Agent** powered by a faster, cheaper model (like GPT-4o Mini) to read that Markdown file and apply the changes to your actual files. Since the logic is already written, the cheaper model just needs to copy/paste and apply, which it does perfectly well.

### **Key Takeaway on "Context Rot"** `[10:37]`

- **Tip:** Once a task is done, clear your chat context before starting the next step to keep the AI sharp.

