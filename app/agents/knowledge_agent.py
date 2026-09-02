from app.agents.state import AgentState
from app.rag.retriever import retrieve
from app.llm.provider import generate

def knowledge_agent(state: AgentState):
    docs = retrieve(state["message"])
    context = "\n\n".join(d["text"] for d in docs)
    prompt = (
        "Answer using only the supplied synthetic policy context. "
        "If the context is insufficient, say so and recommend human review.\n\n"
        f"QUESTION:\n{state['message']}\n\nCONTEXT:\n{context}"
    )
    answer = generate(prompt)
    confidence = 0.88 if docs else 0.35
    return {
        "answer": answer,
        "sources": [{"id": d["id"], "source": d["source"]} for d in docs],
        "confidence": confidence,
        "requires_hitl": confidence < 0.72,
    }
