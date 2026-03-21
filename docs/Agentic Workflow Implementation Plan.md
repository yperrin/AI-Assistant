You are an architect specializing in creating AI driven workflows.
I am trying to have a project where multiple agents can talk to one another, argue with each other and come up with conclusions.
I have been using n8n up until now to create agentic workflows.
I am learning how to use LangGraph because it was advertised as a better solution for an indeterministic agent driven workflow but it seems that all it is is a shared state with conditional looping. This can easily be done in n8n.
I am wondering whether I am missing the point because I am still learning LangGraph.
Is my understanding correct? Am I missing aspects of LangGraph I should be aware of which  would be better suited for my scenario.
List the features LangGraph may bring to my use case and for each one how they would be implemented in LangGraph.
Feel free to include code sample when appropriate.



# **Hierarchical Agentic Orchestration in LangGraph: A Comprehensive Technical Blueprint for Multi-Agent Coordination and Secure Execution**

The shift from monolithic large language model interactions to structured multi-agent systems represents the most significant advancement in computational linguistics and artificial intelligence engineering since the inception of transformers. As the scale and complexity of requested solutions expand beyond the cognitive limits of a single-turn prompt, the necessity for modular, specialized agents that can collaborate, debate, and execute actions becomes paramount.1 This report provides an exhaustive implementation plan for a hierarchical multi-agent framework built upon LangGraph, a low-level orchestration runtime designed to manage stateful, cyclic workflows with precision and durability.3

The architecture described herein is predicated on the coordination of four distinct functional units: a Planner (Supervisor) that manages task decomposition and routing; a Researcher that utilizes recursive, tree-like exploration of the information landscape; a Critic that employs Multi-Agent Personality Shaping (MAPS) to ensure logical rigor; and an Implementer that leverages specialized coding models within secure execution sandboxes.5 By structuring these agents within a graph-based state machine, developers can achieve a level of reliability and traceability that is unattainable in traditional linear chains.3

## **Theoretical Foundation of Graph-Based State Management**

At the core of any sophisticated LangGraph implementation lies the definition of state. In a multi-agent environment, state acts as the "shared scratchpad" or universal whiteboard where agents read instructions, write findings, and record transitions.10 LangGraph utilizes a centralized state object, typically defined via Python’s TypedDict or Pydantic models, which is passed between nodes representing discrete computational steps.3

### **Reducer Logic and State Convergence**

In a system where multiple agents may operate concurrently—such as the Researcher fanning out parallel queries—the mechanism by which state updates are merged is critical.10 LangGraph employs "reducers," which are functions that dictate how new data is integrated into the existing state. For a hierarchical system, the most common reducer is operator.add, applied to a list of messages. This ensures that the conversation history is preserved as an immutable chronological log, preventing the silent data loss that occurs in standard dictionary overrides.10

| State Channel | Data Type | Reducer Function | Architectural Purpose |
| :---- | :---- | :---- | :---- |
| messages | Annotated, operator.add\] | operator.add | Accumulates dialogue and tool results for context retention.10 |
| next\_agent | str | None (Replace) | Stores the Supervisor's routing decision for the next super-step.15 |
| research\_tree | Dict\[str, List\[str\]\] | dict.update | Organizes recursive findings by depth and branch.17 |
| critique\_log | List\] | operator.add | Tracks personality-shaped scoring from multiple critic personas.7 |
| execution\_output | Dict\[str, Any\] | dict.update | Captures artifacts and logs from the sandboxed code environment.8 |

This explicit state schema facilitates high-level features such as persistence and time travel. By integrating a checkpointer—such as a SQLite or PostgreSQL database—the system can save snapshots of the state after every node execution.10 This allows the workflow to be interrupted for human approval or resumed after a system failure, a necessity for long-running research or complex coding tasks.4

## **The Planner: Hierarchical Supervision and Orchestration**

The Planner, or Supervisor, serves as the orchestrator of the entire system. Its primary responsibility is the decomposition of high-level user goals into granular, actionable sub-tasks.5 Unlike a simple router, the Supervisor maintains an awareness of the overall project lifecycle, deciding when a task requires external data (Researcher), logical verification (Critic), or technical implementation (Implementer).1

