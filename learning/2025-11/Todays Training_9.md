---
title: Todays Training
id: 2b89fa3b-8750-80ed-8e3a-d7f91258a5de
url: https://www.notion.so/Today-s-Training-2b89fa3b875080ed8e3ad7f91258a5de
---

- **Discoverable & Addressable:** Easy to find and access via stable interfaces (APIs, SQL).

- **Trustworthy:** Governed with strict quality and lineage controls.

- **Self-Service:** Treated like a product with SLAs for internal consumers.

- **Real-Time at Scale:** Most companies are managing massive, high-velocity data streams. A standout example was **Ferrovial**, which uses real-time traffic data to dynamically regulate highway fees to reduce congestion.

- **Horizontal Democratization:** **SAP** is re-architecting its vertical business functions (like HR and Sales) to break data silos and allow data to flow horizontally across the organization.

<br/>

- **Rung 1: No-Code Start ****[02:16 Opens in a new window](http://www.youtube.com/watch?v=UcoFMDmmqV0&t=136)**

	- Use natural language to prompt CrewAI Studio to build a basic agent (e.g., "Build a personal trainer agent").

	- The system automatically generates the agent, tasks, and output format in seconds using a drag-and-drop interface.

- **Rung 2: Specialized Agents ****[04:28 Opens in a new window](http://www.youtube.com/watch?v=UcoFMDmmqV0&t=268)**

	- Break down complex tasks by creating multiple specialized agents (e.g., a "Head Nutritionist" separate from the "Trainer").

	- Assign specific roles, goals, backstories, and pre-built tools (like Brave Search or Google Sheets) to each agent to improve output quality.

- **Rung 3: Custom Tools with Code ****[08:46 Opens in a new window](http://www.youtube.com/watch?v=UcoFMDmmqV0&t=526)**

	- Extend capabilities by writing your own Python tools for specific needs (e.g., querying the USDA food database API) using the command line (`crewai tool create`).

	- Publish these tools back to the Studio to use them in your no-code workflows.

- **Rung 4: Deployment & Integration ****[11:37 Opens in a new window](http://www.youtube.com/watch?v=UcoFMDmmqV0&t=697)**

	- **Local Use:** Download the entire project as code to run it locally, allowing for infinite customization and integration into other pipelines.

	- **MCP Server:** Export your agent as an **MCP (Model Context Protocol) server**, turning it into a tool that can be used by other apps like Claude Desktop or other fitness platforms.

<br/>

- **Transformation to AI-Native:** Prasanna, initially a part-time engineer, wrote an "AI manifesto" to CEO Jack Dorsey, advocating for a centralized AI strategy. This led to his promotion to CTO and a company-wide shift to prioritize technology and functional organization (unifying engineering and design teams) over siloed business units.

- **"Goose" AI Agent:** Block developed an internal, open-source AI agent called "Goose," built on the Model Context Protocol (MCP). It acts as a general-purpose assistant that can execute tasks by connecting to various tools (like Snowflake, Slack, or Google Docs).

	- **Impact:** Engineering teams using Goose report saving **8-10 hours per week**, with company-wide manual hours saved trending toward 20-25%.

	- **Capability:** Unlike simple chatbots, Goose can "watch" a user's screen, anticipate needs (e.g., auto-drafting a PR for a discussed feature), and perform complex multi-step workflows across different apps.

- **Shift in Hiring & Work:** Block now prioritizes "learning mindset" over specific AI skills, looking for engineers eager to adopt new tools. The role of engineers is evolving from writing code to orchestrating AI agents, with non-technical teams also building their own internal tools using these agents.

- **Code Quality vs. Product Value:** Prasanna argues that code quality does not equal product success, citing YouTube's messy early codebase as an example. He emphasizes solving real user problems over architectural perfection.

- **Open Source Philosophy:** Block released Goose as open source, encouraging other companies to build on it. This aligns with their broader mission of economic empowerment and openness.

