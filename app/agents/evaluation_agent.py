from typing import Dict


class EvaluationAgent:
    """
    Evaluates LLM-generated responses for quality, confidence,
    and risk before execution.

    This agent acts as the system's safety gate.
    """

    def run(self, response: str, context: Dict) -> Dict:
        """
        Evaluate the generated LLM response.

        Args:
            response: The raw LLM output
            context: Metadata including sources, model used, latency

        Returns:
            Evaluation result containing:
            - confidence_score (0.0–1.0)
            - risk_flags (list)
            - decision (approve | escalate)
        """
        raise NotImplementedError
