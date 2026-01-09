from datetime import datetime
from app.orchestrator import Orchestrator
from app.models.ticket import SupportTicket


def main():
    orchestrator = Orchestrator()

    # Example stub ticket
    ticket = SupportTicket(
        ticket_id="TICKET-001",
        user_id="user-123",
        subject="Login issue",
        description="I cannot log into my account.",
        created_at=datetime.utcnow()
    )

    result = orchestrator.handle_ticket(ticket)
    print(result)


if __name__ == "__main__":
    main()

