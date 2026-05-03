---
complexity: Advanced
date: 2026-04-26 12:45:00-04:00
id: 34e9fa3b-8750-804f-97d6-cf2651bbc65e
processed_by_ai: true
summary: This document, based on a talk by Matt Pocock, argues that strong software
  fundamentals are more critical than ever when working with AI, countering the idea
  that AI makes code cheap. It identifies four common failure modes in AI-assisted
  development and proposes solutions rooted in established software engineering principles
  like TDD and Domain-Driven Design.
title: Code is Not Cheap Why Your Engineering Skills Matter More Than Ever
tools_mentioned:
- AI
- GitHub
- n8n
- LangGraph
topics:
- Software Engineering Fundamentals
- AI-assisted Development
- Code Quality
- Software Architecture
- Test-Driven Development
- Domain-Driven Design
- Communication with AI
url: https://www.notion.so/Code-is-Not-Cheap-Why-Your-Engineering-Skills-Matter-More-Than-Ever-34e9fa3b8750804f97d6cf2651bbc65e
---

This transcript is based on the talk **"Software Fundamentals Matter More Than Ever"** by [Matt Pocock](https://www.youtube.com/@mattpocockuk) at the [AI Engineer](https://www.youtube.com/@aiDotEngineer) conference.

---

## 🏗️ The Core Thesis: Code is Not Cheap

Many believe in the "specs-to-code" movement—the idea that you can write a specification, let AI generate the code, and never look at the source again. Matt argues this is a fallacy that leads to **"Software Entropy"** and "vibe coding." In reality, **bad code is the most expensive it has ever been** because it prevents you from leveraging the true bounty of AI.

---

## 🛠️ Key Failure Modes & Strategic Solutions

### 1. Misalignment: "The AI didn't do what I wanted"

- **The Problem:** There is a communication barrier between your mental model and the AI's generation.

- **The Concept:** [Frederick Brooks' "Design Concept"](https://en.wikipedia.org/wiki/The_Design_of_Design)—a shared, invisible theory of what is being built.

- **The Skill:** **"Grill Me"** [05:58 Opens in a new window ](http://www.youtube.com/watch?v=v4F1gFy-hqg&t=358).

	- *Action:* Explicitly tell the AI: *"Interview me relentlessly about every aspect of this plan until we reach a shared understanding."*

	- *Result:* The AI may ask 40–100 questions to resolve dependencies before writing a single line of code.

### 2. Verbosity: "Talking at cross purposes"

- **The Problem:** The AI uses too many words or terminology that doesn't align with the domain.

- **The Concept:** [Ubiquitous Language](https://martinfowler.com/bliki/UbiquitousLanguage.html) from Domain-Driven Design (DDD).

- **The Skill:** **Ubiquitous Language Scan** [09:06 Opens in a new window ](http://www.youtube.com/watch?v=v4F1gFy-hqg&t=546).

	- *Action:* Have the AI scan the codebase to create a Markdown glossary of terms.

	- *Result:* Aligning the AI's "thinking traces" with specific domain terms leads to more concise and accurate implementations.

### 3. Execution Failure: "The code just doesn't work"

- **The Problem:** AI often "outruns its headlights" by writing too much code without validation.

- **The Concept:** [Test-Driven Development (TDD)](https://en.wikipedia.org/wiki/Test-driven_development) as a speed limit for development.

- **The Skill:** **AI-Driven TDD** [11:13 Opens in a new window ](http://www.youtube.com/watch?v=v4F1gFy-hqg&t=673).

	- *Action:* Force the AI to write a test first, make it pass, and then refactor.

	- *Result:* Small, deliberate steps ensure the AI doesn't produce massive, buggy "slop."

### 4. Complexity: "I can't keep up with the volume of code"

- **The Problem:** A codebase full of "Shallow Modules" (tiny, complex blobs) is hard for both humans and AI to navigate.

- **The Concept:** [John Ousterhout's "Deep Modules"](https://www.google.com/search?q=https%3A%2F%2Fwww.amazon.com%2FPhilosophy-Software-Design-John-Ousterhout%2Fdp%2F1732102211) [12:48 Opens in a new window ](http://www.youtube.com/watch?v=v4F1gFy-hqg&t=768).

- **The Skill:** **Architectural Refactoring** [14:30 Opens in a new window ](http://www.youtube.com/watch?v=v4F1gFy-hqg&t=870).

	- *Action:* Wrap related logic into "Deep Modules"—large functionality hidden behind simple, stable interfaces.

	- *Result:* You design the interface (Strategic); the AI handles the implementation (Tactical). This saves cognitive load and makes the code more testable.

---

## 🎯 Summary of Recommendations

 | **Practice** | **Old School Root** | **AI Era Application** | 
 | ---- | ---- | ---- | 
 | **Requirements** | *The Design of Design* | Use the **"Grill Me"** prompt to build a shared concept. | 
 | **Terminology** | *Domain-Driven Design* | Maintain a **Ubiquitous Language** Markdown file. | 
 | **Validation** | *The Pragmatic Programmer* | Use **TDD** to keep the AI's "headlights" on the road. | 
 | **Architecture** | *Philosophy of Software Design* | Build **Deep Modules** to delegate implementation safely. | 

---

## 🔗 Resources

- **GitHub Repo:** [Matt Pocock's AI Skills](https://www.google.com/search?q=https%3A%2F%2Fgithub.com%2Fmattpocock%2Fai-skills)

- **Newsletter/Courses:** [AI Hero](https://aihero.dev/)

- **Full Video:** [Code is Not Cheap — Matt Pocock](https://www.youtube.com/watch?v=v4F1gFy-hqg)

> "AI is a great tactical programmer—a sergeant on the ground. You need to be the strategic leader above it, and that requires software fundamentals." [17:32 Opens in a new window](http://www.youtube.com/watch?v=v4F1gFy-hqg&t=1052)

Given your interest in **AI-assisted systems** and **architectural health**, do you want to explore how to integrate these "Grill Me" or "Ubiquitous Language" workflows into your specific n8n or LangGraph projects?

<br/>