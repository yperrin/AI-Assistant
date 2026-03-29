---
title: Todays training
id: 2a19fa3b-8750-80ea-bf22-fbd1ef7d00d7
url: https://www.notion.so/Today-s-training-2a19fa3b875080eabf22fbd1ef7d00d7
---

> Before coding anything:

> /openspec:proposal [your feature description]

> Review and iterate:

> openspec validate <change-name>
openspec show <change-name>

> When ready:

> /openspec:apply <change-name>

> After completion:

> /openspec:archive <change-name>

> 

> Decided Notion would be a good way to record the training sessions and then have a summary at the end of the week for my teams post.

<br/>

---

- **1. Error Analysis (The Most Valuable Step):**

	- **Collect and Review Traces:** Look at a minimum of 100 interaction logs (traces) with your AI product (like the property management assistant "Nurture Boss") and write down notes (open codes) about what is going wrong [05:00 Opens in a new window ](http://www.youtube.com/watch?v=uiza7wp1KrE&t=300).

	- **Categorize Problems:** Use an LLM or a tool to analyze your notes and group them into categories (axial codes) like "Human Handoff/Transfer Issue" or "Conversational Flow Issues" [11:03 Opens in a new window ](http://www.youtube.com/watch?v=uiza7wp1KrE&t=663).

	- **Prioritize Fixes:** Count the frequency of the categorized issues to identify the most painful problems to fix first [14:18 Opens in a new window ](http://www.youtube.com/watch?v=uiza7wp1KrE&t=858).

- **2. Building an LLM Judge:**

	- **Focus on Binary Scores:** When creating a specific LLM judge for a problem (e.g., human handoff), prompt it to return a **binary score (True/False)** rather than a subjective rating scale (1-5) [24:38 Opens in a new window ](http://www.youtube.com/watch?v=uiza7wp1KrE&t=1478). Scores like 3.2 vs. 3.7 are not actionable and lead to a lack of trust in the evaluation [25:10 Opens in a new window ](http://www.youtube.com/watch?v=uiza7wp1KrE&t=1510).

	- **Calibrate the Judge (Meta-Evaluation):** Use a **confusion matrix** to test the LLM judge against your human-labeled data (ground truth) [31:06 Opens in a new window ](http://www.youtube.com/watch?v=uiza7wp1KrE&t=1866). This step is critical to ensure your judge is trustworthy.

	- **Avoid "Agreement" as a Metric:** Agreement is misleading. Instead, focus on **True Positive Rate** (correctly identifying a failure) and **True Negative Rate** (correctly identifying a non-failure) [30:23 Opens in a new window ](http://www.youtube.com/watch?v=uiza7wp1KrE&t=1823).

- **3. Deployment and Iteration:**

	- **Run Judges in Production:** Deploy the specific, calibrated LLM judges to run on samples of production traces for continuous monitoring and to help you debug errors [36:26 Opens in a new window ](http://www.youtube.com/watch?v=uiza7wp1KrE&t=2186).

	- **Continuous Improvement:** Continue to manually review traces (error analysis) on a regular cadence to ensure you are not missing new or subtle failures [39:39 Opens in a new window ](http://www.youtube.com/watch?v=uiza7wp1KrE&t=2379).

