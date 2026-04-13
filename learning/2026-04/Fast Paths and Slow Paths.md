---
title: Fast Paths and Slow Paths
id: 33a9fa3b-8750-8038-9043-e0862c605e8b
url: https://www.notion.so/Fast-Paths-and-Slow-Paths-33a9fa3b875080389043e0862c605e8b
---

---

### The Core Challenge: The "Universal Mediation" Trap

- **Compounding Latency:** Multistep reasoning loops become unusably slow when every step requires an approval check.

- **Structural Fragility:** Control systems become single points of failure; if the "governor" stalls, the entire autonomous agent stops.

- **Scalability Issues:** Coordination overhead grows superlinearly, making the cost of control higher than the value of the autonomy.

- **False Positives:** Rigid, synchronous gates often block benign behaviors, leading teams to bypass controls entirely to maintain functionality.

---

### The Proposed Solution: Fast vs. Slow Paths

### 1. The Fast Path (Autonomy)

- **Characteristics:** Includes routine data retrieval, tool calls within scoped permissions, and reversible reasoning steps.

- **Mechanism:** Instead of per-step approval, it relies on prior authorization and continuous, passive observation.

### 2. The Slow Path (Mediation)

- **When to use:** For actions with irreversible consequences, crossing trust boundaries (e.g., external user impact), or accessing highly regulated data.

- **Goal:** To intervene only when the stakes change, ensuring the cost of waiting is lower than the potential cost of an error.

---

### Governance as Feedback, Not Approval

- **Continuous Observation:** Control planes should watch everything but only intervene when thresholds are crossed.

- **Proportional Intervention:** Rather than a hard "stop," the system should adjust conditions—such as narrowing retrieval scope, reducing available tools, or requiring higher confidence thresholds.

- **Outcome-Oriented:** Architects should focus on governing the final results and behavioral trajectories rather than micromanaging every inference step.

> "The future of AI governance is not more gates. It is better control. And control, done right, does not stop systems from acting. It ensures they can keep acting safely."

