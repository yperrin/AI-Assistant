---
title: Building Agents in 2026
id: 3079fa3b-8750-808a-b3db-cfa1f82ffd20
url: https://www.notion.so/Building-Agents-in-2026-3079fa3b8750808ab3dbcfa1f82ffd20
---

### **Key Highlights**

- **Flagship vs. Open Source:** While models like [GPT 5.2](http://www.youtube.com/watch?v=D-d4Y6v-pDs) and [Claude 4.6](http://www.youtube.com/watch?v=D-d4Y6v-pDs) [05:10 Opens in a new window ](http://www.youtube.com/watch?v=D-d4Y6v-pDs&t=310) continue to improve in reasoning and autonomy, open-source models (particularly from the [Qwen](http://www.youtube.com/watch?v=D-d4Y6v-pDs) and [GLM](http://www.youtube.com/watch?v=D-d4Y6v-pDs) series) have reached a quality level that allows for local, private agent development [08:16 Opens in a new window ](http://www.youtube.com/watch?v=D-d4Y6v-pDs&t=496).

- **Agentic Fundamentals:** Tina reiterates that agentic systems are composed of [six core components](http://www.youtube.com/watch?v=D-d4Y6v-pDs): tools, knowledge, memory, audio/speech, guardrails, and orchestration [24:04 Opens in a new window ](http://www.youtube.com/watch?v=D-d4Y6v-pDs&t=1444).

- **Local Workflows:** She demonstrates two practical agents:

	- **Financial Agent:** A no-code agent built using [n8n](http://www.youtube.com/watch?v=D-d4Y6v-pDs) and [Ollama](http://www.youtube.com/watch?v=D-d4Y6v-pDs) [30:11 Opens in a new window ](http://www.youtube.com/watch?v=D-d4Y6v-pDs&t=1811) that analyzes credit card statements locally on her machine, keeping sensitive data private [31:34 Opens in a new window ](http://www.youtube.com/watch?v=D-d4Y6v-pDs&t=1894).

	- **Email Agent:** A Python-based system using the [OpenAI Agents SDK](http://www.youtube.com/watch?v=D-d4Y6v-pDs) [44:17 Opens in a new window ](http://www.youtube.com/watch?v=D-d4Y6v-pDs&t=2657) that screens emails, drafts replies, and flags suspicious activity for human review [40:37 Opens in a new window ](http://www.youtube.com/watch?v=D-d4Y6v-pDs&t=2437).

- **Security Focus:** She warns about the risks of viral tools like [OpenClaw](http://www.youtube.com/watch?v=D-d4Y6v-pDs) [48:17 Opens in a new window ](http://www.youtube.com/watch?v=D-d4Y6v-pDs&t=2897), noting that giving agents broad system access (email, terminal, files) requires rigorous security practices like containerization and auditing [52:40 Opens in a new window ](http://www.youtube.com/watch?v=D-d4Y6v-pDs&t=3160).

---

### **Tools and Frameworks Used**

 | **Tool / Framework** | **Description** | 
 | ---- | ---- | 
 | [Ollama](http://www.youtube.com/watch?v=D-d4Y6v-pDs) | A local model manager and developer tool used to download and run open-source LLMs like [Qwen 3](http://www.youtube.com/watch?v=D-d4Y6v-pDs) locally [21:21 Opens in a new window ](http://www.youtube.com/watch?v=D-d4Y6v-pDs&t=1281). | 
 | [n8n](http://www.youtube.com/watch?v=D-d4Y6v-pDs) | A low-code workflow automation tool used for building and hosting agentic systems locally [28:46 Opens in a new window ](http://www.youtube.com/watch?v=D-d4Y6v-pDs&t=1726). | 
 | [OpenAI Agents SDK](http://www.youtube.com/watch?v=D-d4Y6v-pDs) | A development kit used to build complex, multi-agent Python workflows, now supporting open-source models [24:58 Opens in a new window ](http://www.youtube.com/watch?v=D-d4Y6v-pDs&t=1498). | 
 | [Qwen (3, 38B, Coder)](http://www.youtube.com/watch?v=D-d4Y6v-pDs) | A series of high-performance open-source models used as the "brain" for the agents in the demos [32:04 Opens in a new window ](http://www.youtube.com/watch?v=D-d4Y6v-pDs&t=1924). | 
 | [Warp](http://www.youtube.com/watch?v=D-d4Y6v-pDs) | An AI-integrated terminal used for managing the Python-based email agent and execution environment [39:16 Opens in a new window ](http://www.youtube.com/watch?v=D-d4Y6v-pDs&t=2356). | 
 | [Docker](http://www.youtube.com/watch?v=D-d4Y6v-pDs) | Used for self-hosting n8n and Ollama, and recommended for isolating agents for security [29:02 Opens in a new window ](http://www.youtube.com/watch?v=D-d4Y6v-pDs&t=1742). | 
 | [OpenClaw](http://www.youtube.com/watch?v=D-d4Y6v-pDs) | A viral, autonomous AI agent that runs 24/7 on local hardware to manage calendars, files, and emails [48:55 Opens in a new window ](http://www.youtube.com/watch?v=D-d4Y6v-pDs&t=2935). | 
 | [Self-Hosted AI Starter Kit](http://www.youtube.com/watch?v=D-d4Y6v-pDs) | A bundle including n8n, Ollama, [Qdrant](http://www.youtube.com/watch?v=D-d4Y6v-pDs) (vector store), and [PostgreSQL](http://www.youtube.com/watch?v=D-d4Y6v-pDs) for local AI development [29:11 Opens in a new window ](http://www.youtube.com/watch?v=D-d4Y6v-pDs&t=1751). | 

