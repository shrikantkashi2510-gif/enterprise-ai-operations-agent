
# Cost Model

This document outlines the primary cost drivers of the Enterprise AI
Operations Agent and the strategies used to control and optimize cost.

The system is designed to make cost explicit and measurable rather than
opaque or incidental.

---

## Primary Cost Drivers

### 1. LLM Inference
- Token usage for prompt + response
- Model selection (primary vs fallback)
- Retry and reprocessing events

### 2. Vector Retrieval
- Database compute for similarity search
- Storage for embeddings and documents

### 3. Infrastructure
- ECS Fargate compute
- Network egress (if applicable)
- Logging and observability storage

---

## Cost Control Strategies

### Model Routing
- Default to primary model only when confidence is required
- Route low-risk tickets to lower-cost models
- Avoid retries unless explicitly justified

### Context Bounding
- Hard limits on retrieved context size
- Prevent prompt stuffing and runaway token usage

### Escalation Preference
- Escalate uncertain cases instead of repeated LLM calls
- Human review is cheaper than uncontrolled inference loops

---

## Cost Visibility

The system logs:
- Tokens consumed per request
- Model used
- Evaluation outcome
- Escalation rate

These metrics enable:
- Per-ticket cost attribution
- Regression detection
- Budget forecasting

---

## Non-Goals (v1)

- No automated cost optimization
- No dynamic pricing strategies
- No fine-grained per-user billing
