---
complexity: Intermediate
date: 2026-02-22
id: 30f9fa3b-8750-8014-aab5-e0a1b0956b5c
processed_by_ai: true
summary: This document addresses the problem of "undersampling" AI-generated code,
  where AI produces code much faster than it can be manually reviewed or tested, leading
  to unnoticed errors. It proposes Continuous Integration (CI) as the solution to
  continuously verify AI output through automated testing and fast feedback loops.
title: How to Make the Best of AI Programming Assistants
tools_mentioned: []
topics:
- AI Development
- Continuous Integration
- Software Testing
- Feedback Loops
- Code Quality
- Development Practices
url: https://www.notion.so/How-to-Make-the-Best-of-AI-Programming-Assistants-30f9fa3b87508014aab5e0a1b0956b5c
---

### The Core Problem: Undersampling

- **High-Frequency Production:** AI generates code 10x faster than humans [00:00 Opens in a new window ](http://www.youtube.com/watch?v=XavrebMKH2A&t=0).

- **Low-Frequency Feedback:** Traditional manual reviews and slow testing cycles "undersample" the AI's output [02:16 Opens in a new window ](http://www.youtube.com/watch?v=XavrebMKH2A&t=136).

- **The Result:** Substantial or subtle errors go unnoticed because the checking rate doesn't match the production rate [02:25 Opens in a new window ](http://www.youtube.com/watch?v=XavrebMKH2A&t=145).

### The Solution: Continuous Integration (CI)

- **Sampling at the "Nyquist Rate":** Running full test suites on every single AI-generated change, not in batches [04:51 Opens in a new window ](http://www.youtube.com/watch?v=XavrebMKH2A&t=291).

- **Automated Verification:** Using type checking, linting, and architecture checks to validate output before it reaches production [05:13 Opens in a new window ](http://www.youtube.com/watch?v=XavrebMKH2A&t=313).

- **Behavioral Testing:** Focusing on tests that verify domain logic and behavior rather than just syntax [05:42 Opens in a new window ](http://www.youtube.com/watch?v=XavrebMKH2A&t=342).

### Key Strategies for AI Development

1. **Work in Small Steps:** Avoid large-batch AI changes; request code in smaller, verifiable chunks [06:24 Opens in a new window ](http://www.youtube.com/watch?v=XavrebMKH2A&t=384).

1. **Optimize for Fast Feedback:** Your CI pipeline must be fast (seconds, not 30 minutes) to allow for frequent sampling [06:54 Opens in a new window ](http://www.youtube.com/watch?v=XavrebMKH2A&t=414).

1. **Tests as Source of Truth:** Rely on robust automated tests rather than manual reviews to define correctness [07:13 Opens in a new window ](http://www.youtube.com/watch?v=XavrebMKH2A&t=433).

1. **Avoid Long-Lived Branches:** Use feature branches cautiously and integrate frequently to keep the team synchronized [07:23 Opens in a new window ](http://www.youtube.com/watch?v=XavrebMKH2A&t=443).

1. **Ultimate Feedback:** The deployment pipeline should lead all the way to production, which acts as the final sampling mechanism [07:44 Opens in a new window ](http://www.youtube.com/watch?v=XavrebMKH2A&t=464).

<br/>

<br/>

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/800f330d-42f8-47ad-8a9f-47c7834a4d77/fcfdca03-37c7-489c-a036-a291e1380ad9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOFSLHPV%2F20260419%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260419T141351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJIMEYCIQCgpYsdWe3qimqp0WmCqyqE9SfKNrLTP8c24VADMxooLAIhALjWW9MiCs6LQ2hdgcKXR4oxG9fSOpTS%2Bwt8m9VROJW8Kv8DCAIQABoMNjM3NDIzMTgzODA1IgwW9pdvQFIfuCBLuncq3ANbTcO9xk4TslA7cz61Eto0uxJcNab49tYElsmEo%2FHtvgc9qQ1JJlFzEKWijisW8ZyprYE2TlbZwpiPmQVLILiahEoQMsaBhF6Q%2BhVEIsFk4fkFg0JKIYqphw91X8LVe2HOszqiw5XSmblAHFswk7%2BlcG77QESQnHmDt8AZuru7caNlZb4xj0xmIrP0cTOFVaGAfu2a5VXWVb0SB7J4Sqq9H6kbz9K1NP2x3%2FFksCoY5Cr5zB6cc4f54xr05RqDv%2Fp0yE5NrBnuvGSL%2B3o8Mkf3lD5yhZHW7Z2iVR79EdT2eCU4x1GGy%2Fp8yL%2FTVeWYH8zHX8EyLzH3LXgQUcSatX2SewnQhco1qsbsCLOfJ%2Bac%2FBItiZTfCM2E1IY8BStO0ySiCPYz8dKHPz3HyY5jTiAZovr10lqUebb7CpXqe2j7R5YA8Xz78XitXz%2BZTI%2FEOjgXFgSMCuOPwPVNOhSOIzN1LmyJo7QnI7xLIKQ2JQgi%2FjCHyVWTYAf11g0h9t0ISGBpgqM8cY9iIjpsyQyq9I%2B2Wft%2FvmyPzh5flcclyuR%2Bn5fnMqATjFlAIm%2FXM5CLTy90L10yDtYjHwKk3Ib02YGsHVXGfIzjxBLzfg22ntpexl5YOLUCvUCyuTowNTDJrpLPBjqkAT1VYqfSaMVrv%2FIfzZtQBung8ZdAzldISKbuQXgHJHGTYgnlWE0ro04yfEX0DnFI78c8NlkM4uRNQ8m6kbD5o2BZ2rbi9Rlp%2ByXDfHHI9a0Kn%2F4WRIvBaGLRA3RiuW%2B9deD9ZseLcfWz5ThtpqgaMg0TBv2XKICCdLFLoCPTOmlpYGnHaPGGZQJxKFyp%2FbBsAt9d2WkMT7MY18E72tsI5lMVBDoy&X-Amz-Signature=126062d6ff25329ce2c7046b7d85bdf83732d9b3d82c8a236ef32ff7d6f3b47b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)