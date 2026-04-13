---
title: Your Claude Limit Burns In 90 Minutes Because Of One ChatGPT Habit.
id: 3379fa3b-8750-80cf-83ca-e1cf96cc69a7
url: https://www.notion.so/Your-Claude-Limit-Burns-In-90-Minutes-Because-Of-One-ChatGPT-Habit-3379fa3b875080cf83cae1cf96cc69a7
---

---

### **1. Inefficient Document Ingestion**

- **The Challenge:** Users often drag raw PDFs or images into conversations. These files contain formatting overhead (headers, footers, metadata) that can turn a 4,500-word document into over 100,000 tokens [03:12 Opens in a new window ](http://www.youtube.com/watch?v=5ztI_dbj6ek&t=192).

- **The Solution:** Convert documents to **Markdown** before uploading. This strips the "binary structure" and reduces the token footprint by up to 20x [03:42 Opens in a new window ](http://www.youtube.com/watch?v=5ztI_dbj6ek&t=222). Use free web services or Nate's "Open Brain" plugin to automate this conversion [04:32 Opens in a new window ](http://www.youtube.com/watch?v=5ztI_dbj6ek&t=272).

### **2. Conversation Sprawl**

- **The Challenge:** Running 20–40 turns in a single chat fills the context window with "croft" (useless history). This forces the model to compress original instructions, leading to "LLM psychosis" or drifted results [05:23 Opens in a new window ](http://www.youtube.com/watch?v=5ztI_dbj6ek&t=323).

- **The Solution:** * **Start fresh conversations** every 10–15 turns [12:32 Opens in a new window ](http://www.youtube.com/watch?v=5ztI_dbj6ek&t=752).

	- Separate **Information Gathering** (research) from **Execution** (doing the work) into different threads or even different models [07:15 Opens in a new window ](http://www.youtube.com/watch?v=5ztI_dbj6ek&t=435).

### **3. Silent "Plugin Tax"**

- **The Challenge:** Loading unnecessary plugins and connectors (like Google Drive) adds a "silent tax" to every message. Some users load 50,000 tokens of context before typing their first word [08:03 Opens in a new window ](http://www.youtube.com/watch?v=5ztI_dbj6ek&t=483).

- **The Solution:** **Audit your plugins**. Only enable the specific tools (the "right five") needed for the current task rather than leaving the whole "tool workshop" open [08:27 Opens in a new window ](http://www.youtube.com/watch?v=5ztI_dbj6ek&t=507).

### **4. Model Misuse (Over-Intelligence)**

- **The Challenge:** Using the most expensive models (like Claude Opus) for simple tasks like formatting, proofreading, or basic search is wasteful [11:49 Opens in a new window ](http://www.youtube.com/watch?v=5ztI_dbj6ek&t=709).

- **The Solution:** Use a tiered model strategy:

	- **Opus** for high-level reasoning.

	- **Sonnet** for execution.

	- **Haiku** for polishing and simple formatting [12:38 Opens in a new window ](http://www.youtube.com/watch?v=5ztI_dbj6ek&t=758).

### **5. Redundant API/Agent Calls**

- **The Challenge:** For technical users and API builders, re-sending the same system prompts, tool definitions, and reference docs for every call is "pouring money down the drain" [23:11 Opens in a new window ](http://www.youtube.com/watch?v=5ztI_dbj6ek&t=1391).

- **The Solution:** Implement **Prompt Caching**. This can provide a 90% discount on repeated content, reducing costs from $5.00 to $0.50 per million tokens on Opus [18:04 Opens in a new window ](http://www.youtube.com/watch?v=5ztI_dbj6ek&t=1084).

### **6. Poor Web Research Habits**

- **The Challenge:** Native web search within models like Claude can be token-heavy and slower [18:33 Opens in a new window ](http://www.youtube.com/watch?v=5ztI_dbj6ek&t=1113).

- **The Solution:** Use dedicated search services or **MCP (Model Context Protocol)** connectors like Perplexity. These are often 5x faster, provide structured citations, and use 10k–50k fewer tokens per search [19:32 Opens in a new window ](http://www.youtube.com/watch?v=5ztI_dbj6ek&t=1172).

### **7. Architectural Laziness in Agents**

- **The Challenge:** Giving an agent the "full codebase" or every project document when it only needs a specific slice [23:30 Opens in a new window ](http://www.youtube.com/watch?v=5ztI_dbj6ek&t=1410).

- **The Solution:** * **Index references:** Use RAG (Retrieval-Augmented Generation) to give agents only the relevant chunks [22:15 Opens in a new window ](http://www.youtube.com/watch?v=5ztI_dbj6ek&t=1335).

	- **Pre-process context:** Ensure documents are summarized and chunked before they reach the agent [22:35 Opens in a new window ](http://www.youtube.com/watch?v=5ztI_dbj6ek&t=1355).

	- **Scope context:** Only provide the minimum viable context required for the specific agent's task (e.g., don't give a planning agent the full code) [23:42 Opens in a new window ](http://www.youtube.com/watch?v=5ztI_dbj6ek&t=1422).

---

### **Model Selection Strategy**

 | **Model Type** | **Best Use Case** | **Examples** | 
 | ---- | ---- | ---- | 
 | **High-End (e.g., Opus 4.6)** | **Reasoning & Planning** | Complex architecture, logic-heavy problem solving, or strategic planning [12:38 Opens in a new window ](http://www.youtube.com/watch?v=5ztI_dbj6ek&t=758). | 
 | **Mid-Tier (e.g., Sonnet)** | **Execution & Coding** | Writing actual code, performing the "heavy lifting" of the work once the plan is set [12:38 Opens in a new window ](http://www.youtube.com/watch?v=5ztI_dbj6ek&t=758). | 
 | **Low-Tier (e.g., Haiku)** | **Polish & Formatting** | Proofreading, converting text to Markdown, or cleaning up simple data [12:38 Opens in a new window ](http://www.youtube.com/watch?v=5ztI_dbj6ek&t=758). | 

### **Key Advice for Implementation**

- **Don't Default to "Pro" Mode:** Blindly using the most expensive model regardless of the task (like using GPT-5.4 for a simple formatting job) is a common mistake that burns your limits unnecessarily [16:45 Opens in a new window ](http://www.youtube.com/watch?v=5ztI_dbj6ek&t=1005).

- **Use "Thinking" vs "Doing" Modes:** Conduct your research and "thinking" in separate chats or even different models (like Perplexity for search or Grok for social sentiment) [06:22 Opens in a new window ](http://www.youtube.com/watch?v=5ztI_dbj6ek&t=382). Pull the results together into a fresh chat only when you are ready for the AI to do the final "real work" [07:05 Opens in a new window ](http://www.youtube.com/watch?v=5ztI_dbj6ek&t=425).

- **Lean Out Your Context:** As models get more intelligent (like the upcoming Claude Mythos), you can actually provide *less* frontloaded context because the models are better at retrieval and following simpler instructions [11:05 Opens in a new window ](http://www.youtube.com/watch?v=5ztI_dbj6ek&t=665).

---

- **Perplexity:** For **web research**. It's often 5x faster, provides better citations, and burns 10k–50k fewer tokens than searching natively through Claude or ChatGPT [19:32 Opens in a new window ](http://www.youtube.com/watch?v=5ztI_dbj6ek&t=1172).

- **Grok:** For understanding **current social sentiment** or community discussions (specifically on X) [06:22 Opens in a new window ](http://www.youtube.com/watch?v=5ztI_dbj6ek&t=382).

- **ChatGPT (Thinking Mode):** For analyzing **earnings reports** or complex financial data to generate summaries before starting your "real work" in another model [06:34 Opens in a new window ](http://www.youtube.com/watch?v=5ztI_dbj6ek&t=394).

