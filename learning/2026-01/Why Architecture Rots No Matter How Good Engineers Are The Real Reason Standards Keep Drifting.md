---
complexity: Advanced
date: 2026-01-28 19:05:00-05:00
id: 2f79fa3b-8750-802a-9016-d798a617c30d
processed_by_ai: true
summary: This document explores the reasons behind software architecture degradation,
  such as the "Cathedral and Brick" problem and loss of context. It then discusses
  how AI, particularly Large Language Models, can help maintain architectural integrity
  through massive context windows and tireless consistency, while also outlining areas
  where human judgment remains crucial.
title: Why Architecture Rots No Matter How Good Engineers Are The Real Reason Standards
  Keep Drifting
tools_mentioned:
- LLMs
topics:
- Software Architecture
- Technical Debt
- Code Review
- Large Language Models
- AI in Software Development
- System Design
url: https://www.notion.so/Why-Architecture-Rots-No-Matter-How-Good-Engineers-Are-The-Real-Reason-Standards-Keep-Drifting-2f79fa3b8750802a9016d798a617c30d
---

### Why Architecture Rots

- **The "Cathedral and Brick" Problem:** Engineers cannot hold the entire "cathedral" (system design) in mind while laying a single "brick" (line of code) [03:48 Opens in a new window ](http://www.youtube.com/watch?v=NoRePxSrhpw&t=228).

- **Invisible Local Decisions:** Small, reasonable changes—like adding a global click listener to a reusable hook—create systemic failures (e.g., 100 listeners firing at once) that no one person can see coming [05:21 Opens in a new window ](http://www.youtube.com/watch?v=NoRePxSrhpw&t=321).

- **Lossy Context Transfer:** As teams scale and people leave, documentation becomes outdated, and the "why" behind complex patterns disappears [10:34 Opens in a new window ](http://www.youtube.com/watch?v=NoRePxSrhpw&t=634).

### The AI Advantage: Structural Vigilance

- **Massive Context Windows:** Modern LLMs can "hold" 200k+ tokens, allowing them to cross-reference an entire codebase during a single code review [12:04 Opens in a new window ](http://www.youtube.com/watch?v=NoRePxSrhpw&t=724).

- **Tireless Consistency:** Unlike humans, AI doesn't suffer from "deadline pressure" or "cognitive fatigue" on its 47th PR of the week [16:41 Opens in a new window ](http://www.youtube.com/watch?v=NoRePxSrhpw&t=1001).

- **Global-Local Reasoning:** AI can see "the forest and the trees" simultaneously, enforcing high-level architectural rules while reviewing line-by-line changes [15:19 Opens in a new window ](http://www.youtube.com/watch?v=NoRePxSrhpw&t=919).

### Where Humans Still Lead

- **Novel Decisions:** AI struggles to invent net-new patterns and relies on prior examples [17:31 Opens in a new window ](http://www.youtube.com/watch?v=NoRePxSrhpw&t=1051).

- **Business Trade-offs:** AI can flag technical debt but can't decide if shipping faster is the right business move [18:16 Opens in a new window ](http://www.youtube.com/watch?v=NoRePxSrhpw&t=1096).

- **Cross-System Context:** Knowing which team owns a service or remembering a specific failure from a "Black Friday" event remains a human strength [18:43 Opens in a new window ](http://www.youtube.com/watch?v=NoRePxSrhpw&t=1123).