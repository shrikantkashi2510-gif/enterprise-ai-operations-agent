from typing import List


class RetrievalAgent:
    """
    Responsible for retrieving and filtering relevant context
    for a given support ticket.

    Guarantees:
    - Only high-signal context is returned
    - Context size is bounded
    - Sources are traceable
    """

    def run(self, ticket_id: str, query: str) -> List[str]:
        """
        Retrieve context relevant to the support ticket.

        Args:
            ticket_id: Unique identifier of the support ticket
            query: Natural language query derived from the ticket

        Returns:
            List of context snippets to be used by the LLM
        """
        raise NotImplementedError
