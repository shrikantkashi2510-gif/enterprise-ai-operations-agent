class NotificationService:
    """
    Sends alerts and notifications for escalations,
    failures, or policy violations.
    """

    def notify_escalation(self, ticket_id: str, reason: str) -> None:
        """
        Notify humans that a ticket requires manual review.
        """
        raise NotImplementedError

    def notify_failure(self, error: Exception) -> None:
        """
        Notify system owners of operational failures.
        """
        raise NotImplementedError
