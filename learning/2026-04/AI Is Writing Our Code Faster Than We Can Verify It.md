---
complexity: Intermediate
date: 2026-04-15
id: 3439fa3b-8750-809c-a826-dfa2effc9166
processed_by_ai: true
summary: This article by Andrew Stellman discusses the "verification gap" in AI-assisted
  software development, where AI generates code faster than humans can verify it.
  It proposes Quality Engineering, enhanced by AI, as a solution to automate quality
  assurance and build trust in AI-generated code.
title: AI Is Writing Our Code Faster Than We Can Verify It
tools_mentioned:
- Quality Playbook
- GitHub Copilot
- Cursor
- Claude Code
topics:
- AI-assisted software development
- Software quality
- Quality Engineering
- Code verification
- AI agents
url: https://www.notion.so/AI-Is-Writing-Our-Code-Faster-Than-We-Can-Verify-It-3439fa3b8750809ca826dfa2effc9166
---

The article **["AI Is Writing Our Code Faster Than We Can Verify It"](https://www.oreilly.com/radar/ai-is-writing-our-code-faster-than-we-can-verify-it/)** by Andrew Stellman explores the growing "verification gap" in AI-assisted software development. As AI agents generate code at unprecedented speeds, human developers are struggling to keep pace with quality assurance, leading to a breakdown in trust.

### The Core Problem: A False Choice

Stellman argues that many senior developers feel trapped between two "terrible" options:

- **Cognitive Surrender:** Blindly trusting the AI and "vibe coding," which often leads to production failures.

- **Manual Line-by-Line Review:** Reviewing every line of AI-generated code, which is so labor-intensive it negates the productivity gains of using AI in the first place.

### The Solution: Quality Engineering (QE)

The author suggests that the answer lies in **Quality Engineering**, a discipline established in the 1960s to solve the "software crisis." While QE was historically abandoned by many teams because it was perceived as too expensive or slow, AI now makes these robust practices "cheap" to implement.

The article introduces the **[Quality Playbook](https://www.google.com/search?q=https%3A%2F%2Fgithub.com%2Fstellman%2Fquality-playbook)**, an open-source AI skill designed for tools like GitHub Copilot, Cursor, and Claude Code. It automates the creation of "quality infrastructure" by:

- **Extracting Intent:** Inferring what the code *should* do from READMEs, chat logs, and schemas.

- **Traceability:** Linking requirements directly to functional tests.

- **Multi-Model Audits:** Using a "Council of Three" (three independent AI models) to audit code against requirements to reduce hallucinations.

### Key Deliverables of the Playbook

The playbook generates ten specific artifacts to ensure code quality, including:

- **REQUIREMENTS.md:** A source of truth for project intent.

- **QUALITY.md:** A project-specific "constitution" defining what "correct" looks like.

- **AGENTS.md:** A bootstrap file that ensures future AI sessions inherit the existing quality context.

---

**Would you like me to explain how to integrate the ****[Quality Playbook](https://www.google.com/search?q=https%3A%2F%2Fgithub.com%2Fstellman%2Fquality-playbook)**** into your current development workflow?**