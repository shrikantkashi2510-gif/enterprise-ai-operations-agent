from typing import Dict


class PersistenceService:
    """
    Handles persistence of tickets, responses, evaluations,
    and audit logs.

    All writes to durable storage go through this service.
    """

    def save_ticket(self, ticket: Dict) -> None:
        """Persist incoming support ticket."""
        raise NotImplementedError

    def save_response(self, ticket_id: str, response: str) -> None:
        """Persist generated LLM response."""
        raise NotImplementedError

    def save_evaluation(self, ticket_id: str, evaluation: Dict) -> None:
        """Persist evaluation results for auditability."""
        raise NotImplementedError
