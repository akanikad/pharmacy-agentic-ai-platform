from langgraph.graph import StateGraph, START, END
from app.agents.state import AgentState
from app.agents.supervisor import classify_intent
from app.agents.knowledge_agent import knowledge_agent
from app.agents.claims_agent import claims_agent
from app.agents.pa_agent import prior_auth_agent
from app.guardrails.input_guardrail import validate_input
from app.guardrails.output_guardrail import validate_output

def route(state: AgentState):
    intent = state["intent"]
    if intent == "claims":
        return "claims"
    if intent == "prior_authorization":
        return "prior_auth"
    return "knowledge"

def build_graph():
    graph = StateGraph(AgentState)
    graph.add_node("validate_input", validate_input)
    graph.add_node("supervisor", classify_intent)
    graph.add_node("knowledge", knowledge_agent)
    graph.add_node("claims", claims_agent)
    graph.add_node("prior_auth", prior_auth_agent)
    graph.add_node("output_guardrail", validate_output)

    graph.add_edge(START, "validate_input")
    graph.add_edge("validate_input", "supervisor")
    graph.add_conditional_edges("supervisor", route, {
        "claims": "claims",
        "prior_auth": "prior_auth",
        "knowledge": "knowledge",
    })
    graph.add_edge("knowledge", "output_guardrail")
    graph.add_edge("claims", "output_guardrail")
    graph.add_edge("prior_auth", "output_guardrail")
    graph.add_edge("output_guardrail", END)
    return graph.compile()

agent_graph = build_graph()

def run_agent(message: str, member_id: str | None = None):
    result = agent_graph.invoke({
        "message": message,
        "member_id": member_id,
        "events": [],
    })
    return {
        "intent": result.get("intent"),
        "answer": result.get("answer"),
        "sources": result.get("sources", []),
        "confidence": result.get("confidence", 0.0),
        "requires_hitl": result.get("requires_hitl", False),
    }
