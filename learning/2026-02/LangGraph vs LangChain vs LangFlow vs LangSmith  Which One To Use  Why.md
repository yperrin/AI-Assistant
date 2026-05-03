---
complexity: Intermediate
date: 2026-02-17 10:27:00-05:00
id: 30a9fa3b-8750-80b2-b2be-c96d686f8288
processed_by_ai: true
summary: This document explains the differences and use cases for LangChain, LangGraph,
  LangFlow, and LangSmith, which are key frameworks within the LangChain ecosystem
  for building and managing Large Language Model (LLM) applications.
title: LangGraph vs LangChain vs LangFlow vs LangSmith  Which One To Use  Why
tools_mentioned:
- LangChain
- LangGraph
- LangFlow
- LangSmith
- GPT-4
- Llama 3
topics:
- Large Language Models
- LLM Application Development
- LangChain Ecosystem
- Framework Comparison
url: https://www.notion.so/LangGraph-vs-LangChain-vs-LangFlow-vs-LangSmith-Which-One-To-Use-Why-30a9fa3b875080b2b2bec96d686f8288
---

<br/>

Building applications with Large Language Models (LLMs) often involves using a combination of frameworks from the LangChain ecosystem. Here is a breakdown of the differences and use cases for [LangGraph](https://gemini.google.com/glic?hl=en), [LangChain](https://gemini.google.com/glic?hl=en), [LangFlow](https://gemini.google.com/glic?hl=en), and [LangSmith](https://gemini.google.com/glic?hl=en) based on the video:

### **1. LangChain: The Core Framework**

- **What it is:** An open-source framework used to build LLM-powered applications by "chaining" different components together [01:53](https://gemini.google.com/glic?hl=en).

- **Key Features:** Provides abstractions for LLM support (GPT-4, Llama 3), prompt templates, memory for context, and agents that act as reasoning engines [02:16](https://gemini.google.com/glic?hl=en).

- **When to use:** Use this as your foundation to manage API calls, documentation loading, and basic sequential workflows [03:20](https://gemini.google.com/glic?hl=en).

### **2. LangGraph: For Complex Agents**

- **What it is:** Built on top of LangChain, it is designed to manage complex, multi-agent workflows using a graph-based structure [03:42](https://gemini.google.com/glic?hl=en).

- **Key Features:** Uses **Nodes** (actions/tasks), **Edges** (flow of execution), and **State** (shared data structure) [04:21](https://gemini.google.com/glic?hl=en).

- **When to use:** Best for "cyclical" interactions where agents need to talk back and forth or make non-linear decisions [05:14](https://gemini.google.com/glic?hl=en).

### **3. LangFlow: The Visual Prototyper**

- **What it is:** A drag-and-drop UI for LangChain that allows you to build AI workflows without writing code [05:42](https://gemini.google.com/glic?hl=en).

- **Key Features:** Visual interface for experimenting with chains and agents; can be hosted locally or on the cloud [06:21](https://gemini.google.com/glic?hl=en).

- **When to use:** Ideal for rapid prototyping and building MVPs quickly [06:06](https://gemini.google.com/glic?hl=en).

### **4. LangSmith: Monitoring & Evaluation**

- **What it is:** A platform for debugging, testing, and monitoring LLM applications throughout their lifecycle (prototype to production) [07:44](https://gemini.google.com/glic?hl=en).

- **Key Features:** Tracks token usage, costs, error rates, and latency through "traces" [09:05](https://gemini.google.com/glic?hl=en).

- **When to use:** Use this when you need to ensure your application is performing as expected before or after public release [08:02](https://gemini.google.com/glic?hl=en).

### **Quick Comparison Summary**

 | **Tool** | **Primary Purpose** | **Best For** | 
 | ---- | ---- | ---- | 
 | **LangChain** | Development | Building standard LLM chains and apps [01:53](https://gemini.google.com/glic?hl=en). | 
 | **LangGraph** | Orchestration | Complex, multi-agent, cyclical workflows [04:05](https://gemini.google.com/glic?hl=en). | 
 | **LangFlow** | Prototyping | Visual, low-code design and testing [05:58](https://gemini.google.com/glic?hl=en). | 
 | **LangSmith** | Operations | Debugging, monitoring, and cost tracking [07:52](https://gemini.google.com/glic?hl=en). | 

For more details, you can watch the full video: [LangGraph vs LangChain vs LangFlow vs LangSmith](https://gemini.google.com/glic?hl=en).