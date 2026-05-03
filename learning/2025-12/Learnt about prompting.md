---
complexity: Intermediate
date: 2025-12-05 17:46:00-05:00
id: 2c09fa3b-8750-804e-aa0e-da7277bdabdf
processed_by_ai: true
summary: The document discusses a team's progress in transitioning to AI-driven software
  development, focusing on the importance of prompt engineering, strategies for storing
  and reusing prompts (e.g., in GitHub or prompt libraries), and tailoring instructions
  for specific projects. It also mentions leveraging existing prompt templates from
  tools or websites.
title: Learnt about prompting
tools_mentioned:
- GitHub Copilot
- Spec Kit
- Open Spec
- Claude
topics:
- AI-driven Software Development
- Prompt Engineering
- Prompt Management
- Software Development Practices
url: https://www.notion.so/Learnt-about-prompting-2c09fa3b8750804eaa0eda7277bdabdf
---

The team is currently trying to clear our level 4 in the [Transition to AI plan](https://wiki.clarivate.io/spaces/LSHT/pages/805798545/Proposal+for+transition+to+AI+Driven+Software+Development) and I have been learning from some of the[ examples people already provided](https://wiki.clarivate.io/spaces/LSHT/pages/833455606/Level+4+-+Requirement+analysis+results).

I was not really intending for the experiment to be that elaborated, so don't feel like you have to the perfect experiment before you get started.

This also brings the thought that for the prompts that work, we should be able to record them in some fashion.

For instance, most of the options of the impressive prompt would be the same for the project and potentially for other projects.

We can eventually have a library of prompts or we could also store the prompts within github as ./.gihub/prompts/*.prompt.md so they can be re-used in github copilot.

But if we keep re-using the same conditions always, we should probably add those conditions to the instructions-copilot.md file.

As much as we could automate the instructions file to match all java project, it would be better to make them unique and tailored to each project.

We don't necessarily know what to put in there yet, but as we keep learning it will become more obvious.

One advantage of something like Spec Kit or Open Spec is that those tools come with their own prompts, so we don't need to guess.

Not saying that is the solution for us yet.

There are also a few web sites hosting prompt templates (like Claude skills include also the prompts). So we don't need to create the prompts ourselves.

Though it is important for us to try as it deepends our understanding of the tools.