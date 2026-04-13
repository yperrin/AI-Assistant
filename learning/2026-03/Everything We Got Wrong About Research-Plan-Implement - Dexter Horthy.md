---
title: Everything We Got Wrong About Research-Plan-Implement - Dexter Horthy
id: 3329fa3b-8750-8012-9164-d0487e16bc69
url: https://www.notion.so/Everything-We-Got-Wrong-About-Research-Plan-Implement-Dexter-Horthy-3329fa3b875080129164d0487e16bc69
---

---

## The Core Issues with Early Agentic Workflows

- **The "Dumb Zone" & Instruction Budgets:** Frontier LLMs have an "instruction budget" of roughly **150-200 instructions** before consistency degrades. Early RPI prompts often hit 85+ instructions, causing the model to "half-attend" to tasks and skip critical steps [07:36 Opens in a new window ](http://www.youtube.com/watch?v=YwZR6tc7qYg&t=456).

- **Outsourcing the Thinking:** Users often provided too much intent during the research phase. If you tell an agent *what* you are building during research, it returns **opinions** rather than **objective facts** about the codebase [05:06 Opens in a new window ](http://www.youtube.com/watch?v=YwZR6tc7qYg&t=306).

- **The "Slop" Factor:** Attempting 10x speed via full automation leads to "slop"—code that is 50% rework to fix mistakes from the previous week. Horthy argues that 2026 must be the year of "no more slop," moving from blind speed back to **craft** [02:45 Opens in a new window ](http://www.youtube.com/watch?v=YwZR6tc7qYg&t=165).

---

## Lessons Learnt: What They Got Wrong

- **"Don't Read the Code" was a mistake:** Previously, the advice was to just trust the agent and read the plan. Horthy now insists that **engineers must read the code** [09:22 Opens in a new window ](http://www.youtube.com/watch?v=YwZR6tc7qYg&t=562). Plans and implementations often diverge, and "leverage" isn't found by avoiding the code, but by making the alignment phase more efficient.

- **Magic Words:** Tools that require users to say specific "magic words" (e.g., *"work back and forth with me"*) are fundamentally broken. If the workflow requires hours of training to get right, the tool—not the user—is the problem [07:17 Opens in a new window ](http://www.youtube.com/watch?v=YwZR6tc7qYg&t=437).

- **Horizontal Planning:** Models naturally gravitate toward "horizontal" plans (doing all DB work, then all API work, etc.). This makes testing impossible until the very end, leading to massive debugging sessions [18:04 Opens in a new window ](http://www.youtube.com/watch?v=YwZR6tc7qYg&t=1084).

---

## The Solution: The "CRISPY" Framework

 | **Stage** | **Purpose** | **Key Strategy** | 
 | ---- | ---- | ---- | 
 | **Questions** | Alignment | Identify open questions and unknowns before searching the code. | 
 | **Research** | Fact-Finding | **Hide the ticket** from the research agent to ensure it only reports objective facts [11:29 Opens in a new window ](http://www.youtube.com/watch?v=YwZR6tc7qYg&t=689). | 
 | **Design** | Shared Intent | A ~200-line markdown doc to "perform brain surgery" on the agent's intent before coding starts [16:20 Opens in a new window ](http://www.youtube.com/watch?v=YwZR6tc7qYg&t=980). | 
 | **Structure** | Sprint Planning | Create a **Vertical Plan**—breaking the feature into testable, end-to-end slices (e.g., Mock API → UI → DB) [18:31 Opens in a new window ](http://www.youtube.com/watch?v=YwZR6tc7qYg&t=1111). | 
 | **Plan** | Tactical | A detailed doc for the agent to follow during the implementation phase. | 
 | **Work/Implement** | Execution | Small, iterative coding sessions based on the vertical slices. | 
 | **PR** | Review | Human review of the actual code to uphold professional standards [10:20 Opens in a new window ](http://www.youtube.com/watch?v=YwZR6tc7qYg&t=620). | 

---

### Final Takeaway

<br/>

