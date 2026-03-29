---
title: From IDEs to AI Agents with Steve Yegge
id: 3329fa3b-8750-80e0-9b63-f5b00be0e050
url: https://www.notion.so/From-IDEs-to-AI-Agents-with-Steve-Yegge-3329fa3b875080e09b63f5b00be0e050
---

### 🔑 Key Concepts

- **The 8 Levels of AI Adoption:** Yegge outlines a spectrum from **Level 1** (No AI) to **Level 6** (Bored because multiple agents are doing your work) and **Level 8** (Total orchestration). Most engineers are currently stuck at Levels 1–3 [22:52 Opens in a new window ](http://www.youtube.com/watch?v=aFsAOu2bgFk&t=1372).

- **The "Vampiric Effect":** A phenomenon where AI enables 100x productivity but causes extreme mental burnout. Yegge notes that "vibe coding" at high speeds drains "System 2" thinking so fast that developers may only have 3 truly productive hours a day [01:14 Opens in a new window ](http://www.youtube.com/watch?v=aFsAOu2bgFk&t=74), [42:10 Opens in a new window ](http://www.youtube.com/watch?v=aFsAOu2bgFk&t=2530).

- **Gas Town:** Yegge's open-source agent orchestrator. He describes it as a "factory" where a "Mayor" (agent) manages specialized workers like "Polecats" (for small tasks) and "Crews" (for large context tasks) [31:10 Opens in a new window ](http://www.youtube.com/watch?v=aFsAOu2bgFk&t=1870), [33:42 Opens in a new window ](http://www.youtube.com/watch?v=aFsAOu2bgFk&t=2022).

- **The "Bitter Lesson":** Referencing Richard Sutton, Yegge emphasizes that human cleverness (specialized domain knowledge) is consistently outperformed by raw scale (more data/compute). He advises not to fight the AI but to provide it with more context and scale [01:04:54 Opens in a new window ](http://www.youtube.com/watch?v=aFsAOu2bgFk&t=3894).

---

### 🚀 Predictions for the Industry

- **Death of the Big Tech Monolith:** Yegge predicts that large companies are "quietly dying" because they cannot absorb innovation as fast as small, AI-empowered teams of 2–20 people [01:19 Opens in a new window ](http://www.youtube.com/watch?v=aFsAOu2bgFk&t=79), [56:56 Opens in a new window ](http://www.youtube.com/watch?v=aFsAOu2bgFk&t=3416).

- **End of "Coding by Hand":** He asserts that "the days of coding by hand are over" [13:33 Opens in a new window ](http://www.youtube.com/watch?v=aFsAOu2bgFk&t=813). Instead, software will be built through recursive summarization and high-level "vibe" conversations [30:11 Opens in a new window ](http://www.youtube.com/watch?v=aFsAOu2bgFk&t=1811).

- **Democratization of Programming:** By 2027, Yegge predicts non-developers (like his wife) will be top contributors to complex projects like video games because the barrier to entry is shifting from syntax to ideas [01:27:38 Opens in a new window ](http://www.youtube.com/watch?v=aFsAOu2bgFk&t=5258).

- **Token Burn as a Metric:** The best proxy for organizational learning today is "token burn"—how much a team is experimenting and failing with AI [26:33 Opens in a new window ](http://www.youtube.com/watch?v=aFsAOu2bgFk&t=1593).

---

### 💡 Career Advice for Engineers

- **Grieve and Move On:** Yegge describes a "monochrome" week of grief where he realized his 40 years of specialized skills (compilers, debuggers) no longer made him special—but then realized he was having more fun writing 10x more code [01:26:14 Opens in a new window ](http://www.youtube.com/watch?v=aFsAOu2bgFk&t=5174).

- **Avoid "Copilot" Stagnation:** He warns that using basic autocomplete (like standard Copilot) is like "working with a barbarian horde" compared to modern agentic tools like **Claude Code** [01:17:23 Opens in a new window ](http://www.youtube.com/watch?v=aFsAOu2bgFk&t=4643), [01:18:50 Opens in a new window ](http://www.youtube.com/watch?v=aFsAOu2bgFk&t=4730).

- **Capture Your Value:** If you are 100x more productive, Yegge suggests you must learn to "say no" and negotiate a new work-life balance, as traditional companies will simply extract that extra value until you break [01:31:26 Opens in a new window ](http://www.youtube.com/watch?v=aFsAOu2bgFk&t=5486).

<br/>

### 🤖 Why Copilot is Moving Beyond Level 1

- **Background Agents:** You can now delegate complex tasks (e.g., "write comprehensive integration tests for this module") to a [cloud-based coding agent](https://github.blog/changelog/2026-03-11-major-agentic-capabilities-improvements-in-github-copilot-for-jetbrains-ides/) that works independently while you continue coding in the foreground [02:00:00 Opens in a new window ](https://www.youtube.com/watch?v=S1ch_6fjp5M&vl=en&t=7200).

- **Copilot "Squads" (Sub-Agents):** Visual Studio 2026 includes specialized participants like `@workspace`, `@debugger`, and `@profiler`. These act as a team of experts that can independently research, profile, and propose fixes within their specific domains [01:12:01 Opens in a new window ](https://www.youtube.com/watch?v=S1ch_6fjp5M&vl=en&t=4321).

- **Agentic Memory:** Copilot now has [persistent repository-level memory](https://github.com/orgs/community/discussions/186497) that allows agents to learn from past sessions, which is a key requirement for moving from "reactive" to "proactive" assistance [02:02:03 Opens in a new window ](https://www.youtube.com/watch?v=S1ch_6fjp5M&vl=en&t=7323).

- **Autopilot Mode:** In certain environments, Copilot can now run in an [autonomous loop](https://morphllm.com/comparisons/claude-code-vs-copilot)—executing terminal commands, fixing lint errors, and running tests without stopping for human approval at every step [04:05:00 Opens in a new window ](https://www.youtube.com/watch?v=S1ch_6fjp5M&vl=en&t=14700).

---

### ⚖️ The Remaining "Level 1" Arguments

 | **Feature** | **Copilot 2026 Philosophy** | **High-Level Agent Philosophy (e.g., Claude Code)** | 
 | ---- | ---- | ---- | 
 | **Primary UI** | **IDE-First:** Optimized for the "flow state" and reducing keystrokes [04:03:00 Opens in a new window ](https://www.youtube.com/watch?v=S1ch_6fjp5M&vl=en&t=14580). | **Terminal/Task-First:** Optimized for hours eliminated from a migration [04:03:00 Opens in a new window ](https://www.youtube.com/watch?v=S1ch_6fjp5M&vl=en&t=14580). | 
 | **Orchestration** | **Developer-Directed:** You usually trigger specific "skills" or agents manually [04:03:00 Opens in a new window ](https://www.youtube.com/watch?v=S1ch_6fjp5M&vl=en&t=14580). | **Autonomous Planning:** You give one high-level intent; the agent plans and spawns its own sub-tasks [04:05:00 Opens in a new window ](https://www.youtube.com/watch?v=S1ch_6fjp5M&vl=en&t=14700). | 
 | **Context** | **Managed Snippets:** Efficiently fits code into 32k–128k windows [04:03:00 Opens in a new window ](https://www.youtube.com/watch?v=S1ch_6fjp5M&vl=en&t=14580). | **Massive Reasoning:** Often utilizes 1M+ token context for deep architectural changes [04:03:00 Opens in a new window ](https://www.youtube.com/watch?v=S1ch_6fjp5M&vl=en&t=14580), [04:05:00 Opens in a new window ](https://www.youtube.com/watch?v=S1ch_6fjp5M&vl=en&t=14700). | 
 | **Verification** | **Inline Review:** You "Tab" to accept or reject changes in real-time [04:01:00 Opens in a new window ](https://www.youtube.com/watch?v=S1ch_6fjp5M&vl=en&t=14460). | **PR-Ready Diffs:** You review a finished body of work after the agent is done [04:03:00 Opens in a new window ](https://www.youtube.com/watch?v=S1ch_6fjp5M&vl=en&t=14580). | 

### 🏁 Summary: Is it Level 1?

