---
complexity: Intermediate
date: 2025-11-28 20:38:00-05:00
id: 2ba9fa3b-8750-80e7-b08f-ef7ef2a9df7e
processed_by_ai: true
summary: This document discusses the current state of deep learning, highlighting
  PyTorch as the dominant framework and emphasizing the growing importance of on-device
  AI and edge deployment, particularly with ExecuTorch. It also stresses the benefits
  of local AI (privacy, low latency, cost savings) and the critical role of post-training
  techniques like RAG and fine-tuning, alongside the need for culturally specific
  models.
title: Reading article
tools_mentioned:
- TensorFlow
- PyTorch
- ExecuTorch
topics:
- Deep Learning Frameworks
- On-Device AI
- Edge Deployment
- Privacy
- Low Latency
- Cost Savings
- Post-training
- Retrieval-Augmented Generation (RAG)
- Fine-tuning
- Culturally Specific Models
url: https://www.notion.so/Reading-article-2ba9fa3b875080e7b08fef7ef2a9df7e
---

- State of Deep Learning Frameworks: While Moroney acknowledges the importance of TensorFlow in the past, he notes that PyTorch has become the primary framework for building machine learning models today. He encourages developers to focus on building complete solutions rather than engaging in "framework wars," letting the framework be secondary to the overall product.

- On-Device AI and Edge Deployment: The ability to run AI models directly on user devices ("AI at the Edge") is critical. With the recent release of ExecuTorch 1.0 (a PyTorch runtime), developers now have a strong open-source option for deploying models to mobile (Android, iOS) and other edge devices (cars, robots).

- Benefits of Local AI: Deploying models locally offers major advantages:

	- Privacy: It keeps sensitive data (like corporate scripts or personal photos) off the cloud. Moroney cites Hollywood studios, who fear IP leaks, as a prime example of entities requiring local LLMs for script analysis and costing.

	- Low Latency: Processing happens instantly on the device, improving user experience.

	- Cost Savings: App vendors save time and money by not having to maintain cloud services for every AI function (e.g., on-device photo search).

- Developer Focus and "Small AI": Moroney argues that posttraining—the process of adapting or improving models using techniques like Retrieval-Augmented Generation (RAG) and fine-tuning—is the single most important skill for developers moving forward. He predicts that "small AI" will be the next major buzzword after "agents."

- Cultural Specificity: He stresses that culturally specific models are necessary because most Large Language Models (LLMs) are trained primarily on English, creating a technical disadvantage (tokenization issues) for languages like Gaelic, Chinese, or Japanese.
The full discussion is available on the O'Reilly learning platform.