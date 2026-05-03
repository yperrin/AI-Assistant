# Keeping up with the AI Reset

**By:** [Yann Perrin](https://clarivate.atlassian.net/wiki/spaces/LSHT/blog/2026/03/21/268599298/Keeping+up+with+the+AI+Reset)  
**Date:** March 21, 2026  
**Read Time:** 4 min

In my recent talks, I often mention the multiple challenges we face when using AI in the SDLC. I want to talk about the ones we are facing already and one we will be facing later once we get better at it. I am talking about:

* Prompt Engineering
* Context Engineering
* Memory management

---

## Prompt Engineering

We are all mostly familiar with this one, but there are basic concepts and vocabulary we should be aware of. Good prompt engineering allows us to get better results in fewer iterations and allows us to use smaller models to get to the same result.

### The Essentials
* **Tasks:** Describe what you are trying to do, what persona to adopt, and what format you need the data in.
* **Context:** Provide the necessary information so the model can make decisions, including intent and boundaries.
* **References:** Examples of what you are trying to achieve:
    * **No-shot prompting:** No examples provided.
    * **One-shot prompting:** One example provided.
    * **Multi-shots prompting:** Many examples provided.
* **Evaluate & Iterate:** Run the prompt and keep going until you get the result you want.

### Advanced Strategies
* **Prompt Chaining:** Using the result from one prompt to feed another.
* **Chain of Thought:** Asking the model to explain its reasoning.
* **Tree of Thought:** Asking the model to create multiple solutions with pros and cons.
* **Meta-prompting:** Asking the model to create a prompt for you.

---

## Context Engineering

At its basis, this is all about the additional information you provide the model. This is the next level of maturity—understanding how models degrade as more data is passed in (independently of advertised context limits) and why they may start hallucinating or regurgitating rejected solutions.

This becomes vital as we move toward **brown field projects** with large codebases where you cannot pass everything in a single prompt. Solutions like **RAG (Retrieval-Augmented Generation)** become necessary to handle these large volumes of data as we delegate more to independent agents.

---

## Memory

The next level involves **Agentic Workflows**—agents that work on problems independently (e.g., performing market analysis overnight). 

To collaborate effectively, multiple agents working on the same problem need to share a **common memory**. While some current systems use local Markdown files, running agents in parallel and allowing concurrent memory updates presents significant challenges. We are still in the early stages of this, but it is a challenge we will need to tackle in the near future.

---

### Model Reasoning Styles
* **Gemini:** Focused on Planning and Research.
* **ChatGPT:** Focused on Logical Reasoning with hidden chain of thought.
* **Claude:** Focused on Nuance, Context, and explaining steps.