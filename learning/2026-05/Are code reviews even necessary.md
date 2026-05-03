---
complexity: Intermediate
date: 2026-05-02 15:40:00-04:00
id: 3549fa3b-8750-80aa-8072-dd43e17ad801
processed_by_ai: true
summary: This document re-evaluates the necessity and purpose of code reviews in modern
  software development, considering high-performing teams, XP practices, and the impact
  of AI agents. It identifies a shift from gatekeeping to more collaborative, purpose-driven
  review activities, categorizing them into Policy, Show and Tell, and Critique.
title: Are code reviews even necessary
tools_mentioned:
- WordPress
- PHP
topics:
- Code Reviews
- Extreme Programming (XP)
- Pair Programming
- AI in Software Development
- Software Development Practices
- Team Collaboration
- Regulatory Compliance
- Mentorship
url: https://www.notion.so/Are-code-reviews-even-necessary-3549fa3b875080aa8072dd43e17ad801
---

This document analyzes the [Are Code Reviews Even Necessary?](http://www.youtube.com/watch?v=6AxuSfSe4BA) video featuring **Trisha Gee** and **Daniel North**.

---

### 1. Executive Summary

The central theme of this discussion is a re-evaluation of code reviews in the context of high-performing teams, [XP (Extreme Programming)](http://www.youtube.com/watch?v=6AxuSfSe4BA) practices, and the rise of [AI agents](http://www.youtube.com/watch?v=6AxuSfSe4BA). The speakers identify a shift from code reviews as "gatekeeping" to more collaborative, purpose-driven activities.

**Key Takeaways:**

- **The "Purpose" Problem:** Many teams perform code reviews out of "cargo cultism" or regulatory boxes without understanding the specific goal, leading to significant bottlenecks.

- **Pairing vs. Reviewing:** While pairing often removes the need for traditional reviews by providing real-time feedback, separate "critiques" can still provide high-level design alignment.

- **AI's Impact:** With AI generating up to [90% of code](http://www.youtube.com/watch?v=6AxuSfSe4BA), the human role shifts toward "rubber ducking," verifying intent, and ensuring code ownership rather than line-by-line bug hunting.

- **Modern Framework:** The video defines three distinct types of reviews: **Policy** (rules of the road), **Show and Tell** (knowledge sharing), and **Critique** (design alignment).

---

### 2. Detailed Transcription

> **Note:** This transcription captures the full body of the conversation as provided in the [original source](http://www.youtube.com/watch?v=6AxuSfSe4BA).

**Defining Purpose & The Pairing Debate** [00:00 Opens in a new window ](http://www.youtube.com/watch?v=6AxuSfSe4BA&t=0) **Trisha Gee:** Welcome to one big question. I'm chatting with Daniel North about code reviews. Are they necessary?

[00:25 Opens in a new window ](http://www.youtube.com/watch?v=6AxuSfSe4BA&t=25) **Daniel North:** Let's start with purpose. One trope I've heard is: if you're pairing, you don't need a code review. What's your take?

[01:11 Opens in a new window ](http://www.youtube.com/watch?v=6AxuSfSe4BA&t=71) **Trisha Gee:** In XP teams, we didn't do code reviews because we paired. Pairing is about finding the best design iteratively. Traditional code reviews are often gatekeeping—a senior architect asking, "Are there any bugs?" with a default mindset of "no, this code is not ready."

**The Three Patterns of Code Review** [12:06 Opens in a new window ](http://www.youtube.com/watch?v=6AxuSfSe4BA&t=726) **Trisha Gee:** I've identified three main reasons for code reviews:

1. **Gateway Reviews:** Checking if code is safe for the next level (common in finance).

1. **Knowledge Sharing:** Reviewing after merging to share changes across the team.

1. **Collaborative Evolution:** Reviewing iteratively as you commit, evolving the design together.

[20:23 Opens in a new window ](http://www.youtube.com/watch?v=6AxuSfSe4BA&t=1223) **Daniel North:** I have similar names for these:

- **Policy:** "Rules of the road"—checking against regulatory or local idioms.

- **Show and Tell:** "Harvest and amplify"—spotting cool solutions and broadcasting them to become the new policy.

- **Critique:** Used for alignment on big new features or risky design approaches, not for every bug fix.

**The Role of AI & "Embarrassment Driven Refactoring"** [14:19 Opens in a new window ](http://www.youtube.com/watch?v=6AxuSfSe4BA&t=859) **Trisha Gee:** With AI agents, we are collaborating on individual commits. We're learning to review in a way that's more like pairing.

[18:12 Opens in a new window ](http://www.youtube.com/watch?v=6AxuSfSe4BA&t=1092) **Daniel North:** I call it "Embarrassment Driven Refactoring." You start with janky code, then iterate until you're no longer embarrassed to hand it over. AI is a sophisticated "rubber duck." It's great for "technology adjacent" problems—things like modern CSS or PHP that I could learn but can't be bothered to.

**The Bottleneck Problem** [34:51 Opens in a new window ](http://www.youtube.com/watch?v=6AxuSfSe4BA&t=2091) **Trisha Gee:** If AI creates 10x more code, code reviews become a huge bottleneck if we require humans to read every line. We must ask: "In order to what?" If it's just to check a box, we're doing it wrong.

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