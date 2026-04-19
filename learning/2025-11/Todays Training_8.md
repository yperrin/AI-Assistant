---
complexity: Intermediate
date: 2025-11-24
id: 2b59fa3b-8750-80b5-9f94-c4f19a86e35e
processed_by_ai: true
summary: This document outlines a six-stage systematic life cycle for prompt engineering,
  from intent formation to deployment, emphasizing the importance of treating prompts
  like code. It also introduces "Hey Presto," a tool designed to assist with the initial
  intent formation and discovery stage.
title: Todays Training
tools_mentioned:
- Claude
- ChatGPT
- LangChain
- Langsmith
- Hey Presto
topics:
- Prompt Engineering
- AI Workflows
- Prompt Life Cycle
- Tool Development
- Software Development Life Cycle
url: https://www.notion.so/Today-s-Training-2b59fa3b875080b59f94c4f19a86e35e
---

- **Prompting is the Wild West** but a critical part of AI workflows [00:07 Opens in a new window ](http://www.youtube.com/watch?v=V0YhpeSOuzk&t=7). The video proposes a **systematic life cycle** for prompts, which includes six stages.

- **The Six Stages of the Prompt Life Cycle:**

	1. **Intent Formation and Discovery** [05:44 Opens in a new window ](http://www.youtube.com/watch?v=V0YhpeSOuzk&t=344): Clarifying the fuzzy goal into a structured, unambiguous prompt. The speaker argues this is the often-missed first step.

	1. **Authoring and Drafting** [00:31 Opens in a new window ](http://www.youtube.com/watch?v=V0YhpeSOuzk&t=31): Writing, refining, and hands-on experimentation with the prompt text (often done in tools like Claude or ChatGPT).

	1. **Versioning and Storage** [01:16 Opens in a new window ](http://www.youtube.com/watch?v=V0YhpeSOuzk&t=76): Treating prompts like code by storing, naming, and tracking changes to ensure persistence and auditability.

	1. **Evaluation and Testing** [02:10 Opens in a new window ](http://www.youtube.com/watch?v=V0YhpeSOuzk&t=130): Comparing prompts, evaluating outputs for accuracy/cost/hallucinations, especially for production-grade prompts.

	1. **Workflow Construction and Automation** [04:03 Opens in a new window ](http://www.youtube.com/watch?v=V0YhpeSOuzk&t=243): Embedding prompts as steps/guideposts within agentic workflows (using tools like LangChain, Langsmith).

	1. **Deployment and Production Integration** [04:53 Opens in a new window ](http://www.youtube.com/watch?v=V0YhpeSOuzk&t=293): Embedding prompts in real applications, requiring robustness, safety, and traceability.

- **Introducing "Hey Presto"** [08:09 Opens in a new window ](http://www.youtube.com/watch?v=V0YhpeSOuzk&t=489): The speaker introduces a tool he built, Hey Presto, specifically to solve the missing **Intent Formation and Discovery** stage, by helping users turn rough notes into high-grade, structured prompts for specific outcomes like code or presentations.

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/800f330d-42f8-47ad-8a9f-47c7834a4d77/25f5703e-02b7-40de-9f11-2d5d572a06d4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWJAJNNV%2F20260419%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260419T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJGMEQCIFbDkugXinusYpT2sOFZ0TvgYYvw9DypRba7MKbN%2F01UAiA1B0UEcoD9ZgDqNxhee6OYZGpRtbI4Yq9oi9ZNZ%2BmZxir%2FAwgCEAAaDDYzNzQyMzE4MzgwNSIMYh6GkmBGDepYSgYrKtwDXLkXKPALb35ylJ2S%2BBwO%2FUSFvormrEIJhVIS8xC%2BTdSs%2FS6Oj1l1IHOsZMUN3NAez1ONkFrW21Cy0KO2kVQp%2FNkt8fqfUvdapSGjNTHqLBNeB7pkQfpUOG1W1bpq%2BDRiFKlgEF1GzOhjuekZsllHP7q0wVxyd72TCURX9rRKCHNp3K9Rw0XqtMwCDWYW7e8oJqr3B7Z2a468E2sXj8XzyLyoVrlBFWdm6pleTmVtqHlk0ZdMI2eNhxsmJVMUVY1nK2OEPRhBLk8B2caypRWBDY2PrVDSlfwnyKl6WtqdxktPnVTX8iuf%2BnlYOoK%2B2O6b9W08jZJi1pnc%2F85oEH6V1mU5IbbMpPo1JGBiwxPwh%2BcPjSFffhtWZs%2F7qulvGmp%2BOBNkX6CXVzv8eg7It%2BlQvst0nMWgCvc8xOBfAMcwQOZPuVQpghUOEkbKznyrbUirdIzCCIcFCjnRMY0L5KADyJIlJgdcjIhye%2Bk1tnAKG4PfiquOnRvfOKt28X1lOSwGjugzD1G9mrNANIWaDTI2EUFr3uXkcSR5WcqfXmnXfEImfAnuu7VHAw7pwaiYdgwwrhLMToxfV%2FJKI%2FX87%2FjOjH%2FpjFMw6Nr4ihy2rnKA%2F8tw8eiGksbeo118Rsww9K2SzwY6pgF67xvRm2f95CfafkC6i1Nbx0pdZHRPh7m%2FpT7sK0dYUwZ3WOQt%2F7Owp9Py6CmYxW5sQ%2F21An2rvRFsMXguCcXOObLY2f3kYUy7WYv3HqnKD6eeEIdb7FefhWsn6oOIzX3QOLFPj35PwnpNHSmSpOPEe9YSxa%2B5PvhL0OxAY5PBe7FkoZSNCMXYnX%2BMhkHS01%2BBRCRUrADO9ZATFDYiOIQ6Zv3u61X1&X-Amz-Signature=79fc8d42d67d9cc394f44e83c418a5723e7672ac8f7ddf46cdd22a9ca0d1babd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)