"""
Agent Framework Evaluation POC

Defines a common workflow that can be implemented using
different agent frameworks.

The purpose is to compare orchestration characteristics,
not to declare a universal framework winner.
"""

from dataclasses import dataclass


@dataclass
class EvaluationResult:
    framework: str
    workflow: str
    strengths: list
    tradeoffs: list


def evaluate_frameworks():
    results = [
        EvaluationResult(
            framework="LangGraph",
            workflow="Stateful multi-step workflow",
            strengths=[
                "Explicit state management",
                "Graph-based orchestration",
                "Good control over execution flow",
            ],
            tradeoffs=[
                "More architectural setup",
                "Requires understanding of graph/state concepts",
            ],
        ),
        EvaluationResult(
            framework="CrewAI",
            workflow="Role-based multi-agent workflow",
            strengths=[
                "Simple agent/team abstractions",
                "Fast prototyping",
                "Natural role-based delegation",
            ],
            tradeoffs=[
                "Less explicit control for complex state machines",
                "Additional abstraction layer",
            ],
        ),
    ]

    return results


def main():
    print("=== Agent Framework Evaluation ===")

    for result in evaluate_frameworks():
        print(f"\nFramework: {result.framework}")
        print(f"Workflow: {result.workflow}")

        print("Strengths:")
        for item in result.strengths:
            print(f"  - {item}")

        print("Trade-offs:")
        for item in result.tradeoffs:
            print(f"  - {item}")


if __name__ == "__main__":
    main()
