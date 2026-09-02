# Cloud-Native PBM Reference Architecture

## Principles

- API-first
- domain-aligned services
- event-driven integration where asynchronous processing is appropriate
- zero-trust security boundary
- least privilege
- managed cloud services by default
- observable by design
- human oversight for high-impact AI decisions
- portable application containers

## Logical architecture

```mermaid
flowchart TB
    UX[Channels] --> API[API Gateway]
    API --> IAM[IAM / Auth]
    IAM --> APP[Cloud Run / GKE]

    APP --> AG[Agent Orchestration]
    AG --> RAG[RAG Platform]
    AG --> TOOLS[Domain Tools]
    AG --> LLM[Model Gateway]

    TOOLS --> KAFKA[Managed Kafka]
    KAFKA --> LEGACY[Legacy PBM Systems]

    RAG --> VECTOR[(Vector Search)]
    APP --> OBS[Logging / Metrics / Trace]
    APP --> SEC[Secrets / Policy / Security Controls]
```

## Architecture review checklist

- Business capability and bounded context identified
- synchronous vs asynchronous interactions justified
- data ownership identified
- failure modes and retry strategy defined
- idempotency addressed
- security boundary documented
- observability requirements defined
- RTO/RPO considered
- cost drivers identified
- buy-vs-build decision recorded
- migration and rollback plan defined
