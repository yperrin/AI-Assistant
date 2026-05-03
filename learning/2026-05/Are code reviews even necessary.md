---
complexity: Advanced
date: 2026-05-02 15:40:00-04:00
id: 3549fa3b-8750-80aa-8072-dd43e17ad801
processed_by_ai: true
summary: This document redefines code reviews, moving beyond traditional bottlenecks
  to address specific purposes like policy adherence, knowledge sharing, and design
  alignment. It explores how practices like pair programming and AI-generated code
  shift the focus of human review towards intent verification and high-level critiques.
title: Are code reviews even necessary
tools_mentioned:
- linters
- static analysis
- Architecture Decision Record (ADR)
- PHP
- WordPress
topics:
- Code Review
- Software Development Practices
- Pair Programming
- AI in Software Development
- Regulatory Compliance
- Team Collaboration
- Architecture Decision Records
url: https://www.notion.so/Are-code-reviews-even-necessary-3549fa3b875080aa8072dd43e17ad801
---

---

### 1. Executive Summary

- **The "Purpose" Problem:** Many teams perform code reviews out of "cargo cultism" or regulatory boxes without understanding the specific goal, leading to significant bottlenecks.

- **Pairing vs. Reviewing:** While pairing often removes the need for traditional reviews by providing real-time feedback, separate "critiques" can still provide high-level design alignment.

- **AI's Impact:** With AI generating up to [90% of code](http://www.youtube.com/watch?v=6AxuSfSe4BA), the human role shifts toward "rubber ducking," verifying intent, and ensuring code ownership rather than line-by-line bug hunting.

- **Modern Framework:** The video defines three distinct types of reviews: **Policy** (rules of the road), **Show and Tell** (knowledge sharing), and **Critique** (design alignment).

---

### 2. Detailed Transcription

> **Note:** This transcription captures the full body of the conversation as provided in the [original source](http://www.youtube.com/watch?v=6AxuSfSe4BA).

1. **Gateway Reviews:** Checking if code is safe for the next level (common in finance).

1. **Knowledge Sharing:** Reviewing after merging to share changes across the team.

1. **Collaborative Evolution:** Reviewing iteratively as you commit, evolving the design together.

- **Policy:** "Rules of the road"—checking against regulatory or local idioms.

- **Show and Tell:** "Harvest and amplify"—spotting cool solutions and broadcasting them to become the new policy.

- **Critique:** Used for alignment on big new features or risky design approaches, not for every bug fix.

---

### 3. Use Case & Solution Index

### Use Case: High-Trust/XP Engineering Teams

- **Problem:** Traditional pull requests slow down development and signal a lack of trust.

- **Solution:** **Pair Programming.** Two people solve the problem in real-time, providing continuous feedback. The "driver/navigator" metaphor is discarded for "two people solving a puzzle." [04:52 Opens in a new window](http://www.youtube.com/watch?v=6AxuSfSe4BA&t=292)

### Use Case: Regulatory/Compliance Environments

- **Problem:** Need to prove to auditors/regulators that code has been checked.

- **Solution:** **Policy Reviews.** Focus purely on the "rules of the road"—pre-defined regulatory standards and local idioms. Automate as much as possible through linters and static analysis. [20:23 Opens in a new window](http://www.youtube.com/watch?v=6AxuSfSe4BA&t=1223)

### Use Case: Team Design Alignment

- **Problem:** Different pairs solve the same problem in three different ways (e.g., modeling a trade).

- **Solution:** **Out-of-Band Critiques.** The team reviews multiple implementations of the same idea to create a unified "integrated version" and captures it in an **Architecture Decision Record (ADR)**. [09:57 Opens in a new window](http://www.youtube.com/watch?v=6AxuSfSe4BA&t=597)

### Use Case: Mentorship & Training

- **Problem:** Juniors struggle to understand complex senior code or lack exposure to senior decision-making.

- **Solution:** **Inverted Power Structure.** Juniors review senior code. If a junior doesn't understand it, the code isn't "readable." This serves as a powerful learning rubric for the junior and a quality check for the senior. [36:54 Opens in a new window](http://www.youtube.com/watch?v=6AxuSfSe4BA&t=2214)

### Use Case: Working with AI Agents

- **Problem:** AI generates a high volume of code that may include "janky" or unoptimized sections.

- **Solution:** **Sophisticated Rubber Ducking.** Use the AI for "technology adjacent" tasks (e.g., writing specific PHP scripts for WordPress). Scan the output for "smells" (e.g., too many global variables) rather than line-by-line verification. [30:10 Opens in a new window](http://www.youtube.com/watch?v=6AxuSfSe4BA&t=1810)