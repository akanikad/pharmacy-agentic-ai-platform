from app.agents.state import AgentState
from app.rag.retriever import retrieve

def prior_auth_agent(state: AgentState):
    docs = retrieve("prior authorization documentation requirements")
    return {
        "answer": (
            "Based on the synthetic policy knowledge base, the workflow "
            "typically requires the medication/request details and supporting "
            "clinical documentation specified by the applicable policy. "
            "A real determination must be made by the authorized workflow/team."
        ),
        "sources": [{"id": d["id"], "source": d["source"]} for d in docs],
        "confidence": 0.81 if docs else 0.4,
        "requires_hitl": False if docs else True,
    }
