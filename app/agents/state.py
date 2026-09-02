from typing import TypedDict, Any

class AgentState(TypedDict, total=False):
    message: str
    member_id: str | None
    intent: str
    answer: str
    sources: list[dict[str, Any]]
    confidence: float
    requires_hitl: bool
    events: list[dict[str, Any]]
