"""
Multi-Agent Handoff POC

Demonstrates explicit task delegation between specialized agents.

Flow:
User Request
    ↓
Triage Agent
    ↓
 ┌───────────────┬────────────────┐
 ↓               ↓                ↓
Clinical Agent   Policy Agent     Operations Agent
 └───────────────┴────────────────┘
                 ↓
            Final Synthesizer
"""

from dataclasses import dataclass
from typing import Dict


@dataclass
class Task:
    request: str
    category: str = ""
    context: Dict[str, str] = None

    def __post_init__(self):
        if self.context is None:
            self.context = {}


class TriageAgent:
    """Classifies the request and decides which specialist should handle it."""

    def route(self, task: Task) -> Task:
        text = task.request.lower()

        if any(word in text for word in ["drug", "medication", "dosage", "interaction"]):
            task.category = "clinical"

        elif any(word in text for word in ["coverage", "prior authorization", "policy"]):
            task.category = "policy"

        else:
            task.category = "operations"

        task.context["handoff_reason"] = (
            f"Request delegated to {task.category} specialist."
        )

        return task


class ClinicalAgent:
    def handle(self, task: Task) -> Task:
        task.context["specialist_response"] = (
            "Clinical specialist reviewed the medication-related request "
            "and identified the relevant clinical considerations."
        )
        return task


class PolicyAgent:
    def handle(self, task: Task) -> Task:
        task.context["specialist_response"] = (
            "Policy specialist reviewed coverage and authorization requirements."
        )
        return task


class OperationsAgent:
    def handle(self, task: Task) -> Task:
        task.context["specialist_response"] = (
            "Operations specialist reviewed workflow and fulfillment considerations."
        )
        return task


class SynthesizerAgent:
    def synthesize(self, task: Task) -> str:
        return (
            f"Category: {task.category}\n"
            f"Handoff: {task.context['handoff_reason']}\n"
            f"Result: {task.context['specialist_response']}"
        )


def run_workflow(request: str) -> str:
    task = Task(request=request)

    triage = TriageAgent()
    clinical = ClinicalAgent()
    policy = PolicyAgent()
    operations = OperationsAgent()
    synthesizer = SynthesizerAgent()

    task = triage.route(task)

    if task.category == "clinical":
        task = clinical.handle(task)
    elif task.category == "policy":
        task = policy.handle(task)
    else:
        task = operations.handle(task)

    return synthesizer.synthesize(task)


if __name__ == "__main__":
    request = (
        "A member is asking whether a medication requires prior authorization "
        "and what the next step should be."
    )

    print("=== Multi-Agent Handoff POC ===")
    print(run_workflow(request))
