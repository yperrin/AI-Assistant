---
complexity: Advanced
date: 2026-02-18 19:53:00-05:00
id: 30c9fa3b-8750-80f3-a51c-e4c2906020c3
processed_by_ai: true
summary: This document analyzes Nate B. Jones' "5 Levels of AI Coding" framework,
  explaining how AI integration impacts developer productivity, organizational structure,
  and the future of various job roles. It highlights a "J-Curve" productivity dip,
  the "Dark Factory" model, and a shift in value from implementation speed to specification
  quality, leading to a flattening of organizational charts and the potential obsolescence
  of coordination and junior developer roles.
title: The 5 Levels of AI Coding Why Most of You Wont Make It Past Level 2
tools_mentioned:
- GitHub Copilot
- StrongDM
- Cursor
- Midjourney
- Kubernetes
topics:
- AI Coding
- Developer Productivity
- Organizational Structure
- AI Impact on Jobs
- Software Development Workflow
- Specification Quality
- Management Roles
- Future of Work
url: https://www.notion.so/The-5-Levels-of-AI-Coding-Why-Most-of-You-Won-t-Make-It-Past-Level-2-30c9fa3b875080f3a51ce4c2906020c3
---

This video by **Nate B. Jones** explores the "5 Levels of AI Coding," a framework originally proposed by Dan Shapiro (CEO of Glowforge), and analyzes why most developers are currently getting *slower* despite using AI tools.

### **The 5 Levels of Vibe Coding**