### **Task Decomposition and Routing Mechanisms**

The Supervisor is typically implemented as a specialized LLM node configured with a comprehensive system prompt and access to handoff tools.16 This agent analyzes the initial input and determines the most efficient path through the graph. For instance, if a user requests a financial analysis of a specific sector, the Planner identifies that it must first invoke the Researcher to gather data, then the Critic to debate the findings, and finally the Implementer to generate charts.5

A pivotal advancement in LangGraph's architecture is the Command object, which replaces traditional conditional edges in complex hierarchies.28 When an agent completes its sub-task, it returns a Command that specifies the state update and the next destination node. This allows for atomic transitions that maintain message history integrity, preventing "dangling tool calls" that occur when an assistant's request is not properly paired with a response before moving to a new agent.28

### **Implementation Blueprint for the Supervisor Node**

Python

from typing import Annotated, Literal  
from langchain\_openai import ChatOpenAI  
from langgraph.graph import StateGraph, START, END  
from langgraph.types import Command  
from langchain\_core.messages import HumanMessage, SystemMessage

def planner\_node(state: AgentState):  
    """  
    Acts as the central supervisor for task allocation.  
    Determines if the current goal requires research, critique, or code.  
    """  
    llm \= ChatOpenAI(model="gpt-4o", temperature=0)  
      
    \# System prompt defines the roles of the specialized workers  
    system\_prompt \= (  
        "You are a master planner managing three specialists: Researcher, Critic, and Implementer. "  
        "Analyze the user query and delegate work. "  
        "Researcher: Gathers data from the web. "  
        "Critic: Reviews findings and debates ideas using MAPS. "  
        "Implementer: Writes and executes code in a sandbox. "  
        "When the solution is complete, respond with the FINAL ANSWER."  
    )  
      
    messages \= \+ state\["messages"\]  
    response \= llm.invoke(messages)  
      
    \# Logic to parse routing from LLM response or structured tool call  
    target \= determine\_next\_agent(response) \# custom logic to select node  
      
    return Command(  
        update={"messages": \[response\]},  
        goto=target  
    )

By centralizing the control logic within the Planner, the system avoids the "mega-prompt" problem, where a single agent is overwhelmed by too many tools and instructions. Instead, each specialist receives only the context relevant to its domain, improving the accuracy of tool selection and the quality of the generated output.2

## **The Researcher: Recursive Tree-Like Exploration Patterns**

Effective research in the AI era requires more than a single search query. It demands a systematic, iterative exploration of the digital landscape.6 The Researcher agent implemented here draws inspiration from the "GPT Researcher" methodology, employing a tree-like exploration pattern where initial findings serve as the foundation for deeper, more specific inquiries.17

### **Breadth and Depth Metrics in Information Retrieval**

The recursive nature of the Researcher is governed by two core parameters: breadth and depth. Breadth determines how many parallel search paths the agent initiates at each level of the tree, while depth dictates how many sequential layers of investigation are performed.17

The total search complexity can be modeled by the summation of queries at each level ![][image1]:

![][image2]  
For an exhaustive research task, a configuration of breadth=4 and depth=2 results in 20 distinct search operations, ensuring that the agent investigates not only the primary topic but also the hidden connections and sub-topics revealed in the first wave of search results.17

| Configuration | Breadth | Depth | Use Case |
| :---- | :---- | :---- | :---- |
| Quick Overview | 5 | 1 | Fast, broad coverage of a well-known topic.18 |
| Balanced Research | 4 | 2 | Recommended for most professional inquiries.17 |
| Deep Dive | 6 | 3 | Thorough investigation of niche or complex subjects.18 |
| Exhaustive Scan | 8 | 4 | Maximum coverage for high-stakes analysis.18 |

### **Implementing Recursive Subgraphs for Deep Research**

In LangGraph, this iterative process is best managed through a subgraph. This keeps the internal research "loops" isolated from the supervisor's top-level state, preventing the primary conversation history from becoming bloated with raw web snippets.33

Python

\# Researcher Subgraph Node Functions  
def query\_generator\_node(state: ResearchState):  
    """Generates B unique queries based on the current goal and past learnings."""  
    \# LLM creates search terms  
    pass

