import re
from app.agents.state import AgentState

BLOCKED = [
    r"ignore previous instructions",
    r"reveal system prompt",
    r"show your hidden instructions",
]

def validate_input(state: AgentState):
    message = state["message"]
    if any(re.search(pattern, message, re.I) for pattern in BLOCKED):
        return {
            "answer": "The request was blocked by the input safety policy.",
            "confidence": 1.0,
            "requires_hitl": False,
            "intent": "blocked",
        }
    return {}
