---
complexity: Intermediate
date: 2026-04-07 20:28:00-04:00
id: 33c9fa3b-8750-80dc-ac16-ecaa6515ca03
processed_by_ai: true
summary: This document describes LLM knowledge bases, a self-evolving wiki system
  popularized by Andrej Karpathy, which uses Large Language Models to organize research
  and notes in structured Markdown files with interconnected links and LLM-managed
  indexes, offering a cheaper and more customizable alternative to traditional RAG
  systems. It outlines a "compiler"-like architecture and highlights tools like Obsidian
  and Claude Code.
title: I Built Self-Evolving Claude Code Memory w Karpathys LLM Knowledge Bases
tools_mentioned:
- Obsidian
- Claude Code
- RAG
topics:
- LLM Knowledge Bases
- Knowledge Management
- Large Language Models
- Information Organization
- Self-Evolving Systems
- Markdown
- Retrieval-Augmented Generation (RAG)
- Software Engineering Analogy
- Cost-Effectiveness
- Contextual Evolution
url: https://www.notion.so/I-Built-Self-Evolving-Claude-Code-Memory-w-Karpathy-s-LLM-Knowledge-Bases-33c9fa3b875080dcac16ecaa6515ca03
---

LLM knowledge bases, a concept popularized by [Andrej Karpathy](https://www.google.com/search?q=https%3A%2F%2Fx.com%2Fkarpathy%2Fstatus%2F1892645856426868884), are personal, self-evolving wiki systems that use Large Language Models (LLMs) to organize research, code documentation, or personal notes. Instead of traditional retrieval methods like [RAG](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) (which uses vector databases), these systems rely on structured Markdown files, interconnected links, and LLM-managed indexes.

### Core Architecture: The "Compiler" Analogy

The system treats knowledge management like software engineering, following a pipeline from raw data to a queryable "executable."

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

Would you like me to help you draft a product requirement document (PRD) to set up your own knowledge base using these principles?

### References

Gist to build your own Karpathy LLM knowledge base:

[https://gist.github.com/karpathy/442a...](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbTBpR3Y1dkR2bUNwZk82bmVGek9mZ1VkRDZnUXxBQ3Jtc0tucGMyM3lJMkNQb1l4SXZhU3h0MzBYbjlXMUc4VjJhZkJiWGZJNVcweGNROUdXeE95N2dZWlV4RFpUVngzMzZmU0k2WEY3aE5aWE1xWno2U1Z4cXg1V1lJRFVybDhUVVA5R2tGTGlQVm1uTDl5dTlZWQ&q=https%3A%2F%2Fgist.github.com%2Fkarpathy%2F442a6bf555914893e9891c11519de94f&v=7huCP6RkcY4)

Karpathy inspired Claude Code memory system repo:

[https://github.com/coleam00/claude-me...](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbmJuTlk1amdCbmEzcDRaeDlvc244V2xJa2U4Z3xBQ3Jtc0trejVWaTMtSkE0ZmpBX2lnbFJHZ3EtaFpTOGtqZ19BaEc3Y2ZBQWlCM1lLakxIb1NOVHJMVjdpX0FnNzU4dWN3WU53OUZPTGNSUTRfYWZZaDJUTXdxQUR4RzVtdmtkLVFESGNLMS1FaWw1SkFIa0FpYw&q=https%3A%2F%2Fgithub.com%2Fcoleam00%2Fclaude-memory-compiler&v=7huCP6RkcY4)