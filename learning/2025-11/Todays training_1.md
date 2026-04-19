---
complexity: Advanced
date: 2025-11-05 20:29:00-05:00
id: 2a39fa3b-8750-80ab-809e-e7b6cc664566
processed_by_ai: true
summary: This document outlines 10 advanced prompting techniques for AI models, categorized
  into building self-correction systems, meta prompting, reasoning scaffolds, and
  perspective engineering. It covers methods like Chain of Verification, Adversarial
  Prompting, Reverse Prompting, and Multi-Persona Debate to enhance AI output quality
  and reasoning.
title: Todays training
tools_mentioned:
- sub-agents
- Plan Mode
topics:
- AI Prompting
- Prompt Engineering
- Large Language Models
- Self-Correction
- Reasoning Scaffolds
- Meta Prompting
- Perspective Engineering
url: https://www.notion.so/Today-s-training-2a39fa3b875080ab809ee7b6cc664566
---

- **Context-isolated sub-agents**: Subagents let you delegate focused tasks (e.g., running TDD workflows, conducting research) that can be solved independently from your main chat for context-optimized token usage.

- **Plan Mode**: Create, refine, and execute step-by-step implementation plans. Plan Mode analyzes your codebase, generates detailed execution plans, and validates that requirements are covered before starting to code.

### 1. Building Self-Correction Systems

- **Chain of Verification ****[00:59 Opens in a new window ](http://www.youtube.com/watch?v=GTEz5WWbfiw&t=59)****:** Structuring the prompt to include a mandatory verification loop where the model analyzes its own initial output, identifies incompleteness or errors, cites specific language, and then revises its findings.

- **Adversarial Prompting ****[01:50 Opens in a new window ](http://www.youtube.com/watch?v=GTEz5WWbfiw&t=110)****:** Demanding that the model actively "attacks" a previous design or solution to identify vulnerabilities and find problems, even if it has to stretch, ensuring a more complete review (e.g., for security architecture).

- **Strategic Edge-case Learning (Few-shot examples) ****[02:43 Opens in a new window ](http://www.youtube.com/watch?v=GTEz5WWbfiw&t=163)****:** Including examples of common failure modes and boundary cases within the prompt to teach the model how to distinguish subtle "gray spaces" and reduce false negatives.

### 2. Meta Prompting

- **Reverse Prompting ****[04:42 Opens in a new window ](http://www.youtube.com/watch?v=GTEz5WWbfiw&t=282)****:** Asking the model to act as an expert prompt designer, define the single most effective prompt for a defined task (including details, format, and reasoning steps), and then execute that prompt on the provided data.

- **Recursive Prompt Optimization ****[05:53 Opens in a new window ](http://www.youtube.com/watch?v=GTEz5WWbfiw&t=353)****:** Giving the model a multi-iteration task (e.g., "Version 1: add missing constraints," "Version 2: resolve ambiguities") in a single pass to force it to refine the prompt structure based on specific axes you define.

### 3. Reasoning Scaffolds

- **Deliberate Over-Instruction ****[07:05 Opens in a new window ](http://www.youtube.com/watch?v=GTEz5WWbfiw&t=425)****:** Countering the model's default tendency to be concise by explicitly instructing it to "Do not summarize" and expanding every point with exhaustive depth, such as implementation details, edge cases, and historical context.

- **Zero-Shot Chain of Thought Structure ****[08:17 Opens in a new window ](http://www.youtube.com/watch?v=GTEz5WWbfiw&t=497)****:** Providing a template with a sequence of blank steps (like questions) that forces the model to decompose the problem and structure its thinking around the scaffolding you laid out, often effective for technical or quantitative problems.

- **Reference Class Priming ****[09:20 Opens in a new window ](http://www.youtube.com/watch?v=GTEz5WWbfiw&t=560)****:** Providing an example of high-quality reasoning (as opposed to an input/output pair) and asking the model to match that explicit standard of quality, which pushes the model toward a desired level of depth and consistency.

### 4. Perspective Engineering

- **Multi-Persona Debate ****[10:40 Opens in a new window ](http://www.youtube.com/watch?v=GTEz5WWbfiw&t=640)****:** Instantiating multiple "experts" with specific, potentially conflicting priorities, requiring them to debate their preferences and critique the others' positions, and finally synthesizing a recommendation that addresses all concerns.

- **Temperature Simulation (Roleplaying) ****[12:03 Opens in a new window ](http://www.youtube.com/watch?v=GTEz5WWbfiw&t=723)****:** Using roleplaying personas (e.g., "junior analyst who is uncertain" vs. "confident expert who is concise") to simulate low- and high-temperature passes, then asking the model to synthesize the results to highlight where uncertainty is warranted.

---

- **Title:** The Mental Models of Master Prompters: 10 Techniques for Advanced Prompting

- **Channel:** [AI News & Strategy Daily | Nate B Jones](http://www.youtube.com/watch?v=GTEz5WWbfiw)