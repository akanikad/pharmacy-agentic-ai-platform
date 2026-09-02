# ADR-002: Vector Store

## Status
Reference decision

Use PostgreSQL/pgvector for the local prototype because it reduces operational
complexity and supports metadata filtering.

For production, evaluate managed options such as Vertex AI Vector Search,
AlloyDB/pgvector, or enterprise-approved OpenSearch based on scale, latency,
security, operational ownership, and cost.
