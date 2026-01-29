
# Enterprise AI Operations Agent  
## An internal AI copilot that removes operational bottlenecks and replaces people-dependent workflows

This system is designed for founders and leadership teams who are scaling AI-powered workflows and need reliability, control, and decision velocity — without adding operational complexity or headcount.

# 🛠️ The Tech Stack

## Orchestration: n8n (Production-grade workflow automation)

## LLM Framework: CrewAI (Multi-agent orchestration)

## Backend: Python 3.12 (Pydantic V2 for strict type safety)

## Infrastructure: AWS ECS Fargate, Secrets Manager, IAM (Least-Privilege)

## Vector Store: PostgreSQL + pgvector for bounded context retrieval

## Observability: Langfuse (Traceability, Latency, and Cost tracking)

# The Business Problem This Solves

As companies scale, operational knowledge fragments across tools, documents, and people.

The result:
- Founders become decision bottlenecks
- Teams rely on tribal knowledge
- AI systems behave unpredictably in production
- Costs, failures, and risks surface too late

Most AI initiatives fail not because models are weak — but because **operations lack control, observability, and decision boundaries**.


## Who This Is For

This system is designed for:

- Founders and executive teams scaling AI-powered operations
- SaaS and software companies running AI in production
- Teams where AI decisions impact customers, revenue, or risk
- Organizations that need AI systems to be dependable, auditable, and controllable

This is especially relevant when AI systems are no longer experimental — but operationally critical.


## When to Use This

Use this system when:

- AI workflows directly affect customers or revenue
- Failure modes must be detected before they cause damage
- Cost, latency, and quality need active governance
- Human oversight is required for high-risk decisions
- Leadership needs confidence in how AI behaves in production


---

## Problem Statement

Modern enterprises deploy LLM-powered systems without sufficient controls
for response quality, cost, failure handling, and auditability.

This repository demonstrates how to design and operate an agentic AI system
that is safe, observable, and suitable for real business workflows.

---

## What This System Does

- This system acts as an operational control plane for AI workflows in production.
- Orchestrates multi-agent LLM workflows
- Retrieves and bounds high-signal context
- Evaluates responses before execution
- Routes tasks across LLM providers
- Escalates low-confidence cases to humans
- Logs decisions for audit and analysis

---

## What This System Intentionally Does NOT Do

- No user-facing UI
- No fine-tuning
- No autonomous self-modifying agents
- No multi-cloud abstraction
- No unnecessary framework complexity

These exclusions are deliberate design choices.

---

## Example Business Use Case

### AI-Powered Customer Support (Production Scenario)

Incoming support requests are processed through a governed agentic pipeline that:

1. Retrieves only high-signal, bounded knowledge
2. Generates a response within defined quality thresholds
3. Evaluates confidence, risk, and cost
4. Automatically responds or escalates to a human

This ensures AI assistance improves efficiency **without introducing uncontrolled risk**.


---

## Architecture Overview

### **Core Components**
- Workflow orchestration: n8n
- Agent framework: CrewAI
- Runtime: AWS ECS (Fargate)
- Storage: PostgreSQL + pgvector, S3
- Observability: Langfuse, CloudWatch
- Notifications: Slack
```
graph LR
    subgraph "External Triggers"
        Webhook[n8n Webhook]
        Slack[Slack Event]
    end

    subgraph "The Control Plane (AWS Fargate)"
        Orc["🧠 Orchestrator Agent"]
        Eval["⚖️ Evaluation Agent"]
        Auth{Policy Check}
    end

    subgraph "The Action Layer"
        Ret["🔍 Retrieval Agent"]
        Action["🛠️ Action Agent"]
    end

    subgraph "Storage & Monitoring"
        DB[(PostgreSQL / pgvector)]
        Obs[Langfuse Observability]
    end

    %% Flow
    Webhook --> Orc
    Orc --> Auth
    Auth -->|Approved| Ret
    Ret --> DB
    DB --> Orc
    Orc --> Eval
    Eval -->|Confidence > 0.85| Action
    Eval -->|Low Confidence| Slack
    Action --> Obs
Detailed architecture decisions are documented in:
- `ARCHITECTURE.md`
- `DECISIONS.md`
```

---

## Agent Responsibilities

### - **Orchestrator Agent**  
  Controls execution flow and enforces policies

### - **Retrieval Agent**  
  Fetches and bounds relevant context

### - **Evaluation Agent**  
  Scores responses and determines approval or escalation

### - **Action Agent**  
  Executes approved actions only

---

## Reliability & Governance

### 🛡️ Deterministic Governance & Anti-Hallucination
This system replaces "vibe-checking" with Deterministic Guardrails:

### Pydantic Validation: Every agent output is validated against a strict schema. If the LLM returns malformed data, the Orchestrator forces a retry.

### Context Bounding: The Retrieval Agent is restricted to specific pgvector namespaces to prevent the model from "wandering" into irrelevant data.

### The 0.85 Confidence Rule: The Evaluation Agent uses a customized rubric to score groundedness. Any response scoring below 0.85 is automatically routed to a Human-in-the-Loop (Slack) rather than being sent to the customer.
---

## Deployment Model

- Containerized service running on AWS ECS (Fargate)
- Secrets managed via AWS Secrets Manager
- IAM roles follow least-privilege principles
- Event-driven triggers via n8n webhooks

Infrastructure definitions are located in `infra/`.

This deployment model reflects real-world production environments used by scaling teams.

---

## Project Status

### Status: 🚀 Production-Ready (v1.0)

### CI/CD: GitHub Actions enabled for automated testing.

### Security: PII-scrubbing middleware included in the Retrieval Layer.

### Scalability: Stateless architecture ready for AWS Fargate horizontal scaling.

---

## Why This Project Exists

This repository is intentionally designed to reflect how senior engineers
build and operate AI systems in production environments.

It favors correctness, governance, and clarity over novelty.


