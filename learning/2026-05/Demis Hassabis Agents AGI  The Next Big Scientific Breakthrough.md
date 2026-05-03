---
complexity: Advanced
date: 2026-05-03 14:30:00-04:00
id: 3559fa3b-8750-8040-a3b3-f5ce9a51758b
processed_by_ai: true
summary: Demis Hassabis, co-founder of Google DeepMind, discusses the trajectory of
  AGI, predicting its emergence by 2030, and emphasizes the need for agentic systems
  that can actively solve problems and plan. He highlights challenges like reasoning
  gaps, memory management, and the potential of AI to revolutionize science by solving
  "root node" problems.
title: Demis Hassabis Agents AGI  The Next Big Scientific Breakthrough
tools_mentioned:
- Google DeepMind
- AlphaFold
- AlphaGo
- Gemini
- DQN
- Gemma
- Isomorphic Labs
- Waymo
- Co-scientist
- AlphaEvolve
- Theme Park
topics:
- Artificial General Intelligence (AGI)
- Agentic Systems
- Continual Learning
- Memory Management in AI
- Reinforcement Learning
- Multimodal AI
- Scientific Discovery with AI
- Drug Discovery
- Cellular Modeling
- Edge Computing
- Open Source AI
- AI Ethics and Impact
url: https://www.notion.so/Demis-Hassabis-Agents-AGI-The-Next-Big-Scientific-Breakthrough-3559fa3b87508040a3b3f5ce9a51758b
---

## Executive Summary

