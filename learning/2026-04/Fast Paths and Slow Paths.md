---
complexity: Advanced
date: 2026-04-06 07:32:00-04:00
id: 33a9fa3b-8750-8038-9043-e0862c605e8b
processed_by_ai: true
summary: This article argues that scalable autonomous AI systems require a dual-path
  architecture (fast for routine, slow for high-stakes) to move away from synchronous,
  "gatekeeper" style governance. It proposes shifting governance from per-step approval
  to continuous feedback and proportional intervention to ensure safe and efficient
  operation.
title: Fast Paths and Slow Paths
tools_mentioned: []
topics:
- AI Governance
- Autonomous AI Systems
- System Architecture
- Scalability
- Risk Management
- Latency
url: https://www.notion.so/Fast-Paths-and-Slow-Paths-33a9fa3b875080389043e0862c605e8b
---

This article, [Fast Paths and Slow Paths](https://www.oreilly.com/radar) by Varun Raj, argues that the survival of autonomous AI systems at scale depends on moving away from synchronous, "gatekeeper" style governance toward a dual-path architecture.

---

### The Core Challenge: The "Universal Mediation" Trap

Architects often feel that every AI decision must be governed synchronously to be safe. However, the article highlights several reasons why this approach fails in production:

- **Compounding Latency:** Multistep reasoning loops become unusably slow when every step requires an approval check.

- **Structural Fragility:** Control systems become single points of failure; if the "governor" stalls, the entire autonomous agent stops.

- **Scalability Issues:** Coordination overhead grows superlinearly, making the cost of control higher than the value of the autonomy.

- **False Positives:** Rigid, synchronous gates often block benign behaviors, leading teams to bypass controls entirely to maintain functionality.

---

### The Proposed Solution: Fast vs. Slow Paths

The article proposes a model similar to networking (control vs. data planes) where AI execution is split based on risk and reversibility.

### 1. The Fast Path (Autonomy)

Most routine execution should happen here. It operates within "preauthorized envelopes" of behavior.

- **Characteristics:** Includes routine data retrieval, tool calls within scoped permissions, and reversible reasoning steps.

- **Mechanism:** Instead of per-step approval, it relies on prior authorization and continuous, passive observation.

### 2. The Slow Path (Mediation)

Synchronous control is reserved for rare, high-stakes moments.

- **When to use:** For actions with irreversible consequences, crossing trust boundaries (e.g., external user impact), or accessing highly regulated data.

- **Goal:** To intervene only when the stakes change, ensuring the cost of waiting is lower than the potential cost of an error.

---

### Governance as Feedback, Not Approval

The article suggests that for AI to scale, governance must evolve into a **regulatory feedback loop**:

- **Continuous Observation:** Control planes should watch everything but only intervene when thresholds are crossed.

- **Proportional Intervention:** Rather than a hard "stop," the system should adjust conditions—such as narrowing retrieval scope, reducing available tools, or requiring higher confidence thresholds.

- **Outcome-Oriented:** Architects should focus on governing the final results and behavioral trajectories rather than micromanaging every inference step.

> "The future of AI governance is not more gates. It is better control. And control, done right, does not stop systems from acting. It ensures they can keep acting safely."

Would you like me to dive deeper into the [architectural shifts](https://www.oreilly.com/people/varun-raj/) mentioned, such as the use of a "shared context fabric" for agent memory?