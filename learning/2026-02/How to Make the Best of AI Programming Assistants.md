---
title: How to Make the Best of AI Programming Assistants
id: 30f9fa3b-8750-8014-aab5-e0a1b0956b5c
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

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/800f330d-42f8-47ad-8a9f-47c7834a4d77/fcfdca03-37c7-489c-a036-a291e1380ad9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LEBTNGG%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T163628Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIE1f8L1hi4LMGDKrzYOIG9MqyHd7UKrr5nBipcOtJGfaAiEA9wSXMdh2562Ls7tjW1e4aKUhU7jQ7TDL3issJHmzGrkq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDMvkljZ8%2F4ohboh9sSrcA5Woj0Mcr1ohShR%2FkTzo0IoLXwF0rA64rJPk7q5m%2B35yyDz5t6r1BmHh7qDLr0ILPZ9qEmuVJCagolZJCP%2Ff115dg3NfKy9sk%2B5uLMtkFh1edUhhkKa42sLf%2BDO%2B0y7r66U1mXwkTgdoUpOxuNNLvIjN9I5Y1nG7gNVP5AoGQT%2F3SO%2Fu916OqJc%2BKm1ZQYXsdx%2BkqtV%2Fi6%2FP10xI%2FjcSbixDlo1sfqwRb5ictSJTARaO54XsmU5Z4%2FujByXPYM0NLE3OeheZU9ilmawNp77zdv5MbBEFKYH0kTFZfBZhu4cM7njaAePGN8hSUK0vNkfsRRkyjRqyZzSjA%2Fz6Q09hNw6sWJ8VL7%2BK0pgf1KRgtM6ZQWESapJ1ggyIqhWW9h3cODLsmC4uwxggjLuh4sw9SIJ3HdI5OH7vD5TF1%2BE1HfZb%2FzrUo0JyEkMU2lrGvhbEeE90tFeY22ld8YrJ4Hd3WYwOuQ3lmhlxtIl1%2FMZCZqtrhXVTdMuK%2F5tvG%2FVj%2FaxFuqEyPIxxr2Gfn%2BQewlniDe2ZefSmUBnicLd6GVjmMBe4dudghSV0q47jw3M1csxpXk2kFXaAA3EOAEm%2BjJPHdCMp0JPTniJXeKWDk5Q3cYIqyln%2FZ8UCSNuggsowMNKTpc4GOqUBWVhfs%2BHS91eYfYYnWC9e9WmVya6eP6ucQbXNNwjYCRfNILDkYLXLqIgUgpRMuBCXdSPRAlTeFqYb76H3sAR%2FxRyJvY0UJmZEhR61Ifnod00ubUZWROw09tebqF7UHIRuEs7l8rScuYCdDHQQbjibWerj24MyryI%2BYLbtzzasSANn4r%2BVQ4aSt7fg1Dherx6%2F2V%2BBvt85bpgQJv3CD5U%2FPr%2FsRneo&X-Amz-Signature=35004c1f97d4d93e23353c4a0acde9b6769babc3fa3ab3b8a493bf5cb27b70a8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

