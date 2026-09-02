from app.agents.state import AgentState

def validate_output(state: AgentState):
    answer = state.get("answer", "")
    if not answer:
        return {
            "answer": "I could not produce a reliable answer. Please route this request for human review.",
            "confidence": 0.0,
            "requires_hitl": True,
        }
    return {}
