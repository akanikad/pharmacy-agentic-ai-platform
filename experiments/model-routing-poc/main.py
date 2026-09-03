"""
Model Routing POC

Routes requests to different model profiles based on task complexity.

The routing layer is intentionally provider-agnostic.
Actual model invocation can be connected to OpenAI, Anthropic,
Azure AI, Bedrock, or Vertex AI.
"""

from dataclasses import dataclass


@dataclass
class ModelProfile:
    name: str
    provider: str
    strengths: list
    cost_tier: str


MODELS = {
    "fast": ModelProfile(
        name="Fast Model",
        provider="OpenAI",
        strengths=["classification", "simple extraction", "short responses"],
        cost_tier="low",
    ),
    "reasoning": ModelProfile(
        name="Reasoning Model",
        provider="OpenAI",
        strengths=["complex reasoning", "planning", "multi-step tasks"],
        cost_tier="high",
    ),
    "long_context": ModelProfile(
        name="Long Context Model",
        provider="Anthropic",
        strengths=["large documents", "summarization", "document analysis"],
        cost_tier="medium",
    ),
}


def estimate_complexity(request: str) -> str:
    words = request.split()

    if len(words) > 150:
        return "long_context"

    reasoning_keywords = [
        "compare",
        "analyze",
        "recommend",
        "evaluate",
        "why",
        "design",
        "plan",
    ]

    if any(keyword in request.lower() for keyword in reasoning_keywords):
        return "reasoning"

    return "fast"


def route_request(request: str) -> ModelProfile:
    route = estimate_complexity(request)
    return MODELS[route]


def main():
    test_requests = [
        "Classify this pharmacy claim.",
        "Analyze this case and recommend the best authorization strategy.",
        "Summarize this large clinical document and identify key findings.",
    ]

    for request in test_requests:
        model = route_request(request)

        print("\nRequest:")
        print(request)

        print("Selected Model:")
        print(f"  {model.name}")

        print("Provider:")
        print(f"  {model.provider}")

        print("Cost Tier:")
        print(f"  {model.cost_tier}")


if __name__ == "__main__":
    main()
