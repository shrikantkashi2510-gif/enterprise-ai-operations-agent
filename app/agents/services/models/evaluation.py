from dataclasses import dataclass
from typing import List


@dataclass
class EvaluationResult:
    """
    Represents the evaluation outcome of an LLM response.

    This object determines whether the system
    is allowed to act autonomously.
    """

    confidence_score: float
    risk_flags: List[str]
    decision: str  # "approve" or "escalate"
