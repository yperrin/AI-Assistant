---
complexity: Intermediate
date: 2025-11-08 12:32:00-05:00
id: 2a59fa3b-8750-8015-a379-c2d581024c1e
processed_by_ai: true
summary: This document explains key classification evaluation metrics like Recall
  (TPR), Precision, and TNR, detailing their formulas, differences, and appropriate
  use cases. It also introduces open and axial coding methodologies for analyzing
  AI model failures, describing how granular observations are categorized into a structured
  failure taxonomy.
title: Todays learning
tools_mentioned: []
topics:
- Classification Metrics
- Recall
- Precision
- True Negative Rate (TNR)
- AI Model Evaluation
- Qualitative Data Analysis
- Open Coding
- Axial Coding
- Failure Taxonomy
url: https://www.notion.so/Today-s-learning-2a59fa3b87508015a379c2d581024c1e
---

> Please analyze the following  csv file. There is a metadata field which has a nested field called z_note that contains open codes for the analysis of LLM logs that we are conducting.
Please extract all the different open codes. From the z_note field, propose 5-6 categories that we can create axial codes from.

<br/>

- **TPR is the same as Recall.**

- **TNR is a completely different metric from Precision.**

---

## 📐 The Relationship Between Metrics

- **TP** = True Positives

- **TN** = True Negatives

- **FP** = False Positives

- **FN** = False Negatives

---

## 🔑 Key Differences

### 1. TPR vs. Precision (and Recall vs. Precision)

- **Recall (TPR):** Measures the proportion of correctly identified positives *out of all ****actual**** positives* (6$\frac{TP}{TP + FN}$).7 It assesses the model's ability to find all relevant cases.

- **Precision:** Measures the proportion of correctly identified positives *out of all ****predicted**** positives* (9$\frac{TP}{TP + FP}$).10 It assesses the quality of the positive predictions (i.e., minimizing False Positives).

- High **Recall** is crucial when the cost of a **False Negative (FN)** is high (e.g., missing a disease diagnosis).11

- High **Precision** is crucial when the cost of a **False Positive (FP)** is high (e.g., flagging a legitimate financial transaction as fraud).12

### 2. TNR vs. The Other Metrics

- **TNR** focuses entirely on the **Negative class**. It measures how well the model identifies the *actual negative* cases.

- **Recall (TPR)** and **Precision** focus only on the **Positive class** and how well it is identified or predicted.13

---

 | **Metric Name** | **Alternative Name** | **Formula** | **Denominator Focus** | 
 | ---- | ---- | ---- | ---- | 
 | **Recall (or TPR)** | **True Positive Rate (Sensitivity)** | $\frac{TP}{TP + FN}$ | **Actual Positives** (Out of all positive instances, how many did we correctly find?) | 
 | **Precision** | Positive Predictive Value (PPV) | $\frac{TP}{TP + FP}$ | **Predicted Positives** (Out of all our positive predictions, how many were actually correct?) | 
 | **TNR** | **True Negative Rate (Specificity)** | $\frac{TN}{TN + FP}$ | **Actual Negatives** (Out of all negative instances, how many did we correctly find?) | 

<br/>

<br/>

---

# Resources

## 🔍 Open Coding in AI Evals

- **Goal:** To break down raw data (in this case, logs or traces of an AI model's problematic outputs/failures) into distinct, fundamental concepts.

- **Process:** A human annotator or domain expert reviews each trace or failure and assigns **short, descriptive, open-ended notes** or labels (the "open codes") about what went wrong. This is often akin to "journaling" the failures.

- **Output:** A large, comprehensive list of specific failure instances and observations. These codes are very granular and close to the raw data.

- "Refused to answer question about X."

- "Hallucinated non-existent date."

- "Output was overly verbose."

- "Misunderstood the user's intent to be aggressive."

---

## 🧩 Axial Coding in AI Evals

- **Goal:** To organize the numerous, granular open codes into **broader, more abstract categories** or themes, identifying relationships and connections between them. This essentially creates a **failure taxonomy**.

- **Process:** The analyst reviews the open codes and groups similar ones together to form higher-level themes (the "axial codes"). This connects individual failure observations to central concepts, which become the "axes" for further analysis.

- **Output:** A structured hierarchy of failure categories that provides a clear, high-level view of the model's systematic weaknesses.

- **Refusal/Guardrails** (Group for "Refused to answer question about X")

- **Factual Errors/Hallucination** (Group for "Hallucinated non-existent date")

- **Style/Format Issues** (Group for "Output was overly verbose")

- **Misinterpretation/Safety** (Group for "Misunderstood the user's intent to be aggressive")