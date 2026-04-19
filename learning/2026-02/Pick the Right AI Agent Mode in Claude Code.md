---
complexity: Intermediate
date: 2026-02-13
id: 3069fa3b-8750-8026-9b7a-e5c569f1349a
processed_by_ai: true
summary: 'This document compares three modes of operation: Skills, Sub-agents, and
  Agent Teams, detailing their features, communication patterns, token costs, and
  complexity. It provides guidance on when to use each mode and when to transition
  between them based on task requirements and resource constraints.'
title: Pick the Right AI Agent Mode in Claude Code
tools_mentioned: []
topics:
- AI Agents
- Agent Orchestration
- Context Management
- Communication Patterns
- Token Cost Optimization
- Workflow Management
url: https://www.notion.so/Pick-the-Right-AI-Agent-Mode-in-Claude-Code-3069fa3b875080269b7ae5c569f1349a
---

<br/>

### **The Three Modes at a Glance**

 | **Feature** | **Skills** | **Sub-agents** | **Agent Teams** | 
 | ---- | ---- | ---- | ---- | 
 | **Context** | Shared in main chat session [01:31 Opens in a new window](http://www.youtube.com/watch?v=8Sz7OleIb04&t=91) | Isolated per worker [02:23 Opens in a new window](http://www.youtube.com/watch?v=8Sz7OleIb04&t=143) | Isolated per teammate [04:18 Opens in a new window](http://www.youtube.com/watch?v=8Sz7OleIb04&t=258) | 
 | **Communication** | Direct (one session) [01:44 Opens in a new window](http://www.youtube.com/watch?v=8Sz7OleIb04&t=104) | Relay through lead only [02:43 Opens in a new window](http://www.youtube.com/watch?v=8Sz7OleIb04&t=163) | Direct peer-to-peer [04:01 Opens in a new window](http://www.youtube.com/watch?v=8Sz7OleIb04&t=241) | 
 | **Token Cost** | Lowest [15:41 Opens in a new window](http://www.youtube.com/watch?v=8Sz7OleIb04&t=941) | Moderate [15:48 Opens in a new window](http://www.youtube.com/watch?v=8Sz7OleIb04&t=948) | Highest (can be very high) [15:59 Opens in a new window](http://www.youtube.com/watch?v=8Sz7OleIb04&t=959) | 
 | **Complexity** | Simple setup [17:15 Opens in a new window](http://www.youtube.com/watch?v=8Sz7OleIb04&t=1035) | High orchestration effort [17:31 Opens in a new window](http://www.youtube.com/watch?v=8Sz7OleIb04&t=1051) | Very high (beta feature) [18:17 Opens in a new window](http://www.youtube.com/watch?v=8Sz7OleIb04&t=1097) | 

---

### **When to Use Each Mode**

### **1. Skills (The Starting Point)** [00:42 Opens in a new window](http://www.youtube.com/watch?v=8Sz7OleIb04&t=42)

- **Ideal for:** One-shot tasks, methodology-based workflows (e.g., standard research or coding patterns), and when speed is a priority [06:13 Opens in a new window ](http://www.youtube.com/watch?v=8Sz7OleIb04&t=373).

- **Pro Tip:** Use skills by default until you hit context limits or need specialized tool restrictions [13:18 Opens in a new window ](http://www.youtube.com/watch?v=8Sz7OleIb04&t=798).

### **2. Sub-agents (Isolated Workers)** [01:50 Opens in a new window](http://www.youtube.com/watch?v=8Sz7OleIb04&t=110)

- **Ideal for:** Heavy file reads, independent research, or tasks requiring specific tool permissions [08:22 Opens in a new window ](http://www.youtube.com/watch?v=8Sz7OleIb04&t=502).

- **Constraint:** Sub-agents **cannot** talk to each other; they only report back to the main "orchestrator" session [02:43 Opens in a new window ](http://www.youtube.com/watch?v=8Sz7OleIb04&t=163).

### **3. Agent Teams (Collaborative Specialists)** [03:43 Opens in a new window](http://www.youtube.com/watch?v=8Sz7OleIb04&t=223)

- **Ideal for:** Researching and challenging hypotheses, building new modules, or scenarios where specialists need to debate [09:33 Opens in a new window ](http://www.youtube.com/watch?v=8Sz7OleIb04&t=573).

- **Key Advantage:** Teammates can discuss and iterate among themselves without the lead being a bottleneck [10:41 Opens in a new window ](http://www.youtube.com/watch?v=8Sz7OleIb04&t=641).

---

### **When to "Level Up"** [20:48 Opens in a new window](http://www.youtube.com/watch?v=8Sz7OleIb04&t=1248)

- **Shift from Skill → Sub-agent:** When your context window is filling up too fast, or outputs are too verbose for the main thread [21:00 Opens in a new window ](http://www.youtube.com/watch?v=8Sz7OleIb04&t=1260).

- **Shift from Sub-agent → Agent Team:** When workers need to collaborate directly or when the "relay" through the main session becomes a bottleneck [21:32 Opens in a new window ](http://www.youtube.com/watch?v=8Sz7OleIb04&t=1292).

- **Shift Back to Skills/Sub-agents:** If the **token cost** becomes unsustainable or if the coordination overhead exceeds the benefits of parallelism [25:04 Opens in a new window ](http://www.youtube.com/watch?v=8Sz7OleIb04&t=1504).