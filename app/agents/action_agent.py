class ActionAgent:
    """
    Executes approved actions such as sending responses
    or updating ticket status.

    This agent must never act without explicit approval.
    """

    def run(self, ticket_id: str, response: str, approved: bool) -> None:
        """
        Execute the final action.

        Args:
            ticket_id: Support ticket identifier
            response: Final response to be sent
            approved: Whether the evaluation agent approved execution
        """
        if not approved:
            raise PermissionError("Action execution not approved")

        raise NotImplementedError
