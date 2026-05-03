---
complexity: Intermediate
date: 2026-03-16
id: 3259fa3b-8750-8019-b027-df5ab1218aa4
processed_by_ai: true
summary: This document explores Andrej Karpathy's Autoresearch project, which uses
  AI agents in "Agentic Loops" to autonomously conduct research by iteratively editing
  code, running experiments, and committing improvements. It argues that these loops
  are a new fundamental building block for work across various industries, shifting
  human roles to strategic guidance.
title: Autoresearch Agent Loops and the Future of Work
tools_mentioned:
- Autoresearch
- GitHub
topics:
- Autoresearch
- Agentic Loops
- AI Agents
- Autonomous Research
- Software Development
- Automation
- Future of Work
url: https://www.notion.so/Autoresearch-Agent-Loops-and-the-Future-of-Work-3259fa3b87508019b027df5ab1218aa4
---

This video explores Andrej Karpathy's latest project, **Autoresearch**, and the broader concept of **Agentic Loops** as a fundamental new building block for work.

### **The Core Concept: Autoresearch**

- **The Project:** Karpathy released a minimal GitHub repository designed for autonomous AI research [01:52 Opens in a new window ](http://www.youtube.com/watch?v=nt9j1k2IhUY&t=112).

- **The "Loop":** An agent edits training code (`train.py`), runs a fixed **5-minute experiment**, evaluates the result against a specific metric (Validation Bits Per Byte), and only commits the changes if they improve the score [02:12 Opens in a new window ](http://www.youtube.com/watch?v=nt9j1k2IhUY&t=132).

- **Human's New Role:** Instead of manual coding, the human writes a "memo" or strategy document (`program.md`) that guides the agent's research approach [06:18 Opens in a new window ](http://www.youtube.com/watch?v=nt9j1k2IhUY&t=378).

### **The Shift to "Agentic Loops"**

The video argues that these loops are becoming a "work primitive"—a basic building block used across all industries [01:12 Opens in a new window ](http://www.youtube.com/watch?v=nt9j1k2IhUY&t=72):

- **Ralph Wiggum Loop:** A similar iterative software development loop that builds code persistently, clearing its context window periodically to avoid performance degradation [09:09 Opens in a new window ](http://www.youtube.com/watch?v=nt9j1k2IhUY&t=549).

- **Beyond Research:** This pattern is being applied to:

	- **Marketing:** Running thousands of ad variations and landing page tests automatically [12:06 Opens in a new window ](http://www.youtube.com/watch?v=nt9j1k2IhUY&t=726).

	- **Sales:** Targeting leads and refining outreach scripts overnight [16:08 Opens in a new window ](http://www.youtube.com/watch?v=nt9j1k2IhUY&t=968).

	- **Business Operations:** Automating any task that has a clear, objective score and fast feedback [13:30 Opens in a new window ](http://www.youtube.com/watch?v=nt9j1k2IhUY&t=810).

### **Requirements for a Successful Loop**

For a process to be effectively automated via an agentic loop, it typically needs:

1. **A Score:** A way to objectively tell "better" from "worse" without human input [13:48 Opens in a new window ](http://www.youtube.com/watch?v=nt9j1k2IhUY&t=828).

1. **Fast/Cheap Iterations:** Minutes, not months [14:04 Opens in a new window ](http://www.youtube.com/watch?v=nt9j1k2IhUY&t=844).

1. **Bounded Environment:** A defined workspace for the agent [14:10 Opens in a new window ](http://www.youtube.com/watch?v=nt9j1k2IhUY&t=850).

1. **Low Cost of Failure:** Bad iterations shouldn't cause significant damage [14:14 Opens in a new window ](http://www.youtube.com/watch?v=nt9j1k2IhUY&t=854).

### **The Future: Collaborative Swarms**

The next phase involves **synchronous collaboration** where swarms of agents share learnings [17:22 Opens in a new window ](http://www.youtube.com/watch?v=nt9j1k2IhUY&t=1042). Unlike human academia where failed experiments are often buried, an agent network can use every failure to prune the search tree for all other agents [18:39 Opens in a new window ](http://www.youtube.com/watch?v=nt9j1k2IhUY&t=1119).

Watch the full breakdown on YouTube: [Autoresearch, Agent Loops and the Future of Work](http://www.youtube.com/watch?v=nt9j1k2IhUY)