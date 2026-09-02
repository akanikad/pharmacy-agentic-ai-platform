# ADR-001: Agent Orchestration

## Status
Accepted

## Decision
Use LangGraph as the reference orchestration framework.

## Rationale
The workflow needs explicit state, deterministic routing, specialist agents,
tool boundaries, and the ability to introduce human review checkpoints.

## Alternatives
- custom Python state machine
- managed agent runtime
- single-agent tool calling

## Trade-off
LangGraph adds framework dependency but improves visibility and control over
multi-step stateful workflows.
