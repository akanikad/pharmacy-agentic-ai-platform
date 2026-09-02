# ADR-004: Event-Driven Integration with Kafka

## Status
Accepted

## Context
PBM workflows cross multiple systems and often contain asynchronous steps. Point-to-point synchronous coupling increases failure propagation and makes downstream evolution harder.

## Decision
Use Kafka for domain events and asynchronous workflow integration while retaining synchronous APIs for request/response operations that need immediate results.

## Consequences
- Loose coupling and replayability.
- Independent scaling of consumers.
- Requires schema governance, idempotency, retry/DLQ strategy, and observability.

## Production evolution
Add Schema Registry, compatibility checks, idempotency keys, retry topics, DLQs, consumer lag alerts, and trace propagation.
