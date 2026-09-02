from dataclasses import dataclass

@dataclass
class EvalResult:
    answer_quality: float
    groundedness: float
    retrieval_relevance: float
    latency_ms: float
    estimated_cost_usd: float
    safety_passed: bool

def overall_score(r: EvalResult) -> float:
    safety = 1.0 if r.safety_passed else 0.0
    return (
        0.30 * r.answer_quality
        + 0.25 * r.groundedness
        + 0.20 * r.retrieval_relevance
        + 0.15 * min(r.latency_ms / 2000, 1.0)
        + 0.10 * safety
    )
