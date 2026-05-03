---
complexity: Intermediate
date: 2025-11-18 17:20:00-05:00
id: 2af9fa3b-8750-80b5-a10a-d52d2ac7737b
processed_by_ai: true
summary: The document discusses customizing VS Code for Java development, the features
  of the Gemini 3.0 release including its agent-driven IDE, and a comparison between
  Spec Kit and OpenSpec for managing documentation in brownfield projects, highlighting
  challenges with agent context and merging.
title: Training today
tools_mentioned:
- VS Code
- IntelliJ
- Gemini 3.0
- Spec Kit
- OpenSpec
topics:
- VS Code customization
- Java development
- AI models
- Agent-driven development
- Software documentation
- Software architecture
- Context management
url: https://www.notion.so/Training-today-2af9fa3b875080b5a10ad52d2ac7737b
---

Learning to customize and use VS Code for java projects. It is taking some use to but getting close to how I use intellij.

<br/>

Read about the gemini 3.0 release. Better in a lot of ways but maybe not for coding.
Though it seems google is working on having an infrastructure for running agents and still giving access to all kinds of models, not just the google one. Overall there is a better integration with tools, Gemini 3.0 can create code to solve problems or present results (in whatever format is the best for the results you are looking at).

They also released their own agent driven IDE (based on VS Code) which promises to easily allow for running multiple agents in the background.



<br/>

Investigating the difference between spec kit and OpenSpec and why spec kit may not be the best approach for brown field projects. Has to do with creating a lot of documentation over time and maybe needing to read more than one for implementing a new feature. This leads to Graveyard of Intent (context is getting too big and agents are getting confused).

Open Spec has a unique specs document which gets updated once you have finished an implementation. All other documents are archived in an archive folder. But this approach probably works well with one developer but have some issues when multiple developers are working on the same project. Merging the overall spec document could be tricky. 

We could also ask the agent to update a general spec document from the new implemented spec kit feature and add the spec document to the scope when creating a new spec.

[It seems spec kit is currently working on a new feature](https://gemini.google.com/share/19dcd40ee707) probably called consolidate or merge which would allow updating a single spec document or at a module level the truth of the system. One document for the whole system is probably a little big. But this also bring the issue on how to merge this when we have conflicts.

They are also considering what happens with multiple background agents and the idea that they would need shared memory space for documents to be updated by all the agents. This would probably be quite tricky.

<br/>

<br/>