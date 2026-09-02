from app.agents.state import AgentState
from app.tools.claims_tool import get_claim_status
from app.integration.kafka import publish_event

def claims_agent(state: AgentState):
    member_id = state.get("member_id") or "M1001"
    claim = get_claim_status(member_id)
    event = {
        "event_type": "claims.inquiry",
        "member_id": member_id,
        "correlation_id": "demo-correlation-id",
    }
    publish_event("pharmacy.claims.inquiry", event)
    return {
        "answer": (
            f"Synthetic claim inquiry result for {member_id}: "
            f"claim {claim['claim_id']} is {claim['status']}."
        ),
        "sources": [{"id": claim["claim_id"], "source": "synthetic_claims"}],
        "confidence": 0.96,
        "requires_hitl": False,
    }
