---
title: 9 Context Engineering Mistakes That Are Killing Your AI Agents  How to Fix Them at Scale
id: 2c49fa3b-8750-8042-a333-e920a3705bbb
url: https://www.notion.so/9-Context-Engineering-Mistakes-That-Are-Killing-Your-AI-Agents-How-to-Fix-Them-at-Scale-2c49fa3b87508042a333e920a3705bbb
---

### **Core Concept**

### **9 Principles to Fix Context Engineering**

1. **Context as a Compiled View:** Treat every LLM call as a freshly computed projection. Don't just append history; rebuild the minimal relevant slice for the current task to prevent signal dilution [03:49 Opens in a new window ](http://www.youtube.com/watch?v=Udc19q1o6Mg&t=229).

1. **Tiered Memory Model:** Separate storage from presentation. Use a hierarchy: *Working Context* (current call), *Sessions* (event logs), *Memory* (searchable insights), and *Artifacts* (large objects referenced by tag) [04:40 Opens in a new window ](http://www.youtube.com/watch?v=Udc19q1o6Mg&t=280).

1. **Scope by Default:** Default context should contain nearly nothing. Agents should actively choose when to pull in memories or artifacts to keep attention focused [05:36 Opens in a new window ](http://www.youtube.com/watch?v=Udc19q1o6Mg&t=336).

1. **Retrieval Beats Pinning:** Long-term memory must be searchable, not pinned in the prompt. The context window should be the result of a search query, not a passive accumulation of history [06:18 Opens in a new window ](http://www.youtube.com/watch?v=Udc19q1o6Mg&t=378).

1. **Schema-Driven Summarization:** Don't use blind summarization. Use structured schemas to preserve decision structures and essential semantics, making memory debuggable and reversible [07:12 Opens in a new window ](http://www.youtube.com/watch?v=Udc19q1o6Mg&t=432).

1. **Offload Heavy State:** Write large data to disk or files and pass pointers to the agent. Don't feed raw tool results (like massive logs) directly into the prompt [08:11 Opens in a new window ](http://www.youtube.com/watch?v=Udc19q1o6Mg&t=491).

1. **Isolate with Sub-Agents:** Use sub-agents (e.g., Planner, Executor) to isolate scope and state, not to mimic human org charts. They should communicate via structured artifacts [08:56 Opens in a new window ](http://www.youtube.com/watch?v=Udc19q1o6Mg&t=536).

1. **Optimize for Caching:** Design prompts with a stable prefix (instructions/identity) that rarely changes, so the cache can be reused. Only the suffix (user input) should change [09:44 Opens in a new window ](http://www.youtube.com/watch?v=Udc19q1o6Mg&t=584).

1. **Evolve Strategies:** Allow agents to update their instructions and strategies through execution feedback, enabling them to learn from doing rather than being frozen in a static prompt [10:37 Opens in a new window ](http://www.youtube.com/watch?v=Udc19q1o6Mg&t=637).

### **9 Common Mistakes to Avoid**

- **Dumping everything into the prompt:** Leads to rising costs and degraded reasoning [11:16 Opens in a new window ](http://www.youtube.com/watch?v=Udc19q1o6Mg&t=676).

- **Blind summarization:** Erases critical domain insights and constraints [11:30 Opens in a new window ](http://www.youtube.com/watch?v=Udc19q1o6Mg&t=690).

- **Treating context as unlimited RAM:** More tokens often mean more noise and distraction [11:47 Opens in a new window ](http://www.youtube.com/watch?v=Udc19q1o6Mg&t=707).

- **Polluting prompts with logs:** Don't put debug logs or error messages in the prompt; it drowns out the signal [12:14 Opens in a new window ](http://www.youtube.com/watch?v=Udc19q1o6Mg&t=734).

- **Tool Bloat:** Exposing too many overlapping tools increases error rates [12:41 Opens in a new window ](http://www.youtube.com/watch?v=Udc19q1o6Mg&t=761).

- **Anthropomorphizing Agents:** Giving agents human job titles (e.g., "You are the manager") leads to hallucinated teamwork [12:55 Opens in a new window ](http://www.youtube.com/watch?v=Udc19q1o6Mg&t=775).

- **Static Configurations:** Rebuilding the agent from scratch every run prevents it from learning or adjusting heuristics [13:31 Opens in a new window ](http://www.youtube.com/watch?v=Udc19q1o6Mg&t=811).

- **Over-structuring:** Rigid harnesses can box in capable models and kill emergent capabilities [14:07 Opens in a new window ](http://www.youtube.com/watch?v=Udc19q1o6Mg&t=847).

- **Ignoring Prefix Discipline:** Failing to stabilize the prompt prefix leads to unpredictable latency and high costs [14:48 Opens in a new window ](http://www.youtube.com/watch?v=Udc19q1o6Mg&t=888).

