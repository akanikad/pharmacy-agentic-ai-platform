from fastapi import FastAPI
from pydantic import BaseModel, Field
from app.agents.graph import run_agent
from app.observability.logging import configure_logging

configure_logging()

app = FastAPI(
    title="Pharmacy Agentic AI Platform",
    version="0.1.0",
    description="Independent enterprise healthcare Agentic AI reference implementation.",
)

class AssistRequest(BaseModel):
    message: str = Field(min_length=3, max_length=4000)
    member_id: str | None = None

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/v1/assist")
def assist(request: AssistRequest):
    return run_agent(request.message, request.member_id)
