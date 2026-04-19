---
complexity: Advanced
date: 2026-01-13 14:28:00-05:00
id: 2e79fa3b-8750-804f-a46b-f0f1f7845cd2
processed_by_ai: true
summary: This document details experiments comparing various AI models and methods
  for generating software, highlighting that the planning phase acts as a filter,
  making the initial model less critical than expected. The key challenge identified
  is the loss of intent and requirements during the handoff from PRD to planning,
  emphasizing the importance of iterative verification and intent preservation for
  successful AI-driven development.
title: Experiment with building requirements
tools_mentioned:
- GPT-5.2 Instant
- GPT-5.2 Pro
- Claude Code
- Opus 4.5
topics:
- AI Model Comparison
- Software Development
- Product Requirement Documents (PRDs)
- AI Planning
- Intent Preservation
- Iterative Verification
url: https://www.notion.so/Experiment-with-building-requirements-2e79fa3b8750804fa46bf0f1f7845cd2
---

### **The Experiments**

1. **Model Tier Comparison:** He generated Product Requirement Documents (PRDs) using eight different models, ranging from **GPT-5.2 Instant** (15 seconds) to **GPT-5.2 Pro** (15 minutes) [02:22 Opens in a new window ](http://www.youtube.com/watch?v=G7I9VAgUgxw&t=142). All PRDs were then fed into the same build system (**Claude Code** with **Opus 4.5**) [00:30 Opens in a new window ](http://www.youtube.com/watch?v=G7I9VAgUgxw&t=30).

1. **Direct-to-Build:** He bypassed the PRD stage entirely by feeding a 15-minute voice memo (his "intent document") directly into Claude Code's planning mode [05:03 Opens in a new window ](http://www.youtube.com/watch?v=G7I9VAgUgxw&t=303).

1. **Direct-to-Execution:** He skipped planning altogether and commanded the system to build the app directly from his voice memo [05:40 Opens in a new window ](http://www.youtube.com/watch?v=G7I9VAgUgxw&t=340).

1. **Intent-Focused PRDs:** He added explicit instructions to "carry the intent through" (explaining the *why* behind features) to see if preserving nuance improved the build [11:32 Opens in a new window ](http://www.youtube.com/watch?v=G7I9VAgUgxw&t=692).

1. **Multi-Pass Planning:** He forced the AI to perform "triple planning" by comparing its created plan against the original PRD multiple times to identify and re-add dropped requirements [14:28 Opens in a new window ](http://www.youtube.com/watch?v=G7I9VAgUgxw&t=868).

### **Key Conclusions**

- **The "Planning Filter" Effect:** Surprisingly, the builds from "Instant" models and "Pro" models were almost indistinguishable [00:41 Opens in a new window ](http://www.youtube.com/watch?v=G7I9VAgUgxw&t=41). The sophisticated planning mode in tools like Claude Code acts as a filter that "smooths out" the quality of the PRD, making the specific model used for the PRD less important than expected [09:58 Opens in a new window ](http://www.youtube.com/watch?v=G7I9VAgUgxw&t=598).

- **Silent Losses at Handoffs:** The biggest issue isn't model intelligence; it's the loss of **intent** and requirements during the transition from PRD to Plan [11:06 Opens in a new window ](http://www.youtube.com/watch?v=G7I9VAgUgxw&t=666). Even high-quality PRDs saw 20–30% of requirements dropped during the initial planning phase [14:15 Opens in a new window ](http://www.youtube.com/watch?v=G7I9VAgUgxw&t=855).

- **Verification is Critical:** The most successful build came from **iterative verification**—explicitly asking the AI to find what it missed in its plan and updating it before starting the code [14:36 Opens in a new window ](http://www.youtube.com/watch?v=G7I9VAgUgxw&t=876).

- **Intent Preservation:** Using a model that can preserve the "why" (like Opus 4.5, which scored 99% on requirement preservation in his test) leads to a product that feels more like the author's original vision rather than a "sterile" checklist [12:17 Opens in a new window ](http://www.youtube.com/watch?v=G7I9VAgUgxw&t=737).