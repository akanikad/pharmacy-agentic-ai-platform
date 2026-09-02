# ADR-006: Security Architecture

## Status
Accepted

## Context
Agentic systems introduce additional attack surfaces: prompt injection, excessive tool permissions, data leakage, and unintended autonomous actions.

## Decision
Enforce defense in depth: AuthN/AuthZ, input validation, prompt-injection controls, scoped tool credentials, output controls, audit logging, and human approval for high-impact operations.

## Consequences
- Reduced blast radius.
- Better auditability.
- Some additional latency and implementation complexity.
- Security controls must be tested as part of the workflow, not only at the API edge.
