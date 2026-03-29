---
title: Training in Graph RAG step1
id: 2c39fa3b-8750-80a6-954c-c7c3ee60286a
url: https://www.notion.so/Training-in-Graph-RAG-step1-2c39fa3b875080a6954cc7c3ee60286a
---

- First asked Claude what concept I needed to learn based on my background, then asked for a prompt I can run un perplexity to learn those concepts.

- Ask AI how to get started: *If I want to learn graph RAG, given my current focus and background, what would be the best tools for me to use to get a project started. Ask me any necessary questions for you to be able to answer this question.*

	- Claude asked me 10 qualifying questions then suggested a 4+ week learning program with a starter guide and code samples

		- LlamaIndex - python

		- Newo4j community edition

		- Ollama

	- Gemini proposed multiple solutions and then asked 3 questions (though they do know about me)

		- First pass

			- n8n + ollama + neo4j

			- Microsoft GraphRAG + local Ollama for zero costs

		- Second pass after answering the questions

			- Option A - n8n + Ollama + Neo4j providing docker configuration and database structure + offering to write the n8n workflow for me.

			- Option B - Similar with coding in C# to extract entities from documents.

	- Based on the topics uncovered, use the new feature within notebookLM to search for sources. This also adds YouTube videos.

	- Do a search directly in Youtube - use videos from people I watch regularly already.

	- Ask for negative/comparison 

		- What are the reasons why a GraphRag project fails?

		- What are the scenarios where GraphRag performs worse than RAG

	<br/>

		- Audio overview customized to introduction and use cases

	- Mind map (of everything)

	- Video overview (provide a topic)

	- Infographic (provide a topic)

<br/>

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/800f330d-42f8-47ad-8a9f-47c7834a4d77/b00931ef-35f8-48e8-af2b-4dc14ae26312/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WDPY5HJX%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T163518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJIMEYCIQCc%2B5oHLVv8Y0HAsTZ%2BPzw88BeQq6RpoX%2Fri0kuzGTOBAIhAPMeCHuc7qKAGIA%2FlZpmD7L5CPpEF4rkdMJmNJF%2F3W9PKv8DCBEQABoMNjM3NDIzMTgzODA1Igwa0%2BAAnAlo2VA9Fmsq3AORCh5h0g8xFDONkHvODOSfUBBHK8Bc3k7nlUJgGKFsrVwYn7CKcoqR572MvzMXgH3mAFeMvLzP37Gjq4RXPAPAGw07JY%2BecQXuZRKuik%2F%2BAbeeBdpkCVzcLyy6o6BMvkT1DTxyveumM4R4j38AIIUEHZUwjPbKQ3N4NPBL0COaUoZLKn8nk7kie6eJxsjkZ94y86X50srtkLNdIud%2BHa93Q3CmQeo3dG2q%2FUxVhRDlvqfzztrsaYxIokqGwrbzQUAepdryBv22lOLbz2WrScSZ23az8SQaM4Rje%2Bkpwg2DMHVDWlh%2BdTAw6%2BtnOIqwUMaat8uzkMfnh0dps1TJ%2FQrJ24uVK5Jp7gEkBAXTIjvYKIr1bIMhicxPZiW8w7WM16baEprVmYo7GCaKZIh%2FcBeyg7HjSe615vH4VjUkyVPq2f07lesFPcQ5%2FaUDvmmW4ee980MRt7qIMkiaVE3xVOAPTIXGWiOlr%2BbMDECG9z05%2FnQCcNmKZB75D4O2Ogon7ecdZsDOfoZGbMM68xl%2BeFk5umYbv%2Bsbr8H5RL8xzfbj4ITpBlph9FHuCFUl1Iie0HAt7LSpkfScrjL%2BOzul09m%2BsEJRKA8spwW8nxsMf1ceEFMdxDRcTIHC9M68MTCZlKXOBjqkAa0pf5IvEuG5HufiXLbvlCLLaG8kdvBpbdnXSxiFYL9jtyawLBF3szOjRdlXRVWjA1TQt74SdqN7D0fC%2BRHADdtGd0OTx9o7DBv5X%2BFdQx4xnrj4Uv8vIcqC3szSmenEPwjGFBMwX3QokF4KZ50R2KKn8MAEkNpFa2Vhx%2FZJEo5l8lK%2F%2FMF0y7UwfkmuoYJoWZuGrUsYVMYfTfeM%2BMckOipbWfGA&X-Amz-Signature=beba0226739db902384202d75d3278de25dd8e707c61b123b7cfe15d8cbdcacf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<br/>

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/800f330d-42f8-47ad-8a9f-47c7834a4d77/d1e40866-6d78-4e38-97cf-656a70a7897f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WDPY5HJX%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T163518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJIMEYCIQCc%2B5oHLVv8Y0HAsTZ%2BPzw88BeQq6RpoX%2Fri0kuzGTOBAIhAPMeCHuc7qKAGIA%2FlZpmD7L5CPpEF4rkdMJmNJF%2F3W9PKv8DCBEQABoMNjM3NDIzMTgzODA1Igwa0%2BAAnAlo2VA9Fmsq3AORCh5h0g8xFDONkHvODOSfUBBHK8Bc3k7nlUJgGKFsrVwYn7CKcoqR572MvzMXgH3mAFeMvLzP37Gjq4RXPAPAGw07JY%2BecQXuZRKuik%2F%2BAbeeBdpkCVzcLyy6o6BMvkT1DTxyveumM4R4j38AIIUEHZUwjPbKQ3N4NPBL0COaUoZLKn8nk7kie6eJxsjkZ94y86X50srtkLNdIud%2BHa93Q3CmQeo3dG2q%2FUxVhRDlvqfzztrsaYxIokqGwrbzQUAepdryBv22lOLbz2WrScSZ23az8SQaM4Rje%2Bkpwg2DMHVDWlh%2BdTAw6%2BtnOIqwUMaat8uzkMfnh0dps1TJ%2FQrJ24uVK5Jp7gEkBAXTIjvYKIr1bIMhicxPZiW8w7WM16baEprVmYo7GCaKZIh%2FcBeyg7HjSe615vH4VjUkyVPq2f07lesFPcQ5%2FaUDvmmW4ee980MRt7qIMkiaVE3xVOAPTIXGWiOlr%2BbMDECG9z05%2FnQCcNmKZB75D4O2Ogon7ecdZsDOfoZGbMM68xl%2BeFk5umYbv%2Bsbr8H5RL8xzfbj4ITpBlph9FHuCFUl1Iie0HAt7LSpkfScrjL%2BOzul09m%2BsEJRKA8spwW8nxsMf1ceEFMdxDRcTIHC9M68MTCZlKXOBjqkAa0pf5IvEuG5HufiXLbvlCLLaG8kdvBpbdnXSxiFYL9jtyawLBF3szOjRdlXRVWjA1TQt74SdqN7D0fC%2BRHADdtGd0OTx9o7DBv5X%2BFdQx4xnrj4Uv8vIcqC3szSmenEPwjGFBMwX3QokF4KZ50R2KKn8MAEkNpFa2Vhx%2FZJEo5l8lK%2F%2FMF0y7UwfkmuoYJoWZuGrUsYVMYfTfeM%2BMckOipbWfGA&X-Amz-Signature=ca365af65011320a1dce8034f1b91e273e6285e9b7edcf65ca656430bd8d6ed5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

