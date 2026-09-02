# Technical Runbook

## API does not start

1. verify Python 3.12+
2. reinstall requirements
3. check port 8080
4. run `pytest -q`

## Kafka unavailable

The demo tool is designed to degrade safely and continue the reference workflow.
For production, Kafka availability should be treated as an explicit dependency
with retry, DLQ, monitoring, and alerting.

## Low confidence

The system should return a review-required state rather than inventing an answer.

## Production hardening checklist

- enterprise identity provider
- secrets manager
- private networking
- encryption
- centralized audit logging
- vulnerability scanning
- dependency management
- model/data governance
- PHI controls
- disaster recovery
- SLOs and alerting
