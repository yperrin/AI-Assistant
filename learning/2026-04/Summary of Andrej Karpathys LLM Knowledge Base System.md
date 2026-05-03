---
complexity: Intermediate
date: 2026-04-27
id: 34f9fa3b-8750-804e-bb23-d54b92132c62
processed_by_ai: true
summary: This document explains a system, introduced by Nate Herk, that uses Claude
  Code and Obsidian to build a personal, compounding knowledge base with markdown
  files, moving beyond traditional RAG. It details the architecture, a 5-minute setup
  guide, and the benefits of using an LLM as an ingestion engine for structured knowledge.
title: Summary of Andrej Karpathys LLM Knowledge Base System
tools_mentioned:
- Claude Code
- Obsidian
- VS Code
- Obsidian Web Clipper
topics:
- Knowledge Management
- Personal Knowledge Base
- LLM Applications
- Retrieval-Augmented Generation (RAG)
- Markdown
- Second Brain
url: https://www.notion.so/Summary-of-Andrej-Karpathy-s-LLM-Knowledge-Base-System-34f9fa3b8750804ebb23d54b92132c62
---

### The system, as explained by [Nate Herk](https://www.youtube.com/@nateherk), leverages **Claude Code** and **Obsidian** to create a personal, compounding knowledge base that moves beyond ephemeral AI chats.

---

### **1. The Core Philosophy**

Traditional RAG (Retrieval-Augmented Generation) often relies on similarity searches that lack deep structural understanding. Karpathy's approach uses:

- **LLM as an Ingestion Engine:** You provide raw documents (PDFs, transcripts, etc.), and the LLM organizes, links, and summarizes them.

- **Markdown as Infrastructure:** The entire system is just a folder of markdown files. No complex vector databases or embedding pipelines are required.

- **Compounding Knowledge:** Instead of information disappearing after a session, it builds a persistent "second brain" where relationships are explicitly mapped via backlinks.

---

### **2. System Architecture**

The vault structure is intentionally simple to keep it scalable and token-efficient:

 | **Component** | **Description** | 
 | ---- | ---- | 
 | `**/raw**` | The landing zone for new, unprocessed source files (e.g., meeting notes, articles). | 
 | `**/wiki**` | The structured output from the LLM, containing interlinked concept pages and summaries. | 
 | `**index.md**` | A high-level map of all tools, techniques, and people within the vault. | 
 | `**log.md**` | A history of operations and updates performed by the agent. | 
 | `**CLAUDE.md**` | The "instruction manual" that tells Claude Code how to interact with and update the vault. | 

---

### **3. Setup Guide (5-Minute Process)**

1. **Install ****[Obsidian](https://obsidian.md/)****:** Use this as your visual IDE to see the graph of your knowledge.

1. **Initialize a Vault:** Create a folder and open it in Obsidian and [VS Code](https://code.visualstudio.com/).

1. **Boot ****[Claude Code](https://www.google.com/search?q=https%3A%2F%2Fdocs.anthropic.com%2Fen%2Fdocs%2Fagents-and-tools%2Fclaude-code)****:** Run `claude` in your terminal within that folder.

1. **Prompt for Implementation:** Copy the [original gist from Karpathy](https://www.google.com/search?q=https%3A%2F%2Fgist.github.com%2Fkarpathy%2Fllm-wiki.md) and tell Claude to implement it as your second brain.

1. **Ingest Content:** Use a tool like the [Obsidian Web Clipper](https://www.google.com/search?q=https%3A%2F%2Fchrome.google.com%2Fwebstore%2Fdetail%2Fobsidian-web-clipper%2Fmhfghmclicphhaanoojhkocjcaomamba) to drop articles into `/raw` and ask Claude to "ingest" them.

---

### **4. Key Benefits & Limitations**

- **Efficiency:** One user reported a **95% reduction in token usage** by querying a compact wiki instead of hundreds of raw files [04:53 Opens in a new window ](http://www.youtube.com/watch?v=sboNwYmH3AY&t=293).

- **Semantic Depth:** It follows links and indexes for a "human-like" understanding of relationships rather than just keyword similarity [16:17 Opens in a new window ](http://www.youtube.com/watch?v=sboNwYmH3AY&t=977).

- **Scalability Note:** While excellent for hundreds of pages (personal/small team scale), traditional RAG pipelines are still recommended for enterprise-level datasets with millions of documents [17:11 Opens in a new window ](http://www.youtube.com/watch?v=sboNwYmH3AY&t=1031).

---

> **Related Resource:** For more on building the logic behind these agents, see the [Every Claude Code Memory System Explained Opens in a new window ](https://www.youtube.com/watch?v=sboNwYmH3AY&list=WL&index=42&t=358s) video.