def search\_executor\_node(state: ResearchState):  
    """Executes searches using Tavily or DuckDuckGo API in parallel."""  
    \# Integrate TavilySearchResults for structured data  
    pass

def insight\_extractor\_node(state: ResearchState):  
    """Analyzes search results to extract key facts and identify knowledge gaps."""  
    \# Updates the 'learnings' list in state  
    pass

def research\_routing(state: ResearchState):  
    """Conditional edge logic for depth termination."""  
    if state\["current\_depth"\] \< state\["max\_depth"\]:  
        return "query\_generator"  
    return END

This recursive structure allows the agent to behave autonomously within its domain. If the initial search for "quantum computing breakthroughs" yields information about "topological qubits," the agent automatically adjusts its next-level queries to explore that specific sub-field without needing further intervention from the Planner.6

## **The Critic: Multi-Agent Personality Shaping (MAPS) and Reflection**

The Critic agent provides the "System 2" cognitive layer of the system. Its role is to scrutinize findings, challenge assumptions, and debate potential solutions to ensure they are logically consistent and free from hallucinations.12 To achieve a superior level of reasoning, this implementation utilizes the Multi-Agent Personality Shaping (MAPS) framework, which assigns distinct psychological and domain-specific personas to different instances of the critic.7

### **The Big Five Framework in Agentic Reasoning**

Inspired by the Big Five personality theory, the MAPS framework shapes the reasoning behavior of agents through personality vectors. By assigning traits like "Neuroticism" to a Critic or "Openness" to an Interpreter, the system induces heterogeneous collaboration that mitigates the behavioral homogeneity often found in single-model systems.7

1. **The Optimist (Openness/Extraversion):** Focuses on the potential advantages, future-forward applications, and creative syntheses of the research findings.7  
2. **The Pessimist (Neuroticism/Conscientiousness):** Acts as the "Skeptic," identifying risks, potential biases, logical gaps, and scenarios where the proposed solution might fail.7  
3. **The Scholar (Agreeableness/Conscientiousness):** Ensures factual grounding, citation accuracy, and adherence to established domain standards.7

### **The Reflexion Loop and Iterative Improvement**

The interaction between the Researcher and the Critic follows a cyclical "Reflexion" pattern.19 The Critic agents review the Researcher's draft and provide structured feedback. The Researcher then incorporates this feedback to produce a revised version. This loop continues for a fixed number of trials or until a quality threshold is met.7

| Phase | Agent Role | Output |
| :---- | :---- | :---- |
| Action | Researcher | Initial research report or draft solution.35 |
| Evaluation | Critic Personas | Multidimensional scores (Accuracy, Depth, Logic).7 |
| Reflection | Reflection Model | Verbal feedback summarizing errors and revision steps.35 |
| Revision | Researcher | Updated output incorporating the Critic's suggestions.35 |

This process ensures that the final output is not just a first-pass generation but a refined, peer-reviewed document. The use of multiple personas prevents the system from converging on a biased or narrow conclusion, as the Optimist and Pessimist are forced to reconcile their perspectives through the Supervisor.5

## **The Implementer: Secure Execution and Specialized Coding**

The final stage of the workflow involves the technical implementation of the solution. The Implementer agent is tasked with writing, testing, and running code.8 To perform this reliably, the system must bridge the gap between abstract natural language reasoning and concrete code execution within a secure environment.8

### **Qwen 2.5-Coder: Optimization for Software Engineering**

While general models are capable of coding, specialized models like Qwen 2.5-Coder are best suited for the Implementer role. These models are trained on trillions of tokens of source code and text-code grounding, enabling superior code reasoning and fixing capabilities.41 Qwen 2.5-Coder-32B, in particular, has demonstrated state-of-the-art performance in real-world application scenarios, matching GPT-4o in coding benchmarks while maintaining a 128K context window.41

A key feature of Qwen 2.5-Coder is its native support for tool calling. When tasked with a data visualization, the model does not merely suggest Python code; it outputs the code in a structured format that the LangGraph runtime can directly execute in the sandbox.42

### **Sandboxed Execution via E2B Code Interpreter**

Executing AI-generated code on a local machine is a significant security risk. The Implementer utilizes the E2B Code Interpreter SDK to spawn secure cloud sandboxes powered by Firecracker micro-VMs.8 This environment provides a running Jupyter server that the LLM can interact with, allowing it to:

