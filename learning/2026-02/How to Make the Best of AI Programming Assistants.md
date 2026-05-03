---
complexity: Advanced
date: 2026-02-22
id: 30f9fa3b-8750-8014-aab5-e0a1b0956b5c
processed_by_ai: true
summary: Dave Farley discusses the engineering challenges of integrating AI assistants
  like Claude Code into software development, emphasizing the need for feedback mechanisms,
  particularly Continuous Integration, to evolve and match the high frequency of AI-generated
  code production. He applies the Nyquist-Shannon Sampling Theorem to explain why
  traditional feedback loops "undersample" AI output, leading to errors.
title: How to Make the Best of AI Programming Assistants
tools_mentioned:
- Claude Code
- Continuous Integration
topics:
- AI in Software Development
- Continuous Integration
- Software Engineering
- Feedback Loops
- Automated Testing
- Nyquist-Shannon Sampling Theorem
url: https://www.notion.so/How-to-Make-the-Best-of-AI-Programming-Assistants-30f9fa3b87508014aab5e0a1b0956b5c
---

In this video, **Dave Farley** from [Modern Software Engineering](http://www.youtube.com/watch?v=XavrebMKH2A) discusses the engineering challenges of using AI assistants like Claude Code. He argues that as AI increases the frequency of code production, our feedback mechanisms must evolve to keep pace.

### The Core Problem: Undersampling

Farley applies the **Nyquist-Shannon Sampling Theorem** to software development [01:04 Opens in a new window ](http://www.youtube.com/watch?v=XavrebMKH2A&t=64). The theorem states that to accurately represent a signal, you must sample it at least twice as fast as its highest frequency.

- **High-Frequency Production:** AI generates code 10x faster than humans [00:00 Opens in a new window ](http://www.youtube.com/watch?v=XavrebMKH2A&t=0).

- **Low-Frequency Feedback:** Traditional manual reviews and slow testing cycles "undersample" the AI's output [02:16 Opens in a new window ](http://www.youtube.com/watch?v=XavrebMKH2A&t=136).

- **The Result:** Substantial or subtle errors go unnoticed because the checking rate doesn't match the production rate [02:25 Opens in a new window ](http://www.youtube.com/watch?v=XavrebMKH2A&t=145).

### The Solution: Continuous Integration (CI)

Farley reframes **Continuous Integration** as a definitive sampling strategy rather than just a pipeline [03:43 Opens in a new window ](http://www.youtube.com/watch?v=XavrebMKH2A&t=223). To effectively manage AI-generated code, he recommends:

- **Sampling at the "Nyquist Rate":** Running full test suites on every single AI-generated change, not in batches [04:51 Opens in a new window ](http://www.youtube.com/watch?v=XavrebMKH2A&t=291).

- **Automated Verification:** Using type checking, linting, and architecture checks to validate output before it reaches production [05:13 Opens in a new window ](http://www.youtube.com/watch?v=XavrebMKH2A&t=313).

- **Behavioral Testing:** Focusing on tests that verify domain logic and behavior rather than just syntax [05:42 Opens in a new window ](http://www.youtube.com/watch?v=XavrebMKH2A&t=342).

### Key Strategies for AI Development

1. **Work in Small Steps:** Avoid large-batch AI changes; request code in smaller, verifiable chunks [06:24 Opens in a new window ](http://www.youtube.com/watch?v=XavrebMKH2A&t=384).

1. **Optimize for Fast Feedback:** Your CI pipeline must be fast (seconds, not 30 minutes) to allow for frequent sampling [06:54 Opens in a new window ](http://www.youtube.com/watch?v=XavrebMKH2A&t=414).

1. **Tests as Source of Truth:** Rely on robust automated tests rather than manual reviews to define correctness [07:13 Opens in a new window ](http://www.youtube.com/watch?v=XavrebMKH2A&t=433).

1. **Avoid Long-Lived Branches:** Use feature branches cautiously and integrate frequently to keep the team synchronized [07:23 Opens in a new window ](http://www.youtube.com/watch?v=XavrebMKH2A&t=443).

1. **Ultimate Feedback:** The deployment pipeline should lead all the way to production, which acts as the final sampling mechanism [07:44 Opens in a new window ](http://www.youtube.com/watch?v=XavrebMKH2A&t=464).

Farley concludes that as the bottleneck of "typing speed" disappears, software development must prioritize **feedback as a first-class engineering concern** [08:31 Opens in a new window ](http://www.youtube.com/watch?v=XavrebMKH2A&t=511).

<br/>

<br/>

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/800f330d-42f8-47ad-8a9f-47c7834a4d77/fcfdca03-37c7-489c-a036-a291e1380ad9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W4FWLT43%2F20260503%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260503T185829Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGF7yKVSS7%2FrHdYbVo98%2FlbAxui4CRLBfjaJE3fCikSBAiEAr%2F9AYfySrgVAAhHUYUzpUEepUsXv%2B8vWeAGVxQIGDmIq%2FwMIWxAAGgw2Mzc0MjMxODM4MDUiDEC7hRXigwQ6V4rxwyrcA5zGnTCDMQuwQ%2BgN1hKlhRQec9sOE7kr8tPD8Xw2HGK3NM%2Fl5U8ikRAErIFfDRzMNQxygGSq7vOhI4lOYjjb76%2Bv2qJKvHBn%2FIdlf6lv2ubnLbscbylunypxuDjjgo15eeYz6CSIf4V%2BlwsEdxqc6AK0GnWjTAJihpYPl4VgxS%2Bh%2FH0OKCIZkuamifu0jno2jXpCbzh0Wr%2BvZBjFQYRv78chXJktmcJ93tdy2vDfYHIb0w86OQN0QQQVY5JVbjy1oK2PZTZmEaz3yw9ZPvgJoWO6HzBz26bFh87jf59c%2Bm3RGcKzLPqWGzUocozu%2BkYawzI3lB54BwSJ8%2BtGVeUqPnwrOppDYTSf3UlbaLLZMXUlvpYAhq9D4SRZ34txtmzZJ3K4RoDeX%2BLTBybTM8F6%2FJc6Aun3PckAi6zw1mndvFODfUlLAZZkQ3QVNkmSevF56nKKp2Z9QAYr8irVNRJppq0hAvvaPDAaR1LVtjdyX0zVgvNxxEX6P4idzHZNI2CPKSYqgty%2F9A%2BSlObYgLrhCmTdVeWxfxEmsMlo0am3leHNupJg1MtL5gBbC%2FmK3twTvpyC%2F0JfA92PtTVvoiNNx1JYIYE0PDW5WDDSascQYtbVMwL8Ozu8jP0glegCMKqb3s8GOqUBTVYq4AvN2lzTHiajpCIG%2BbuEgxZorGHA9H5RKdPsUkgvmugulgBXvqawuRCc3KCPwW3b7PXcMuAXj1AymnjmRMnm2Dd05gCehcNkFep6OlkPZm7ZNO6GNPiU%2FcWu8U6MUFUJQpK4xAXJyiSDFdA4Q0%2FunrTS%2ByUUZ9TkAHWhKwnhi%2FDjCfFh9xpGuXU1xsaj6a%2FuAv2Ov9%2FBictTIJNg%2BJDzVt9R&X-Amz-Signature=140b0e0575b3dc906c8accd872cbdbc1a6ed736fe5b0c769c5552d82200856b9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)