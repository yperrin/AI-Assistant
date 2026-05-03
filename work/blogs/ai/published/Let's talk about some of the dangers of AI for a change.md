# Let's talk about some of the dangers of AI for a change

**By:** [Yann Perrin](https://clarivate.atlassian.net/wiki/spaces/LSHT/blog/2026/04/20/395051725/Let+s+talk+about+some+of+the+dangers+of+AI+for+a+change)  
**Date:** April 20, 2026  
**Read Time:** 4 min

You all know I am pretty enthusiastic about using AI and I believe that is definitely something we should be doing and to be honest something I really enjoy doing. I can't get to do enough with it. 

I want to share 3 warnings though because we should not ignore the challenges that come with using it. Most of the issues can be addressed with intentional and intelligent human in the loop approach.

* Over reliance on AI
* Comprehension Debt
* Why humans are needed in an automated system

---

## Over Reliance on AI

I have had 2 experiences recently where I had to review AI generated code. In both cases when I asked what problem are we trying to solve I was given the original stated issue but not the actual source of the problem. AI generated code which in both cases solved the problem but also removed the reason the code was there for.

You can use AI to identify the root cause, once you found it, understand it, then you can ask the AI to solve the issue. But if you let the AI do both then you cannot do a code review. **If you don't understand the code changed or why the code change is fixing your specific issue, you should not commit the code. Period. No exceptions.**

This creates something coined as **Dark code**. Unlike technical debt or "spaghetti code," Dark Code isn't necessarily buggy. It is code where the *comprehension step* was skipped because AI generated it, automated checks passed it, and it was shipped immediately to maintain velocity. To combat Dark Code while maintaining AI-driven speed, here are some suggestions:

* **Layer 1: Spec-Driven Development:** Force understanding *before* code exists. Use a clear written specification as the "primary artifact." This spec then becomes the "eval" (evaluation) that the AI must pass.
* **Layer 2: Self-Describing Systems:** Use *Context Engineering* to embed comprehension into the codebase via structural context (module manifests) and semantic context (rules of engagement/failure modes).
* **Layer 3: The Comprehension Gate:** Instead of manual PR reviews, use AI to surface "principal engineer" level questions (e.g., "Why is this caching here?"). This acts as a filter to make massive volumes of code legible to senior leadership.

---

## Comprehension Debt

* **The Invisible Cost:** Unlike technical debt, which creates friction (slow builds, messy code), *comprehension debt breeds false confidence*. The code looks clean and tests pass, but the human understanding of *why* decisions were made evaporates.
* **The Theory of the System:** When teams rely on passive delegation ("just make it work"), they lose the mental model of the system. This leads to a "wall" where simple changes eventually cause unexpected breaks because no one understands the underlying design.

### Key Insights:
* **Skill Decline:** A study by Anthropic showed that developers using AI completed tasks at the same speed as a control group but scored **17% lower on follow-up comprehension quizzes**, specifically in debugging and conceptual understanding.
* **Usage Matters:** Developers who use AI for *conceptual inquiry* (asking "why") score significantly higher (65%+) than those who use it for *delegation* (under 40%).

---

## Why Human in the Loop is a necessity

Unlike previous management experiments (like Zappos' holacracy) which failed loudly, **World Model failures are invisible**. The information continues to flow, but the *judgment* disappears. Systems may flag data correlations without understanding external context, leading to poor decisions that feel like "bad luck" rather than systemic errors.

To avoid those silent issues, the following is recommended:
1.  **Explicitly label outputs** as "Act on this" (factual/low-risk) vs. "Interpret this first" (requires human judgment).
2.  **Record the results** of actions taken to create a feedback loop.

The danger lies in systems that work "well enough" that no one questions their degrading decision quality until it's too late.

> **Note on Zappos' Holacracy:** A radical transition initiated by CEO Tony Hsieh to eliminate traditional hierarchy. While meant to combat bureaucracy, it serves as a reminder that radical structural changes require clear judgment and human oversight to succeed.