* Run Python code and capture stdout/stderr.8  
* Generate and download artifacts like charts or CSV files.20  
* Install necessary Python or system packages dynamically during runtime.20  
* Upload user data (e.g., a CSV of netflix movies) for analysis.20

Python

from e2b\_code\_interpreter import CodeInterpreter

def implementer\_node(state: AgentState):  
    """  
    Writes and runs Python code in a secure E2B sandbox.  
    Uses Qwen 2.5-Coder for high-precision code generation.  
    """  
    \# 1\. Model generates the code based on Critic's refined plan  
    code \= qwen\_model.generate\_code(state\["messages"\])  
      
    \# 2\. Execute in secure cloud sandbox  
    with CodeInterpreter() as sandbox:  
        execution \= sandbox.notebook.exec\_cell(code)  
          
        \# 3\. Capture results and errors  
        if execution.error:  
            \# Route back for self-fixing if execution fails  
            return {"messages": \[HumanMessage(content=f"Code Error: {execution.error.value}")\]}  
          
        \# 4\. Save artifacts (e.g., charts) to state  
        chart\_data \= execution.results.png if execution.results else None  
          
    return {"execution\_output": {"logs": execution.logs.stdout, "chart": chart\_data}}

The combination of a specialized coder and a micro-VM sandbox ensures that the Implementer is both highly capable and safe. If the generated code fails to run, the system enters a self-correction loop where the error log is passed back to the coder for a revision—a pattern essential for complex data analysis or software development tasks.26

## **Production Engineering: Persistence, Observability, and Limits**

Moving from a prototype to a production-grade multi-agent system requires rigorous engineering around state persistence and system observability.4 LangGraph provides the infrastructure to manage these non-functional requirements without complicating the core agent logic.3

### **Stateful Persistence and Checkpointing**

In production, agents often engage in multi-turn conversations that span hours or days. Checkpointing allows the graph to persist its state in a database, associated with a unique thread\_id.10 This is crucial for:

* **Error Recovery:** If a node fails due to an API timeout, the system can resume from the last successful checkpoint rather than restarting the entire research tree.10  
* **Human-in-the-Loop:** High-stakes tasks, such as the Implementer running code that modifies a database, can be configured with an interrupt. The state is saved, the execution pauses, and a human operator can inspect and approve the action before it proceeds.4

| Component | Implementation Option | Recommended Context |
| :---- | :---- | :---- |
| Ephemeral Memory | MemorySaver | Local development and unit testing.15 |
| Persistent DB | SqliteSaver / PostgresSaver | Production environments requiring durability.10 |
| Long-term Store | InMemoryStore / Vector DB | Storing embeddings or agent memories across threads.14 |

### **Recursion Limits and Safety Guards**

To prevent infinite loops—especially in recursive research or critic-writer cycles—it is mandatory to configure recursion limits. LangGraph natively supports a recursion\_limit parameter in the run configuration.49 If the graph exceeds a set number of "super-steps" (e.g., 50), it raises a GraphRecursionError, allowing the system to fail gracefully and return the best available answer rather than exhausting API budgets.49

| Guardrail | Mechanism | Impact |
| :---- | :---- | :---- |
| recursion\_limit | Configuration parameter | Prevents infinite agent cycles.49 |
| max\_tokens | Model parameter | Controls latency and cost per turn.49 |
| tool\_usage\_limit | Custom state tracking | Enforces rate limits on expensive tools like search or sandboxes.51 |

## **Strategic Synthesis: Navigating the Multi-Agent Landscape**

The implementation plan detailed in this blueprint provides a structured path for scaling AI capabilities. The synergy between the Planner’s orchestration, the Researcher’s depth, the Critic’s logic, and the Implementer’s execution creates a system that is greater than the sum of its parts.2

By adopting a hierarchical architecture, developers can ensure that each agent remains highly focused on its domain of expertise. The use of subgraphs facilitates modular development, allowing different teams to work on the Researcher or Implementer independently.33 Furthermore, the integration of 2025-era features like the Command API and specialized models like Qwen 2.5-Coder ensures that the system is built on the current state-of-the-art, offering maximum performance and security.28

