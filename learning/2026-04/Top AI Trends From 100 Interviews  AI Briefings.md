---
complexity: Advanced
date: 2026-04-27
id: 34f9fa3b-8750-80c4-9062-cd7aa113c9ae
processed_by_ai: true
summary: This document summarizes a discussion on the evolving role of developers
  in the age of AI and introduces nWave, an open-source AI development system that
  leverages specialized agents to assist with software engineering, emphasizing behavioral
  engineering and iterative specification.
title: Top AI Trends From 100 Interviews  AI Briefings
tools_mentioned:
- nWave
- Anthropic's Claude
topics:
- AI in Software Engineering
- Developer Role Shift
- AI Agents
- Software Architecture
- Continuous Delivery
- Test-Driven Development
- Iterative Development
- Behavioral Engineering
url: https://www.notion.so/Top-AI-Trends-From-100-Interviews-AI-Briefings-34f9fa3b875080c49062cd7aa113c9ae
---

This transcript summary from the [Modern Software Engineering](https://www.youtube.com/@ModernSoftwareEngineeringYT) video, **"Top AI Trends From 100 Interviews | AI Briefings: nWave,"** explores the shifting role of developers and the introduction of the nWave AI development system.

---

## 🏗️ The Changing Role of the Developer

Dave Farley opens by arguing that AI has already profoundly disrupted software engineering.

- **The Shift:** If your core skill was simply translating a description into code, AI can now do that faster and more cheaply [01:00 Opens in a new window ](http://www.youtube.com/watch?v=8WJ1XVBh8NA&t=60).

- **New Focus:** Developers must refocus on building an understanding of the problem and "behavioral engineering"—communicating, understanding context, and describing problems in verifiable detail [04:45 Opens in a new window ](http://www.youtube.com/watch?v=8WJ1XVBh8NA&t=285).

- **Human "Taste":** Humans remain essential for providing broad context, architecture, and engineering "taste," especially for high-stakes systems involving finance or privacy [08:20 Opens in a new window ](http://www.youtube.com/watch?v=8WJ1XVBh8NA&t=500).

---

## 🌊 Introducing nWave: Agents as Teammates

[nWave](https://www.google.com/search?q=https%3A%2F%2Fgithub.com%2Fnwave-io%2Fnwave) is an open-source AI development system (currently running on Anthropic’s Claude) that treats AI agents as members of a development team [02:40 Opens in a new window ](http://www.youtube.com/watch?v=8WJ1XVBh8NA&t=160).

### Key Principles of nWave:

- **Opinionated Framework:** It supports high-level engineering principles like **Hexagonal Architecture**, **Continuous Delivery**, and **Double-Loop TDD** [16:54 Opens in a new window ](http://www.youtube.com/watch?v=8WJ1XVBh8NA&t=1014).

- **Behavioral Engineering:** Agents are designed with specific "personalities" and boundaries to reduce hallucinations and ensure single-responsibility (SOLID principles) [13:34 Opens in a new window ](http://www.youtube.com/watch?v=8WJ1XVBh8NA&t=814).

- **Iterative Specification:** Instead of "Big Design Up Front," it uses a "micro-spec" or "Fine-grained Iterative Specification" approach, inspired by the "Elephant Carpaccio" exercise [10:13 Opens in a new window ](http://www.youtube.com/watch?v=8WJ1XVBh8NA&t=613).

---

## 🛠️ The nWave Multi-Agent System

The creators, Mike and Alessandro, explain that nWave utilizes an orchestrator to manage a diverse team of specialized agents [14:52 Opens in a new window ](http://www.youtube.com/watch?v=8WJ1XVBh8NA&t=892):

- **Scale:** At the time of recording, the system includes **23 agents** with over **90 specialized skills** [17:02 Opens in a new window ](http://www.youtube.com/watch?v=8WJ1XVBh8NA&t=1022).

- **Orchestration:** A central orchestrator ensures that agents stay in their "roles" (e.g., preventing a "Crafter" agent from making high-level architectural decisions) [15:18 Opens in a new window ](http://www.youtube.com/watch?v=8WJ1XVBh8NA&t=918).

- **Small Steps:** The workflow forces developers to break features into small, manageable waves, facilitating a process of discovery rather than just code generation [12:11 Opens in a new window ](http://www.youtube.com/watch?v=8WJ1XVBh8NA&t=731).

---

## 💡 Practical Advice for AI-Assisted Dev

- **Avoid "Vibe Coding":** While "vibe coding" works for simple personal apps, professional systems require discipline, observability, and logging to prevent untraceable outages [07:06 Opens in a new window ](http://www.youtube.com/watch?v=8WJ1XVBh8NA&t=426).

- **Don't Skip the Code:** The creators recommend never deploying AI-generated code to production without a human review [09:17 Opens in a new window ](http://www.youtube.com/watch?v=8WJ1XVBh8NA&t=557).

- **Small Iterations:** The primary value of these tools is the ability to iterate quickly and test ideas in small, verifiable steps [11:34 Opens in a new window ](http://www.youtube.com/watch?v=8WJ1XVBh8NA&t=694).

---

> **Note:** For more on Dave Farley's approach to TDD and engineering, you can check his [official course link](https://courses.cd.training/courses/tdd-bdd-design-through-testing-team?coupon=tdd-ai-30) mentioned in the video description.