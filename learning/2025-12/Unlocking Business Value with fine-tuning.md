---
title: Unlocking Business Value with fine-tuning
id: 2d39fa3b-8750-8021-a451-f9eab583a386
url: https://www.notion.so/Unlocking-Business-Value-with-fine-tuning-2d39fa3b87508021a451f9eab583a386
---

---

### Key Takeaways

- **When to Fine-Tune:** Use it when prompt engineering and [RAG](https://marketingassets.microsoft.com/gdc/gdcaQpL2m/original?ocid=eml_pg488409_gdc_comm_az&mkt_tok=MTU3LUdRRS0zODIAAAGb8JgQSnAvR94R_ieK6OJxP5ChxmoCC_qLi3SYxWK2SYGzyJtxGZBUBW4UWbiE5rrkNgtfV9wASntCiFuftyZR1EAWBSe9d4_GB3fA0K7FsorTgmXGIfLB3JVF) reach their limits—specifically for niche terminology, strict formatting, or reducing latency/token costs by shortening prompts.

- **The Hybrid Approach (RAFT):** The most effective strategy often combines [Retrieval Augmented Generation (RAG)](https://marketingassets.microsoft.com/gdc/gdcaQpL2m/original?ocid=eml_pg488409_gdc_comm_az&mkt_tok=MTU3LUdRRS0zODIAAAGb8JgQSnAvR94R_ieK6OJxP5ChxmoCC_qLi3SYxWK2SYGzyJtxGZBUBW4UWbiE5rrkNgtfV9wASntCiFuftyZR1EAWBSe9d4_GB3fA0K7FsorTgmXGIfLB3JVF) for real-time facts with fine-tuning for domain-specific behavior.

- **Techniques:** * **SFT (Supervised Fine-Tuning):** Teaching the model with direct input-output pairs.

	- **DPO (Direct Preference Optimization):** Aligning the model based on human "thumbs up/down" preferences; faster and more stable than traditional RLHF.

	- **Distillation:** Using a large "teacher" model (like GPT-4o) to train a smaller, cheaper "student" model (like Phi-3).

- **Data is King:** Success depends on high-quality, curated datasets. While the technical minimum is 10 examples, the guide recommends hundreds or thousands for meaningful improvement.

### Core Benefits

1. **Lower Latency:** Faster inference because the model needs fewer instructions in the prompt.

1. **Cost Efficiency:** Smaller models can be fine-tuned to match the performance of larger ones for specific tasks.

1. **Specialization:** Improved handling of edge cases and "industry-speak" (e.g., medical, legal, or agricultural terms).

---