Ultimately, the success of such a system depends on the clarity of the state schema and the precision of the agent prompts. As AI systems evolve from simple assistants to autonomous problem-solvers, the ability to coordinate these "independent actors" through graph-based workflows will remain the cornerstone of professional AI engineering.2

#### **Works cited**

1. LangGraph Multi Agent Workflow Tutorial \- Kinde, accessed February 23, 2026, [https://kinde.com/learn/ai-for-software-engineering/ai-agents/langgraph-multiagent-workflow-tutorial/](https://kinde.com/learn/ai-for-software-engineering/ai-agents/langgraph-multiagent-workflow-tutorial/)  
2. LangGraph: Multi-Agent Workflows \- LangChain Blog, accessed February 23, 2026, [https://blog.langchain.com/langgraph-multi-agent-workflows/](https://blog.langchain.com/langgraph-multi-agent-workflows/)  
3. Building Multi Agent Systems using LangGraph | by Sathwick \- Medium, accessed February 23, 2026, [https://medium.com/@sathwickreddy/building-multi-agent-systems-using-langgraph-2e6055066336](https://medium.com/@sathwickreddy/building-multi-agent-systems-using-langgraph-2e6055066336)  
4. LangGraph overview \- Docs by LangChain, accessed February 23, 2026, [https://docs.langchain.com/oss/python/langgraph/overview](https://docs.langchain.com/oss/python/langgraph/overview)  
5. Building a Supervisor Multi-Agent System with LangGraph Hierarchical Intelligence in Action | by Mani | Medium, accessed February 23, 2026, [https://medium.com/@mnai0377/building-a-supervisor-multi-agent-system-with-langgraph-hierarchical-intelligence-in-action-3e9765af181c](https://medium.com/@mnai0377/building-a-supervisor-multi-agent-system-with-langgraph-hierarchical-intelligence-in-action-3e9765af181c)  
6. Blog | GPT Researcher, accessed February 23, 2026, [https://docs.gptr.dev/blog](https://docs.gptr.dev/blog)  
7. MAPS: Multi-Agent Personality Shaping for Collaborative Reasoning \- arXiv, accessed February 23, 2026, [https://arxiv.org/html/2503.16905v2](https://arxiv.org/html/2503.16905v2)  
8. e2b-cookbook/examples/langgraph-python ... \- GitHub, accessed February 23, 2026, [https://github.com/e2b-dev/e2b-cookbook/blob/main/examples/langgraph-python/langgraph\_code\_interpreter.ipynb](https://github.com/e2b-dev/e2b-cookbook/blob/main/examples/langgraph-python/langgraph_code_interpreter.ipynb)  
9. LangGraph 101: Let's Build A Deep Research Agent | Towards Data Science, accessed February 23, 2026, [https://towardsdatascience.com/langgraph-101-lets-build-a-deep-research-agent/](https://towardsdatascience.com/langgraph-101-lets-build-a-deep-research-agent/)  
10. Part 1: How LangGraph Manages State for Multi-Agent Workflows (Best Practices) \- Medium, accessed February 23, 2026, [https://medium.com/@bharatraj1918/langgraph-state-management-part-1-how-langgraph-manages-state-for-multi-agent-workflows-da64d352c43b](https://medium.com/@bharatraj1918/langgraph-state-management-part-1-how-langgraph-manages-state-for-multi-agent-workflows-da64d352c43b)  
11. AI Agents XII — LangGraph graph-based framework \- Artificial Intelligence in Plain English, accessed February 23, 2026, [https://ai.plainenglish.io/ai-agents-xii-langgraph-graph-based-framework-b7b74e1fa5df](https://ai.plainenglish.io/ai-agents-xii-langgraph-graph-based-framework-b7b74e1fa5df)  
12. Multiple AI Agents: Creating Multi-Agent Workflows Using LangGraph and LangChain, accessed February 23, 2026, [https://vijaykumarkartha.medium.com/multiple-ai-agents-creating-multi-agent-workflows-using-langgraph-and-langchain-0587406ec4e6](https://vijaykumarkartha.medium.com/multiple-ai-agents-creating-multi-agent-workflows-using-langgraph-and-langchain-0587406ec4e6)  
13. Building Multi-Agent Systems with LangGraph: A Step-by-Step Guide | by Sushmita Nandi, accessed February 23, 2026, [https://medium.com/@sushmita2310/building-multi-agent-systems-with-langgraph-a-step-by-step-guide-d14088e90f72](https://medium.com/@sushmita2310/building-multi-agent-systems-with-langgraph-a-step-by-step-guide-d14088e90f72)  
14. Mastering LangGraph State Management in 2025 \- Sparkco, accessed February 23, 2026, [https://sparkco.ai/blog/mastering-langgraph-state-management-in-2025](https://sparkco.ai/blog/mastering-langgraph-state-management-in-2025)  
15. langchain/langgraph-supervisor, accessed February 23, 2026, [https://reference.langchain.com/javascript/langchain-langgraph-supervisor](https://reference.langchain.com/javascript/langchain-langgraph-supervisor)  
16. Building Multi-Agent Systems with LangGraph-Supervisor \- DEV Community, accessed February 23, 2026, [https://dev.to/sreeni5018/building-multi-agent-systems-with-langgraph-supervisor-138i](https://dev.to/sreeni5018/building-multi-agent-systems-with-langgraph-supervisor-138i)  
17. Deep Research NEW | GPT Researcher, accessed February 23, 2026, [https://docs.gptr.dev/docs/gpt-researcher/gptr/deep\_research](https://docs.gptr.dev/docs/gpt-researcher/gptr/deep_research)  
18. piy-us/deep\_research\_langgraph: This is a LangGraph based Deep Research Agent Workflow. \- GitHub, accessed February 23, 2026, [https://github.com/piy-us/deep\_research\_langgraph](https://github.com/piy-us/deep_research_langgraph)  
19. Reflection Agents \- LangChain Blog, accessed February 23, 2026, [https://blog.langchain.com/reflection-agents/](https://blog.langchain.com/reflection-agents/)  
20. E2b data analysis integration \- Docs by LangChain, accessed February 23, 2026, [https://docs.langchain.com/oss/python/integrations/tools/e2b\_data\_analysis](https://docs.langchain.com/oss/python/integrations/tools/e2b_data_analysis)  
21. Build a Multi-Agent System with LangGraph and Mistral on AWS | Artificial Intelligence, accessed February 23, 2026, [https://aws.amazon.com/blogs/machine-learning/build-a-multi-agent-system-with-langgraph-and-mistral-on-aws/](https://aws.amazon.com/blogs/machine-learning/build-a-multi-agent-system-with-langgraph-and-mistral-on-aws/)  
22. LangGraph Tutorial for Beginners \- Analytics Vidhya, accessed February 23, 2026, [https://www.analyticsvidhya.com/blog/2025/05/langgraph-tutorial-for-beginners/](https://www.analyticsvidhya.com/blog/2025/05/langgraph-tutorial-for-beginners/)  
23. cgoncalves94/multi\_agent\_system: Multi-Agent LangGraph System \- GitHub, accessed February 23, 2026, [https://github.com/cgoncalves94/multi\_agent\_system](https://github.com/cgoncalves94/multi_agent_system)  
24. Build a personal assistant with subagents \- Docs by LangChain, accessed February 23, 2026, [https://docs.langchain.com/oss/python/langchain/multi-agent/subagents-personal-assistant](https://docs.langchain.com/oss/python/langchain/multi-agent/subagents-personal-assistant)  
25. Building Multi-Agents Supervisor System from Scratch with LangGraph & Langsmith | by Anurag Mishra | Medium, accessed February 23, 2026, [https://medium.com/@anuragmishra\_27746/building-multi-agents-supervisor-system-from-scratch-with-langgraph-langsmith-b602e8c2c95d](https://medium.com/@anuragmishra_27746/building-multi-agents-supervisor-system-from-scratch-with-langgraph-langsmith-b602e8c2c95d)  
26. Understanding the LangGraph Multi-Agent Supervisor | by akanshak \- Medium, accessed February 23, 2026, [https://medium.com/@akanshak/understanding-the-langgraph-multi-agent-supervisor-00fa1be4341b](https://medium.com/@akanshak/understanding-the-langgraph-multi-agent-supervisor-00fa1be4341b)  
27. LangGraph Multi-Agent Supervisor, accessed February 23, 2026, [https://reference.langchain.com/python/langgraph-supervisor](https://reference.langchain.com/python/langgraph-supervisor)  
28. How to implement handoffs between agents \- cloudns.asia, accessed February 23, 2026, [https://nightcat.cloudns.asia:9981/sitedoc/langgraph/v0.4.3/how-tos/agent-handoffs/](https://nightcat.cloudns.asia:9981/sitedoc/langgraph/v0.4.3/how-tos/agent-handoffs/)  
29. Transactional Cross-Graph Handoff · Issue \#6455 · langchain-ai/langgraph \- GitHub, accessed February 23, 2026, [https://github.com/langchain-ai/langgraph/issues/6455](https://github.com/langchain-ai/langgraph/issues/6455)  
30. How Agent Handoffs Work in Multi-Agent Systems | Towards Data Science, accessed February 23, 2026, [https://towardsdatascience.com/how-agent-handoffs-work-in-multi-agent-systems/](https://towardsdatascience.com/how-agent-handoffs-work-in-multi-agent-systems/)  
31. Building Multi-Agent Applications with Deep Agents \- LangChain Blog, accessed February 23, 2026, [https://blog.langchain.com/building-multi-agent-applications-with-deep-agents/](https://blog.langchain.com/building-multi-agent-applications-with-deep-agents/)  
32. assafelovic/gpt-researcher: An autonomous agent that conducts deep research on any data using any LLM providers. \- GitHub, accessed February 23, 2026, [https://github.com/assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher)  
33. Subgraphs \- Docs by LangChain, accessed February 23, 2026, [https://docs.langchain.com/oss/python/langgraph/use-subgraphs](https://docs.langchain.com/oss/python/langgraph/use-subgraphs)  
34. LangGraph Subgraphs: A Guide to Modular AI Agents Development \- DEV Community, accessed February 23, 2026, [https://dev.to/sreeni5018/langgraph-subgraphs-a-guide-to-modular-ai-agents-development-31ob](https://dev.to/sreeni5018/langgraph-subgraphs-a-guide-to-modular-ai-agents-development-31ob)  
35. Built with LangGraph\! \#29: Reflection & Reflexion | by Okan Yenigün \- Medium, accessed February 23, 2026, [https://medium.com/@okanyenigun/built-with-langgraph-29-reflection-reflexion-10cc1cf96f35](https://medium.com/@okanyenigun/built-with-langgraph-29-reflection-reflexion-10cc1cf96f35)  
36. Building Multi-Agent Systems with LangGraph | by Clearwater Analytics Engineering, accessed February 23, 2026, [https://medium.com/cwan-engineering/building-multi-agent-systems-with-langgraph-04f90f312b8e](https://medium.com/cwan-engineering/building-multi-agent-systems-with-langgraph-04f90f312b8e)  
37. Reflexion Agent Pattern — Agent Patterns 0.2.0 documentation \- Read the Docs, accessed February 23, 2026, [https://agent-patterns.readthedocs.io/en/stable/patterns/reflexion.html](https://agent-patterns.readthedocs.io/en/stable/patterns/reflexion.html)  
38. Design of a Self-Improving Gödel Agent with CrewAI and LangGraph \- GitHub Gist, accessed February 23, 2026, [https://gist.github.com/ruvnet/15c6ef556be49e173ab0ecd6d252a7b9](https://gist.github.com/ruvnet/15c6ef556be49e173ab0ecd6d252a7b9)  
39. E2B: Integrating Language Models with Python Execution for Advanced Analytics, accessed February 23, 2026, [https://www.buildfastwithai.com/blogs/integrating-execution-environments-with-language-models-using-e2b-and-langchain](https://www.buildfastwithai.com/blogs/integrating-execution-environments-with-language-models-using-e2b-and-langchain)  
40. e2b-dev/e2b-cookbook: Examples of using E2B \- GitHub, accessed February 23, 2026, [https://github.com/e2b-dev/e2b-cookbook](https://github.com/e2b-dev/e2b-cookbook)  
41. Qwen/Qwen2.5-Coder-7B-Instruct \- Hugging Face, accessed February 23, 2026, [https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct)  
42. Function Calling with Small Language Models | Microsoft Community Hub, accessed February 23, 2026, [https://techcommunity.microsoft.com/blog/educatordeveloperblog/function-calling-with-small-language-models/4472720](https://techcommunity.microsoft.com/blog/educatordeveloperblog/function-calling-with-small-language-models/4472720)  
43. Qwen 2.5 Coder: A Guide With Examples \- DataCamp, accessed February 23, 2026, [https://www.datacamp.com/tutorial/qwen-coder-2-5](https://www.datacamp.com/tutorial/qwen-coder-2-5)  
44. ChatQwen integration \- Docs by LangChain, accessed February 23, 2026, [https://docs.langchain.com/oss/python/integrations/chat/qwen](https://docs.langchain.com/oss/python/integrations/chat/qwen)  
45. Function Calling \- Qwen, accessed February 23, 2026, [https://qwen.readthedocs.io/en/v2.0/framework/function\_call.html](https://qwen.readthedocs.io/en/v2.0/framework/function_call.html)  
46. How to Continuously Improve Your LangGraph Multi-Agent System \- Maxim AI, accessed February 23, 2026, [https://www.getmaxim.ai/articles/how-to-continuously-improve-your-langgraph-multi-agent-system/](https://www.getmaxim.ai/articles/how-to-continuously-improve-your-langgraph-multi-agent-system/)  
47. LangGraph Multi-Agent Orchestration: Complete Framework Guide \+ Architecture Analysis 2025 \- Latenode Blog, accessed February 23, 2026, [https://latenode.com/blog/ai-frameworks-technical-infrastructure/langgraph-multi-agent-orchestration/langgraph-multi-agent-orchestration-complete-framework-guide-architecture-analysis-2025](https://latenode.com/blog/ai-frameworks-technical-infrastructure/langgraph-multi-agent-orchestration/langgraph-multi-agent-orchestration-complete-framework-guide-architecture-analysis-2025)  
48. langchain-ai/langgraph-supervisor-py \- GitHub, accessed February 23, 2026, [https://github.com/langchain-ai/langgraph-supervisor-py](https://github.com/langchain-ai/langgraph-supervisor-py)  
49. How to cap tool and sub-agent calls in DeepAgents? \- LangChain Forum, accessed February 23, 2026, [https://forum.langchain.com/t/how-to-cap-tool-and-sub-agent-calls-in-deepagents/1653](https://forum.langchain.com/t/how-to-cap-tool-and-sub-agent-calls-in-deepagents/1653)  
50. Qwen2.5 32b will start to put the tool calls in the content instead of the tool\_calls : r/ollama, accessed February 23, 2026, [https://www.reddit.com/r/ollama/comments/1j30893/qwen25\_32b\_will\_start\_to\_put\_the\_tool\_calls\_in/](https://www.reddit.com/r/ollama/comments/1j30893/qwen25_32b_will_start_to_put_the_tool_calls_in/)  
51. LangGraph Tutorial: Enhanced State Management for Multi-Tool Agents \- Unit 2.2 Exercise 1 \- AI Product Engineer, accessed February 23, 2026, [https://aiproduct.engineer/tutorials/langgraph-tutorial-enhanced-state-management-for-multi-tool-agents-unit-22-exercise-1](https://aiproduct.engineer/tutorials/langgraph-tutorial-enhanced-state-management-for-multi-tool-agents-unit-22-exercise-1)

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA0AAAAYCAYAAAAh8HdUAAAAtUlEQVR4XmNgGP7AEYhfA/F/JPwLiHcDsTCSOqxgDhD/A2IPdAlcQBCITwPxAyCWRpXCDTSB+C0QrwFiFjQ5nCCaAeKXcnQJfGASEP8GYht0CVwA5p+7QCyOJocTEPIPGxCzogvC/FOELgEEjEDcBMQ66BKg+MHlHxUgngvEnMiC+OIH5KRZDBCXoABjIP7KgOkfSQaIhkdArAgTdAHiZwyItPYXiJ9AMYgNE1/OgD1wRgHtAQAv+ie2Ic8IBwAAAABJRU5ErkJggg==>

[image2]: <data:image/png;base64,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>