The video categorizes AI integration into five distinct stages [02:37 Opens in a new window ](http://www.youtube.com/watch?v=bDcgHzCBgmQ&t=157):

1. **Level 0: Spicy Autocomplete** – Basic suggestions (e.g., original GitHub Copilot) [02:44 Opens in a new window ](http://www.youtube.com/watch?v=bDcgHzCBgmQ&t=164).

1. **Level 1: Coding Intern** – AI handles discrete, well-scoped functions; humans review everything [03:02 Opens in a new window ](http://www.youtube.com/watch?v=bDcgHzCBgmQ&t=182).

1. **Level 2: Junior Developer** – AI navigates codebases and multifile changes; humans still read every line. **90% of "AI native" devs stop here** [03:30 Opens in a new window ](http://www.youtube.com/watch?v=bDcgHzCBgmQ&t=210).

1. **Level 3: Developer as Manager** – The AI implements features and submits PRs; the human directs and approves at the PR level [03:56 Opens in a new window ](http://www.youtube.com/watch?v=bDcgHzCBgmQ&t=236).

1. **Level 4: Developer as Product Manager** – You write a spec, leave, and return to check if tests passed. You no longer read the code [04:41 Opens in a new window ](http://www.youtube.com/watch?v=bDcgHzCBgmQ&t=281).

1. **Level 5: The Dark Factory** – An autonomous black box where specs go in and working software comes out with zero human code review [05:14 Opens in a new window ](http://www.youtube.com/watch?v=bDcgHzCBgmQ&t=314).

### **Key Takeaways for Senior Leaders**

As a Senior Director, several points from the video align with your interests in **Medallion architecture**, **event-driven systems**, and **AI-assisted systems**:

- **The "J-Curve" Productivity Dip:** Randomized trials show experienced devs can take **19% longer** on tasks with AI because they are running "new engines on old transmissions" [15:25 Opens in a new window ](http://www.youtube.com/watch?v=bDcgHzCBgmQ&t=925). True gains (25%+) require a total workflow redesign, not just installing a tool [17:00 Opens in a new window ](http://www.youtube.com/watch?v=bDcgHzCBgmQ&t=1020).

- **The "Dark Factory" Model:** A team called **StrongDM** is cited as a Level 5 example. They use **Markdown specifications** and "Scenarios" (behavioral tests kept external to the codebase) to prevent AI from "teaching to the test" [08:27 Opens in a new window ](http://www.youtube.com/watch?v=bDcgHzCBgmQ&t=507).

- **Structural Friction:** Traditional ceremonies like stand-ups and sprint planning become "friction" when implementation happens in hours, not weeks [19:21 Opens in a new window ](http://www.youtube.com/watch?v=bDcgHzCBgmQ&t=1161).

- **The Shift in Value:** The bottleneck has moved from **implementation speed** to **specification quality** [22:02 Opens in a new window ](http://www.youtube.com/watch?v=bDcgHzCBgmQ&t=1322). This requires deep systems thinking—exactly the "long-term architectural health" you prioritize.

- **Legacy Systems (Brownfield):** The video warns that you cannot "Dark Factory" your way through legacy systems without first reverse-engineering them into explicit specifications [23:15 Opens in a new window ](http://www.youtube.com/watch?v=bDcgHzCBgmQ&t=1395).

### **Resources**

- **Full Video:** [The 5 Levels of AI Coding](https://www.youtube.com/watch?v=bDcgHzCBgmQ)

- **Nate's Substack:** [Full Story w/ Prompts](https://natesnewsletter.substack.com/p/the-5-level-framework-that-explains)

<br/>

Based on the video, the "Dark Factory" era leads to a radical flattening of the organizational chart. Because machines handle the implementation, the entire coordination layer of a modern software company—which Nate B. Jones notes currently occupies about 60% of a manager's time—is essentially deleted.

### **Key Shifts in Company Structure**

- **Flattening of the Org Chart:** AI-native startups like [Cursor](https://www.youtube.com/watch?v=bDcgHzCBgmQ) and [Midjourney](https://www.youtube.com/watch?v=bDcgHzCBgmQ) are generating hundreds of millions in revenue with only a few dozen employees. This results in a revenue-per-employee ratio roughly 5-6 times higher than the average SaaS company.

- **Deletion of Coordination Roles:** Traditional roles created to manage human limitations—such as Scrum Masters, Release Managers, and Technical Program Managers—are at risk of disappearing because the "friction" they manage (like synchronization and sprint planning) no longer serves a purpose when agents build features in hours.

- **The "Middle" Hollows Out:** The career ladder is being "hollowed out from underneath." Junior roles are declining (down 67% in US job postings) because AI handles the "simple" bugs and features that juniors traditionally used for learning.

- **Shift from Specialists to Generalists:** Value is shifting away from deep specialists (e.g., someone who only knows Kubernetes) toward generalists who understand the business, the customer, and the entire system architecture.

### **The Evolving Role of Management**

Management moves from **coordination** to **articulation**:

- **Engineering Managers:** Their value shifts from "coordinating the team" to "defining the specification" clearly enough for agents to build it.

- **Program Managers:** They move from tracking dependencies between human teams to architecting the "pipeline of specs" flowing through the factory.

Ultimately, the bottleneck of the organization moves from **how fast can we build it** to **what should we build and for whom**.

<br/>

Based on the video's analysis of the transition toward "Dark Factories" and autonomous AI agents, the jobs most likely to disappear are those centered around **coordination**, **implementation of simple tasks**, and **manual verification**.

Nate B. Jones highlights that as AI moves toward Level 5 (The Dark Factory), roles designed to manage human limitations become redundant.

### **Roles Most at Risk**

- **Junior Developers:** Entry-level postings have already declined significantly (67% in the US). AI now handles the "simple" features and bug fixes that juniors traditionally used to learn the craft, hollowing out the bottom of the career ladder.

- **Middle Management & Coordination Roles:** Approximately 60% of a manager's time is currently spent on "coordination layers" that may be deleted. Specific roles mentioned include:

	- **Scrum Masters:** Redundant when implementation happens in hours rather than weeks.

	- **Release Managers:** Their value in coordinating complex human shipping schedules is minimized by automated pipelines.

	- **Technical Program Managers:** Roles focused purely on tracking dependencies between human teams.

- **Manual QA Engineers:** Traditional QA teams exist because humans can't evaluate their own work objectively. In a Dark Factory, AI tests against "Scenarios" (behavioral specs) it was never shown, making manual test passes obsolete.

- **Specialized "Implementation" Roles:** Developers who function as "adequate" implementers—those who can write a CRUD endpoint but lack broader system or business intuition—are being replaced by models that can do the same work for the cost of tokens.

### **The Structural Change**

The video notes that these roles aren't necessarily eliminated as a "cost-saving measure" but because they **no longer serve a purpose** in an AI-native workflow. The center of gravity is shifting from **coordination** to **articulation**—the ability to describe a problem precisely enough for a machine to solve it.

For more details, you can view the [full video](https://www.youtube.com/watch?v=bDcgHzCBgmQ) or read the [full story with prompts](https://natesnewsletter.substack.com/p/the-5-level-framework-that-explains?r=1z4sm5&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true).