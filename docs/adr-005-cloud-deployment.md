# ADR-005: Cloud Deployment Strategy

## Status
Accepted

## Context
The target architecture must support cloud-native deployment while avoiding unnecessary coupling between application design and one cloud provider.

## Decision
Containerize the application and express infrastructure through Terraform. Use managed services for identity, secrets, observability, events, and model hosting where they meet enterprise requirements.

## Consequences
- Repeatable environments.
- Clear separation between application and infrastructure.
- Easier portability across AWS, Azure, and GCP.
- Requires cloud-specific security and operational adapters.
