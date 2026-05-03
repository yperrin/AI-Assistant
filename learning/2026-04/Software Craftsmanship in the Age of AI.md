---
complexity: Advanced
date: 2026-04-12 22:17:00-04:00
id: 3419fa3b-8750-80b2-aff1-ff0ec5f9a2c5
processed_by_ai: true
summary: This document discusses the O'Reilly AI Codecon, focusing on how software
  craftsmanship is evolving as AI agents increasingly write code. It explores different
  perspectives on human-AI collaboration in software development, from fully automated
  "dark factories" to human oversight and new architectural paradigms.
title: Software Craftsmanship in the Age of AI
tools_mentioned:
- Claude
- Codex
- Gemini
- Go
- pandas
- Treehouse
- Antfarm
- OpenClaw
- Box
topics:
- AI Agents
- Software Craftsmanship
- AI in Software Development
- Automation
- Augmentation
- Agentic Failure
- Software Architecture
- Context Engineering
- Multi-Agent Systems
url: https://www.notion.so/Software-Craftsmanship-in-the-Age-of-AI-3419fa3b875080b2aff1ff0ec5f9a2c5
---

On March 26, Addy Osmani and I are hosting the third [O’Reilly AI Codecon](https://www.oreilly.com/AI-Codecon/),
 and this time we’re taking on the question of what software 
craftsmanship looks like when AI agents are writing much of the code.

The subtitle of this event, “Software Craftsmanship in the Age of 
AI,” was meant to be provocative. Craftsmanship implies care, intention,
 and deep skill. It implies a maker who touches the material. But we’re 
entering a world where some people with quite impressive output *don’t* touch the code. Steve Yegge, in [our conversation earlier this week](https://www.oreilly.com/radar/steve-yegge-wants-you-to-stop-looking-at-your-code/),
 put it bluntly: “Code is a liquid. You spray it through hoses. You 
don’t freaking look at it.” Wes McKinney, the creator of pandas and one 
of our speakers at this event, [doesn’t write code by hand any more either](https://wesmckinney.com/blog/mythical-agent-month/).
 He’s burning north of 10 billion tokens a month across Claude, Codex, 
and Gemini, writing vast amounts of Go, a language he’s never coded in 
manually.

If that’s where this is headed, then what exactly are we crafting? 
That’s the question this lineup is built to answer, and the speakers 
come at it from very different angles.

## **The “dark factory” position**

One end of the spectrum is occupied by people who are already operating what are increasingly being called [dark factories](https://www.cow-shed.com/blog/dark-factories-five-levels-ai-automation-transform-audit-banking-legal),
 after the robot factories where there are no lights because the robots 
that do all of the work don’t need them. These are software production 
environments where humans set direction but agents do nearly all the 
implementation.

**Ryan Carson** is the clearest example on our stage. 
Ryan built and sold Treehouse, where he helped over a million people 
learn to code. Now he’s building [Antfarm](https://x.com/ryancarson/status/2020931274219594107), an open source tool that lets you install an entire team of agents into [OpenClaw](https://openclaw.ai/)
 with a single command. His talk, “How to Create a Team of Agents in 
OpenClaw and Ship Code with One Command,” is essentially a tutorial on 
running a software factory where a planning agent decomposes your 
feature request into user stories, each story gets implemented and 
tested in isolation by a separate agent, failures retry automatically, 
and you get back tested pull requests. This isn’t quite a dark factory, 
though. Ryan has built a CI pipeline where the agent records itself 
using a feature and attaches the video to the PR for human review. It’s 
an assembly line, and the human’s job is to inspect the output, not 
produce it.

This is [Steve Yegge’s Level 7 or 8](https://www.oreilly.com/radar/steve-yegge-wants-you-to-stop-looking-at-your-code/),
 and it’s no longer theoretical. But Ryan’s talk will also reveal what 
happens at the edges, when agents break, when the feedback loop fails, 
when automated retries aren’t enough.

## **The craftsmanship-means-oversight position**

At the other end you have people who are deeply enthusiastic about AI
 coding but insist that the human role isn’t just “set direction and 
walk away.” It’s active, continuous, and skilled.

**Addy Osmani** anchors this position. His talk, 
“Orchestrating Coding Agents: Patterns for Coordinating Agents in 
Real-World Software Workflows,” is about the coordination problem. As he
 and I discussed in [our recent conversation](https://www.oreilly.com/radar/what-developers-actually-need-to-know-right-now/),
 there’s a spectrum from solo founders running hundreds of agents 
without reviewing the code to enterprise teams with quality gates and 
long-term maintenance to think about. Most real teams are somewhere in 
the middle, and they need patterns, not just tools. Addy has been 
thinking hard about what Andrej Karpathy called “context engineering,” 
the discipline of structuring all the information an LLM needs to 
perform reliably. His new book *[Beyond Vibe Coding](https://learning.oreilly.com/library/view/beyond-vibe-coding/9798341634749/)* is essentially a manual for this new discipline.

**Cat Wu** from Anthropic brings the platform maker’s 
perspective. She leads product for Claude Code and Cowork, and her focus
 on building AI systems that are “reliable, interpretable, and 
steerable” represents a design philosophy that the tool should make 
human oversight natural and easy. Where Ryan Carson’s approach pushes 
toward maximum agent autonomy, Cat’s work at Anthropic is about giving 
humans the right levers to stay meaningfully in the loop. I’m really 
looking forward to the conversation between Cat and Addy.

## **The costs of getting it wrong**

Several speakers are focused squarely on what happens when the dark factory breaks down.

**Nicole Koenigstein’s** talk, “The Hidden Cost of 
Agentic Failure and the Next Phase of Agentic AI,” is about the failure 
modes that don’t show up in demos. Nicole is writing the O’Reilly book *[AI Agents: The Definitive Guide](https://learning.oreilly.com/library/view/ai-agents-the/0642572247775/)*, and she’s been consulting with companies on the gap between what agents can do in a sandbox and what they do in production. **Hila Fox**
 from Qodo brings a complementary perspective with “From Prompt to 
Multi-Agent System: The Evolution of Our AI Product,” which traces the 
real path from a simple prompt-based tool to a production multi-agent 
system, including all the things that go wrong along the way.

The lightning talks share more results of real-world experience. **Advait Patel**,
 a site reliability engineer at Broadcom, will talk about what happens 
when AI agents break production systems, and how his team responded. **Abhimanyu Anand**
 from Elastic asks a question that should keep every AI builder up at 
night: “Is your eval lying to you?” If your evaluation framework is 
giving you false confidence, you’re building on sand.

## **The bottleneck was never hands on keyboards**

**Wes McKinney’s** talk, “The Mythical Agent-Month,” 
revisits Fred Brooks’s famous argument that adding more people to a late
 software project makes it later, and asks whether the same dynamics 
apply to adding more agents. Wes’s answer, as he’s laid it out in [his blog post](https://wesmckinney.com/blog/mythical-agent-month/),
 is so compelling that we immediately invited him to give it as a talk, 
even though that meant rearranging the existing program. Agents leave 
the essential complexity, the hard design decisions, the conceptual 
integrity of the system, completely untouched. Worse, agents introduce 
new accidental complexity at machine speed. Wes describes hitting a 
“brownfield barrier” around 100,000 lines of code where agents begin 
choking on the bloated codebases they themselves have generated.

This connects directly to something that Steve Yegge and Wes (and 
many others, including me) have converged on: Taste is the scarce 
resource. Brooks argued 50 years ago that design talent was the real 
bottleneck. Now that agents have removed the labor constraint, that 
argument is stronger than ever. The developers who thrive won’t be the 
ones who run the most parallel sessions. They’ll be the ones who can 
hold their project’s conceptual model in their head, who know what to 
build and what to leave out.

## **New architectures for the new reality**

A cluster of talks addresses the structural question: If agents are 
doing most of the coding, what does the engineering organization, the 
platform, and the architecture need to look like?

**Juliette van der Laarse**’s talk, “The AI Flower: A 
Public Capability Architecture for AI-Native Engineering,” lays out a 
framework for how engineering teams should organize their capabilities 
in a world of AI-native workflows. Juliette’s work is a start on 
thinking through the second-order effects of the new technology. How 
does the organization itself need to change? We came across Juliette’s 
work recently and think it may be especially compelling for many of our 
enterprise customers.

**Mike Amundsen **has spent years thinking about API 
ecosystems and sustainable architecture, and he’s applying that lens to 
the question of how AI should relate to human expertise. His talk, “From
 Automation to Augmentation: Designing AI Coaches That Amplify 
Expertise,” makes a distinction that will determine the shape of the 
future human/AI economy. Automation replaces human work. Augmentation 
amplifies it.

Several other lightning talks fill in important pieces. **Tatiana Botskina**,
 a PhD candidate at Oxford and founder of an AI agent registry, talks 
about agent-to-agent collaboration and provenance, the question of how 
you know where an agent’s outputs came from. **Neethu Elizabeth Simon**
 from Arm addresses MCP server testing, a nuts-and-bolts reliability 
question that will matter more as MCP becomes the standard connective 
tissue for agent systems. And **Arushee Garg** from 
LinkedIn describes a production multi-agent system for generating 
outreach messages. These are all exploring issues that matter during 
real-world deployment.

## **The enterprise view**

The event closes with my fireside chat with **Aaron Levie**,
 cofounder and CEO of Box. Aaron has been one of the most thoughtful 
enterprise CEOs on the question of what agents mean for SaaS and for 
knowledge work more broadly. His argument is that agents don’t replace 
enterprise software; they ride on top of it, and they need content, 
context, and governance to do anything useful. He’s also made the point 
that most companies have vast amounts of work they’ve never been able to
 afford to do, contracts they’ve never analyzed, processes they’ve never
 optimized. AI doesn’t just automate existing work. It unlocks work that
 was previously too expensive to attempt.

That connects to a theme I’ve been developing in my own work: the 
danger that AI creates enormous value but hollows out the economic 
circulatory system that supports the human expertise it depends on. 
Aaron is running a public company that has to navigate this in real 
time, making AI central to Box’s product while making the case that 
human judgment, context, and governance are more valuable, not less, in 
an agentic world.

## **What I’ll be watching for**

There will be not only real excitement but hopefully deeper insight 
emerging from the tensions between these speakers and the positions they
 take. Ryan Carson and Cat Wu represent genuinely different philosophies
 of the human-agent relationship, and both are shipping real products. 
Wes McKinney and Addy Osmani agree that taste and design judgment matter
 more than ever, but they’re coming at it from very different vantage 
points: Wes as an individual developer pushing the limits of parallel 
agent sessions, Addy as someone thinking about patterns that work for 
teams of hundreds. Nicole Koenigstein and Hila Fox are asking the 
question that the enthusiasm sometimes papers over: What happens when it
 goes wrong?

And underneath all of it is the question that Steve Yegge, who isn’t 
on this program but whose ideas have certainly shaped my design of the 
program, would frame as a matter of grief and acceptance. Are we at the 
end of programming as a craft practice, or at the beginning of a new and
 different craft? I think the lineup proves that the craft isn’t dying. 
It’s migrating, from writing code to designing systems, from typing to 
taste, from individual heroics to orchestration. The people who 
understand that transition earliest will have an enormous advantage.