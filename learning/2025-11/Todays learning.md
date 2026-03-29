---
title: Todays learning
id: 2a39fa3b-8750-805c-acd3-c0ab0aaf8414
url: https://www.notion.so/Today-s-learning-2a39fa3b8750805cacd3c0ab0aaf8414
---

<br/>

---

### 1. The Projection Trap

- **Issue:** Users project capabilities onto the model that it does not have, often resulting in an **underspecified prompt** [00:20 Opens in a new window ](http://www.youtube.com/watch?v=KwQpPbLEBMA&t=20). For example, asking for a "professional update" without specifying the audience or length [00:54 Opens in a new window ](http://www.youtube.com/watch?v=KwQpPbLEBMA&t=54).

- **Solution:** Use **schema-first prompting** [01:31 Opens in a new window ](http://www.youtube.com/watch?v=KwQpPbLEBMA&t=91). Instead of writing a prompt forward, define the exact structure or schema of the output you want, which serves as a map for the AI [01:13 Opens in a new window ](http://www.youtube.com/watch?v=KwQpPbLEBMA&t=73).

---

### 2. The Revision Loop

- **Issue:** Asking for a small fix causes the model to **rewrite the whole thing** or touch elements you didn't want it to change [02:21 Opens in a new window ](http://www.youtube.com/watch?v=KwQpPbLEBMA&t=141).

- **Solution:** Be absolutely **surgical** in your request [03:13 Opens in a new window ](http://www.youtube.com/watch?v=KwQpPbLEBMA&t=193). Quote the **exact snippet you want changed** and request only that patched section back [03:21 Opens in a new window ](http://www.youtube.com/watch?v=KwQpPbLEBMA&t=201). Alternatively, if using a schema, specify that only a certain field should be touched, freezing the others [03:36 Opens in a new window ](http://www.youtube.com/watch?v=KwQpPbLEBMA&t=216).

---

### 3. The Planning Illusion

- **Issue:** For complex multi-step tasks (like "analyze churn and propose a plan"), the model will often **collapse the task into one single, shallow response**, skipping crucial reasoning steps [04:22 Opens in a new window ](http://www.youtube.com/watch?v=KwQpPbLEBMA&t=262).

- **Solution:** Break the challenge into **stages with explicit outputs and validation gates at each stage** [05:00 Opens in a new window ](http://www.youtube.com/watch?v=KwQpPbLEBMA&t=300). Force a step-by-step progression by instructing the model to complete only one stage and then stop before moving to the next [05:08 Opens in a new window ](http://www.youtube.com/watch?v=KwQpPbLEBMA&t=308).

---

### 4. The Confidence Illusion (Hallucination)

- **Issue:** The model provides **fluent but incorrect answers** with mismatched or non-existent citations [06:44 Opens in a new window ](http://www.youtube.com/watch?v=KwQpPbLEBMA&t=404).

- **Solution:** Require the model to say **"I don't know"** when unsure and to provide **confidence labels** with its answers [06:51 Opens in a new window ](http://www.youtube.com/watch?v=KwQpPbLEBMA&t=411). An advanced fix is to use "chain of verification prompting" to name the conditions under which the model can move forward and print a response [07:20 Opens in a new window ](http://www.youtube.com/watch?v=KwQpPbLEBMA&t=440).

---

### 5. The Drift Problem

- **Issue:** **Consistency issues** where the same inputs result in different, inconsistent outputs across runs, such as generated tags or categories that drift [08:03 Opens in a new window ](http://www.youtube.com/watch?v=KwQpPbLEBMA&t=483).

- **Solution:** **Turn the model temperature down** (in the API) and **set absolute constraints** in the chat [08:11 Opens in a new window ](http://www.youtube.com/watch?v=KwQpPbLEBMA&t=491). Your job is to be extremely obsessive about **token-level clarity and consistency** in your inputs and to take away all ambiguity that invites creativity from the model [09:04 Opens in a new window ](http://www.youtube.com/watch?v=KwQpPbLEBMA&t=544).

---

### 6. The Cognitive Bandwidth Trap

- **Issue:** The user includes **too much context**, leading to worse outputs, even with large context windows [09:16 Opens in a new window ](http://www.youtube.com/watch?v=KwQpPbLEBMA&t=556). Users mistakenly think accumulating a "pile" of context is helpful [10:30 Opens in a new window ](http://www.youtube.com/watch?v=KwQpPbLEBMA&t=630).

- **Solution:** Have **clean context loading** and default to providing **as little context as is humanly possible** to get the model to complete the task [09:30 Opens in a new window ](http://www.youtube.com/watch?v=KwQpPbLEBMA&t=570). Focus on the necessary "slice of context" instead of the full document [09:51 Opens in a new window ](http://www.youtube.com/watch?v=KwQpPbLEBMA&t=591).

---

