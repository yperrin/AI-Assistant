---
complexity: Advanced
date: 2025-11-27 11:59:00-05:00
id: 2b89fa3b-8750-80e2-96f1-d2f321665056
processed_by_ai: true
summary: This document explores strategies for exposing LS&H R&D data to internal
  and external customers, questioning the current MCP (Multi-Cloud Platform) strategy
  and proposing a complex solution involving GraphRAG, vector search, and specialized
  agents. The author concludes that MCP should be a distribution pattern rather than
  a core architectural goal, emphasizing the need to solve data access and understand
  usage patterns first.
title: MCP as data gateway
tools_mentioned:
- Anthropic article
- deltalake
topics:
- Data Exposure
- R&D Data
- Multi-Cloud Platform (MCP) Strategy
- GraphRAG
- Vector Search
- Multi-Agent Systems
- Data Architecture
- Ontologies
- Data Mesh
url: https://www.notion.so/MCP-as-data-gateway-2b89fa3b875080e296f1d2f321665056
---

Researching how to expose our LS&H R&D data to internal and external customers. I am curious about the current MCP strategy and wondering if maybe I am missing something.

Most research I have done seems to indicate MCP is not necessarily bad but there are a lot of caveats, especially for external paying customers.

As per Anthropic article, passing raw data through an MCP server is probably not a great idea because of high token usage, potentially infinite loop and also json is not necessarily the best protocol for transferring a lot of data (which would be required for a deep analysis).

I am trying to solve the issue of we are not quite sure what the users would ask of our data. If we knew for sure, a cube would probably be the best solution (think of it as a fixed database aggregating all of the data into a single space).

The solution seems to be a complex combination of GraphRAG (as research data is inherently highly connected but our current data mesh architecture have the data isolated in separate domains), vector search and also providing specialized agents with different perspective on the data and a coordinator agent in front of this to delegate to the appropriate agents.

This could solve the issue for internal customers, think of the insights our consultancy team could create and share with our customers. 

For this to apply to external customers, we could have an MCP (or more than one) in front of all of that with the addition of a gateway (to make sure the customers have access to the data and have paid for the privilege).

An interesting conclusion for there would be that content teams would be responsible for pushing the data to deltalake (like we do now) but also for providing an agent which would allow accessing the domain data.

I am still amazed how ontologies are really the glue which brings everything together and I think we should be doing more than we are doing now if we are to create a graph of related entities.

I am still aggregating all the information I can to try to form an opinion but it is already clear that providing an MCP for accessing our data is going to be a fairly complex task.

Either way it seems focusing on MCP as the goal may be the wrong approach and it should only come into picture when data access has been solved and usage patterns are understood. MCP is a distribution pattern but not a core architectural need.

It seems to me that a series of agents matching the product focuses (but not necessarily the product) on the Clarivate customer side and a general GraphRAG at the LS&H division level (or maybe more than one) would probably be a good solution to get started with.

I am still not sure how we are able to avoid regulatory concerns with all of that.