---
complexity: Intermediate
date: 2026-02-01 10:05:00-05:00
id: 2fa9fa3b-8750-8018-ba91-d3343b016c37
processed_by_ai: true
summary: This document discusses the challenges of evaluating AI/LLM systems, distinguishing
  between offline and online quality, and how traditional testing methods often fall
  short. It emphasizes the importance of continuous improvement through a feedback
  loop, highlighting how real user behavior can surprise developers and necessitate
  a robust evaluation "flywheel."
title: Evals are not all you need
tools_mentioned: []
topics:
- AI System Evaluation
- Offline Quality
- Online Quality
- Continuous Improvement
- LLM Evaluation
- User Behavior
- Product Testing
url: https://www.notion.so/Evals-are-not-all-you-need-2fa9fa3b87508018ba91d3343b016c37
---

- **Offline quality**: A way to estimate how it behaves while you’re still developing it, before any customer sees it

- **Online quality**: Signals for how it’s actually performing once real customers are using it

- **Continuous improvement**: A reliable feedback loop that lets you find problems, fix them, and get better over time

## **Why Traditional Testing Breaks**

- **Offline quality?** You write unit tests and integration tests before launch to verify behavior.

- **Online quality?** You monitor production for errors and exceptions. When something
breaks, you get a stack trace that tells you exactly what went wrong.

- **Continuous improvement?** It’s almost automatic. You write a new test, fix the bug, and ship.
When you fix something, it stays fixed. Find issue, fix issue, move on.

## **Model Versus Product**

![Evaluation.png](https://www.oreilly.com/radar/wp-content/uploads/sites/3/2026/01/Evaluation.png)

## **What You Measure Against**

- **Excellent**: Resolves the issue completely in one response, uses clear language, offers next steps if relevant

- **Adequate**: Answers the question but requires follow-up or includes unnecessary information

- **Poor**: Misunderstands the question, gives irrelevant information, or fails to address the core issue

## **How You Measure**

![image-7.png](https://www.oreilly.com/radar/wp-content/uploads/sites/3/2026/01/image-7.png)

## **Production Surprises You (and Humbles You)**

- **Your reference examples don’t cover what users actually ask.** You anticipated questions about return policies, shipping times, and
order status. But users ask about things you didn’t include: “Can I
return this if my dog chewed on the box?“ or “My package says delivered
but I never got it, and also I’m moving next week.“ They combine
multiple issues in one message. They reference previous conversations.
They phrase things in ways your reference examples never captured.

- **Users find scenarios you missed.** Maybe your bot handles refund requests well but struggles when users
ask about partial refunds on bundled items. Maybe it works fine in
English but breaks when users mix in Spanish. No matter how thorough
your prelaunch testing, real users will find gaps.

- **User behavior shifts over time.** The questions you get in month one don’t look like the questions you
get in month six. Users learn what the bot can and can’t do. They
develop workarounds. They find new use cases. Your reference examples
were a snapshot of expected behavior, but expected behavior changes.

## **The Flywheel**

![image-8.png](https://www.oreilly.com/radar/wp-content/uploads/sites/3/2026/01/image-8.png)

## **So What Are “Evals“?**

- “We should build evals“ → Usually means “we should write LLM judges“ (useless if not calibrated and not part of the flywheel).

- “Evals are dead; A/B testing is key“ → This is part of the flywheel. Some
companies overindex on online signals and fix issues without many
offline metrics. Might or might not make sense based on product.

- “How are GPT-5.2 evals looking?“ → These are model benchmarks, often not useful for product builders.

- “How many evals do you have?“ → Might refer to data samples, metrics… We don’t know what.