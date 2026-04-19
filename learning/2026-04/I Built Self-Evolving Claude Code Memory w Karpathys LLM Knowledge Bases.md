---
complexity: Intermediate
date: 2026-04-07 20:28:00-04:00
id: 33c9fa3b-8750-80dc-ac16-ecaa6515ca03
processed_by_ai: true
summary: This document outlines a knowledge management system that uses an LLM-based
  "compiler" analogy to process raw data into an organized wiki, emphasizing self-correction
  and cost-effectiveness over traditional RAG methods. It details the architecture,
  key components, and benefits of this approach for creating evolving, contextual
  memory systems.
title: I Built Self-Evolving Claude Code Memory w Karpathys LLM Knowledge Bases
tools_mentioned:
- Obsidian
- Claude Code
topics:
- Knowledge Management
- LLMs
- Personal Wiki
- Data Processing
- System Architecture
- Cost Optimization
- Self-Correction
url: https://www.notion.so/I-Built-Self-Evolving-Claude-Code-Memory-w-Karpathy-s-LLM-Knowledge-Bases-33c9fa3b875080dcac16ecaa6515ca03
---

### Core Architecture: The "Compiler" Analogy

 | **Stage** | **Component** | **Description** | 
 | ---- | ---- | ---- | 
 | **Source Code** | **Raw Folder** | The entry point containing unprocessed articles, papers, or conversation transcripts. | 
 | **Compiler** | **LLM Processing** | A script sends raw data to an LLM to generate summaries, extract concepts, and create links. | 
 | **Executable** | **The Wiki** | The final, compiled Markdown files organized into concepts and connections. | 
 | **Test Suite** | **Health Checks** | Automated "linting" to find broken links, stale data, or research gaps [04:30 Opens in a new window ](http://www.youtube.com/watch?v=7huCP6RkcY4&t=270). | 
 | **Runtime** | **Agent Query** | The LLM agent searches the wiki, using a master **index file** to navigate without needing semantic search [05:22 Opens in a new window ](http://www.youtube.com/watch?v=7huCP6RkcY4&t=322). | 

---

### Key Components & Tools

- **[Obsidian](https://www.google.com/search?q=https%3A%2F%2Fobsididan.md)****:** Often used as the "canvas" for the knowledge base. Its [Graph View](https://help.obsidian.md/Plugins/Graph+view) allows users and agents to visualize how different pieces of knowledge are connected through back-links [04:06 Opens in a new window ](http://www.youtube.com/watch?v=7huCP6RkcY4&t=246).

- **[Claude Code](https://www.google.com/search?q=https%3A%2F%2Fdocs.anthropic.com%2Fen%2Fdocs%2Fagents-and-tools%2Fclaude-code)****:** Used to automate the creation and maintenance of the memory system through custom hooks.

- **Self-Correction:** The system performs "health checks" to ensure data integrity, much like a linter checks code for errors [04:54 Opens in a new window ](http://www.youtube.com/watch?v=7huCP6RkcY4&t=294).

### Benefits of This Approach

- **95% Cheaper than RAG:** By avoiding complex vector databases and utilizing automaintained index files, the system stays lightweight and cost-effective [05:22 Opens in a new window ](http://www.youtube.com/watch?v=7huCP6RkcY4&t=322).

- **Contextual Evolution:** For developers, this creates a "codebase memory" that tracks architectural decisions and lessons learned over time, rather than just raw git logs [09:06 Opens in a new window ](http://www.youtube.com/watch?v=7huCP6RkcY4&t=546).

- **Customization:** Unlike "black box" memory systems, users can modify the underlying prompts and scripts to change how the LLM extracts and promotes knowledge [16:14 Opens in a new window ](http://www.youtube.com/watch?v=7huCP6RkcY4&t=974).

### References