# ADR-003: Model and Provider Abstraction

## Status
Accepted

## Context
Model capabilities, pricing, latency, context windows, safety behavior, and enterprise approvals change rapidly. Coupling business agents directly to a single provider creates migration and optimization risk.

## Decision
Use a provider abstraction behind the agent layer. Business workflows should request capabilities rather than directly constructing provider-specific clients.

## Consequences
- Supports model routing and fallback.
- Makes evaluation across models easier.
- Reduces vendor lock-in.
- Adds a small abstraction layer and requires provider-specific testing.

## Production evolution
Add model registry, prompt/version management, routing policy, token/cost telemetry, safety configuration, and automated evaluation gates.
