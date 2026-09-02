from app.agents.state import AgentState

def classify_intent(state: AgentState):
    text = state["message"].lower()

    if any(x in text for x in ["claim", "adjudication", "rejected", "paid"]):
        intent = "claims"
    elif any(x in text for x in ["prior authorization", "prior auth", "authorization"]):
        intent = "prior_authorization"
    else:
        intent = "knowledge"

    return {"intent": intent}