In this interview with Y Combinator, [Demis Hassabis](https://www.google.com/search?q=Demis%20Hassabis), co-founder of Google DeepMind and 2024 Nobel Prize winner in Chemistry, discusses the trajectory of Artificial General Intelligence (AGI) and its potential to revolutionize science. Hassabis predicts that **AGI could emerge by 2030** and emphasizes that the path forward lies in creating **agentic systems**—AI that can actively solve problems and plan rather than just process text.

The conversation highlights several core challenges:

- **Reasoning Gaps:** While AI can solve complex problems (like IMO-level math), it still fails at basic reasoning and self-correction, which Hassabis attributes to a lack of "introspection" in current thought processes.

- **The "Duct Tape" Phase:** Current memory management, such as massive context windows, is described as a brute-force solution. The future requires more elegant **continual learning** models that mimic biological brain processes like REM sleep for memory consolidation.

- **Root Node Problems:** Hassabis views AI as the ultimate tool for science, aiming to solve "root node" problems that unlock entire new fields—using [AlphaFold](https://www.google.com/search?q=https%3A%2F%2Falphafold.google.com%2F) as the primary example of how AI can solve massive combinatorial search spaces.

---

## Detailed Transcription

**[00:00 Opens in a new window ](http://www.youtube.com/watch?v=JNyuX1zoOgU&t=0)** **Demis Hassabis:** Continual learning, long-term reasoning, some aspects of memory—these are still unsolved. I think all of these are going to be required for AGI. Depending on what your AGI timeline is—mine's like 2030 or something like this—then if you start off on a deep tech journey today, you have to just consider AGI appearing in the middle of that journey. It's not bad necessarily, but you have to take that into account. You have to have an active system that can actively solve problems for you to get to AGI. So agents are that path, and I think we're just getting going.

**[00:39 Opens in a new window ](http://www.youtube.com/watch?v=JNyuX1zoOgU&t=39)** **Host:** Demis Hassabis has had one of the most unusual careers in tech. He was a chess prodigy as a kid, then designed his first hit video game, *Theme Park*, at 17. He then went back to school, got a PhD in cognitive neuroscience, published foundational work on how memory and imagination work in the brain, and then in 2010 co-founded DeepMind with one mission: solve intelligence. And I think they've done it. Since then, his lab has gone on to do things most people thought were decades away. AlphaGo beat a world champion at Go. AlphaFold cracked protein structure prediction, a 50-year grand challenge in biology, and they gave it away for free to every scientist on Earth. That work won him the Nobel Prize in chemistry last year. Today Demis leads Google DeepMind, where he's building Gemini and pushing toward the same goal he set when he was a teenager: artificial general intelligence. Please welcome Demis.

**[01:53 Opens in a new window ](http://www.youtube.com/watch?v=JNyuX1zoOgU&t=113)** **Host:** So you've been thinking about AGI longer than almost anyone. When you look at the current paradigm—large scale pre-training, RLHF, chain of thought—how much of the final architecture for AGI do you think we already have, and what's fundamentally missing right now?

**[02:06 Opens in a new window ](http://www.youtube.com/watch?v=JNyuX1zoOgU&t=126)** **Demis Hassabis:** Well, first of all, thanks Gary for that great introduction. It's great to be here. The components that you just mentioned, I'm pretty sure will be part of the final architecture for AGI. I can't see a world in which we will realize in a couple of years this was a dead end. But there still might be one or two things missing on top of what we already know works. Continual learning, long-term reasoning, some aspects of memory—these are still unsolved. And how to get the systems to be more consistent across the board. I think all of these are going to be required for AGI. It might be that the existing techniques can just scale up to that with some innovation... but it could be that there's still one or two big ideas left that need to be cracked. I don't think it's more than one or two.

**[03:27 Opens in a new window ](http://www.youtube.com/watch?v=JNyuX1zoOgU&t=207)** **Host:** Working with a bunch of agentic systems, the wildest thing to me is to what degree it's the same weights over and over. This idea of continual learning is so interesting because right now we're sort of cobbling it together with duct tape—these dream cycles at night and things like that.

**[03:45 Opens in a new window ](http://www.youtube.com/watch?v=JNyuX1zoOgU&t=225)** **Demis Hassabis:** Yeah, the dream cycles. I studied how the hippocampus works and integrates new knowledge gracefully into the existing knowledge base. The brain does that amazingly well during sleep, especially REM sleep, replaying back episodes that are important so that you can learn from it. In fact, our very first Atari program, DQN, used experience replay. We borrowed that from neuroscience and replayed successful trajectories many times. I agree we're using duct tape right now—shove it all in the context window. But this seems a bit unsatisfying. Even though you could have tens of millions of context windows, there's still a cost to looking it up and finding the right thing relevant for the specific decision. I think there's a lot of room for innovation in areas like memory.

**[05:41 Opens in a new window ](http://www.youtube.com/watch?v=JNyuX1zoOgU&t=341)** **Demis Hassabis:** The problem is that we're trying to store everything in that context window—things that are not important, things that are wrong. It's pretty brute force currently. And if you're trying to process live video and you just naively record all the tokens, a million tokens isn't that much—it's only like 20 minutes. You need more if you want something that's going to understand what's going on in your life over a month or two.

**[06:05 Opens in a new window ](http://www.youtube.com/watch?v=JNyuX1zoOgU&t=365)** **Host:** DeepMind has historically leaned into reinforcement learning and search. How much of that philosophy is embedded in how you're building Gemini today? Is RL still underrated?

**[06:26 Opens in a new window ](http://www.youtube.com/watch?v=JNyuX1zoOgU&t=386)** **Demis Hassabis:** I think potentially it is. All of the Atari work and AlphaGo were agent systems—systems able to accomplish goals on their own and make plans. We're seeing thinking modes and chain of thought reasoning as aspects of what was pioneered with AlphaGo coming back now. We're relooking at those old ideas at scale today, including Monte Carlo tree search and other ways of augmenting RL on top of today's foundation models.

**[07:57 Opens in a new window ](http://www.youtube.com/watch?v=JNyuX1zoOgU&t=477)** **Host:** Obviously you need bigger models to be smarter, but we're also seeing distillation working. Frontier models are finding that smaller ones are 95% as good at one-tenth the price.

**[08:22 Opens in a new window ](http://www.youtube.com/watch?v=JNyuX1zoOgU&t=502)** **Demis Hassabis:** I think one of our biggest strengths has been distilling and packing that power into smaller and smaller models. We have a huge need to do it because we serve the biggest AI surfaces—Search, Gemini, Maps, YouTube. That's billions of users. They have to be served extremely fast and efficiently. Our Gemma 2 models show amazing power for their size. I don't see a theoretical limit yet in terms of information density.

**[11:04 Opens in a new window ](http://www.youtube.com/watch?v=JNyuX1zoOgU&t=664)** **Demis Hassabis:** Small models have many uses. Speed allows you to iterate faster, especially in coding collaboration. Another big thing is running these on the edge for privacy and security. For robotics in your house, you're going to want efficient, powerful local models that maybe only delegate to the cloud in certain circumstances.

**[12:32 Opens in a new window ](http://www.youtube.com/watch?v=JNyuX1zoOgU&t=752)** **Host:** Going back to context and memory, models are currently stateless. What would the developer experience be like with a continual learning model?

**[12:46 Opens in a new window ](http://www.youtube.com/watch?v=JNyuX1zoOgU&t=766)** **Demis Hassabis:** Not having continual learning is holding back agents from doing full tasks. They don't adapt well to the context you're in. They need to be able to learn about the specific context you put them in for them to be "fire and forget."

**[13:23 Opens in a new window ](http://www.youtube.com/watch?v=JNyuX1zoOgU&t=803)** **Host:** Where are we on reasoning? Models still fail on things a smart undergrad wouldn't.

**[13:35 Opens in a new window ](http://www.youtube.com/watch?v=JNyuX1zoOgU&t=815)** **Demis Hassabis:** There’s a lot of innovation left in thinking paradigms. We're doing fairly simplistic, brute force things. I think there's scope for monitoring the chain of thought and interjecting midway. Sometimes systems get into loops. I like to play chess against Gemini, and it's interesting because foundation models are pretty poor at games. Sometimes it will consider a move, realize it's a blunder, but because it can't find anything better, it goes back and does it anyway. There's a jagged intelligence—it can solve gold medal IMO problems but make basic elementary math errors. There’s something about introspection missing.

**[15:30 Opens in a new window ](http://www.youtube.com/watch?v=JNyuX1zoOgU&t=930)** **Host:** Agents are big. What does DeepMind's research tell you about where capabilities actually are versus the hype?

**[15:42 Opens in a new window ](http://www.youtube.com/watch?v=JNyuX1zoOgU&t=942)** **Demis Hassabis:** We're just at the beginning. You have to have an active system to get to AGI. We're only in the last couple of months starting to find the really valuable places where it’s not just a toy. I see people setting off dozens of agents for 40 hours, but I'm not sure the output justifies the input yet. I wish I had these tools at 17—I can prototype a game like *Theme Park* in 30 minutes now, which took me 6 months back then. But it still needs human craft, soul, and taste. Why hasn't a kid made a hit game with 10 million copies yet? Something is still missing in the process or tools.

**[18:25 Opens in a new window ](http://www.youtube.com/watch?v=JNyuX1zoOgU&t=1105)** **Demis Hassabis:** Regarding creativity—can a system invent Go? If you give it a high-level description, can it return the game of Go? Today's systems can't do that. It might be that they are capable of it, but they need a brilliant person to provide the impetus and soul.

**[20:17 Opens in a new window ](http://www.youtube.com/watch?v=JNyuX1zoOgU&t=1217)** **Host:** Switching to open source—the release of Gemma... does that change who gets to build?

**[20:42 Opens in a new window ](http://www.youtube.com/watch?v=JNyuX1zoOgU&t=1242)** **Demis Hassabis:** We're huge proponents of open science. We're committed to the open weights path with Gemma. It’s also important to have Western stacks in open source. Strategically, our edge models for Android, glasses, and robotics are best being open because once they are on those surfaces, they are vulnerable anyway.

**[22:18 Opens in a new window ](http://www.youtube.com/watch?v=JNyuX1zoOgU&t=1338)** **Host:** Gemini was built multimodal from the start. What does that buy you?

**[22:46 Opens in a new window ](http://www.youtube.com/watch?v=JNyuX1zoOgU&t=1366)** **Demis Hassabis:** It was harder to start multimodal, but we believe we gain in the long run for world model building. It’s critical for robotics. A digital assistant in the real world needs to understand intuitive physics and the physical context around you.

**[24:04 Opens in a new window ](http://www.youtube.com/watch?v=JNyuX1zoOgU&t=1444)** **Host:** What happens when inference is essentially free?

**[24:11 Opens in a new window ](http://www.youtube.com/watch?v=JNyuX1zoOgU&t=1451)** **Demis Hassabis:** I'm not sure it will ever be free. Jevons Paradox suggests we'll just use whatever we get our hands on—millions of agents or swarms. Energy might become zero-cost with fusion or superconductors, but there's still the bottleneck of physical chip creation.

**[25:20 Opens in a new window ](http://www.youtube.com/watch?v=JNyuX1zoOgU&t=1520)** **Host:** For the bio founders: AlphaFold 3 took us beyond proteins. How close are we to modeling full cellular systems?

**[25:40 Opens in a new window ](http://www.youtube.com/watch?v=JNyuX1zoOgU&t=1540)** **Demis Hassabis:** [Isomorphic Labs](https://www.isomorphiclabs.com/) is trying to build the adjacent biochemistry to design compounds. Eventually, we want a virtual cell—a full working simulation. We're about 10 years away. We're starting with the nucleus because it's self-contained. The issue is data—if we could image a live cell without destroying it, we could turn it into a vision problem.

**[28:15 Opens in a new window ](http://www.youtube.com/watch?v=JNyuX1zoOgU&t=1695)** **Host:** Which scientific domain will transform most in the next five years?

**[28:32 Opens in a new window ](http://www.youtube.com/watch?v=JNyuX1zoOgU&t=1712)** **Demis Hassabis:** My mission was: step one, solve intelligence; step two, use it to solve everything else. I meant solve "root node" problems in science—areas that unlock whole new branches. AlphaFold is the prototypical example. I don't see any area of science this won't help with. We are at an "AlphaFold 1" moment in materials and mathematics.

**[30:40 Opens in a new window ](http://www.youtube.com/watch?v=JNyuX1zoOgU&t=1840)** **Host:** What's the difference between a startup that advances the frontier and one that's just an API wrapper?

**[30:51 Opens in a new window ](http://www.youtube.com/watch?v=JNyuX1zoOgU&t=1851)** **Demis Hassabis:** You have to intercept where the tech is going. The sweet spot is combining AI with another deep technology area—materials, medicine, the world of atoms. Those are defensible areas. Nothing worthwhile is easy. Back in 2010, investors told me AI doesn't work. You need belief and conviction.

**[33:28 Opens in a new window ](http://www.youtube.com/watch?v=JNyuX1zoOgU&t=2008)** **Host:** What makes a scientific domain ripe for a breakthrough?

**[33:34 Opens in a new window ](http://www.youtube.com/watch?v=JNyuX1zoOgU&t=2014)** **Demis Hassabis:** Massive combinatorial search spaces. The more massive, the better. You need a clear objective function—like winning a game or minimizing free energy—and enough data or a simulator to generate synthetic data. Drug discovery is exactly this: finding a needle in a haystack.

**[35:13 Opens in a new window ](http://www.youtube.com/watch?v=JNyuX1zoOgU&t=2113)** **Host:** How close are we to AI systems doing genuine scientific reasoning, not just pattern matching?

**[35:32 Opens in a new window ](http://www.youtube.com/watch?v=JNyuX1zoOgU&t=2132)** **Demis Hassabis:** We're close. We have systems like Co-scientist and AlphaEvolve. But I haven't seen a massive, truly novel discovery yet. It requires analogical reasoning. Can it come up with a hypothesis that's interesting? I call it the "Einstein test": if you train a system on the physics knowledge of 1901, can it come up with special relativity from 1905? Once it can, we're on the verge of true novelty.

**[37:54 Opens in a new window ](http://www.youtube.com/watch?v=JNyuX1zoOgU&t=2274)** **Host:** Last question: What do you know now that you wish you knew at 25?

**[38:23 Opens in a new window ](http://www.youtube.com/watch?v=JNyuX1zoOgU&t=2303)** **Demis Hassabis:** Going after hard problems is no more difficult than going after shallow ones; they are just differently difficult. You might as well put your life force into something that makes a difference. And take the AGI timeline seriously—if you start a 10-year deep tech journey today, AGI will appear in the middle of it. Build something that leverages that.

---

## Use Case & Solution Index

### 1. Software Engineering & Game Development

- **Use Case:** Rapid prototyping of complex software and game systems.

- **Solution:** Using foundation models to reduce development time from months to minutes (e.g., prototyping *Theme Park* style games).

- **Current Gap:** Requires "human soul" and taste to create a market-leading hit.

### 2. Scientific Discovery & Material Science

- **Use Case:** Navigating massive combinatorial search spaces to find specific solutions.

- **Solution:** AlphaFold-style models that use clear objective functions (like energy minimization) to "hill climb" toward a solution.

- **Specific Domain:** Identifying new materials or compounds that physics allows but haven't been found.

### 3. Drug Discovery

- **Use Case:** Designing compounds with specific biochemical properties without side effects.

- **Solution:** [Isomorphic Labs](https://www.isomorphiclabs.com/) uses AI to model biochemistry adjacent to protein structures to predict how drugs will interact with targets.

### 4. Biology & Cellular Modeling

- **Use Case:** Predicting cellular behavior under specific perturbations.

- **Solution:** Creating a "Virtual Cell."

- **Incremental Step:** Starting with a virtual nucleus simulation due to its self-contained nature.

### 5. Robotics & Real-World Interaction

- **Use Case:** Autonomous agents interacting with physical environments (e.g., home robots, [Waymo](https://waymo.com/)).

- **Solution:** Multimodal foundation models that understand "intuitive physics" and the physical context of their surroundings.

### 6. Edge Computing & Privacy

- **Use Case:** Processing personal audio/visual data without sending it to the cloud.

- **Solution:** Distilling frontier models into "Nano" or edge-sized models (like [Gemma](https://ai.google.dev/gemma)) that run locally on devices or glasses.