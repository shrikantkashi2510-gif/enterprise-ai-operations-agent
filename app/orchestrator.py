from app.agents.retrieval_agent import RetrievalAgent
from app.agents.evaluation_agent import EvaluationAgent
from app.agents.action_agent import ActionAgent
from app.services.llm_router import LLMRouter
from app.services.persistence import PersistenceService
from app.services.notifications import NotificationService
from app.models.ticket import SupportTicket


class Orchestrator:
    """
    Central coordinator for the AI Operations Agent.

    Enforces:
    - Execution order
    - Safety gates
    - Escalation policies
    """

    def __init__(self):
        self.retrieval_agent = RetrievalAgent()
        self.evaluation_agent = EvaluationAgent()
        self.action_agent = ActionAgent()

        self.llm_router = LLMRouter()
        self.persistence = PersistenceService()
        self.notifications = NotificationService()

    def handle_ticket(self, ticket: SupportTicket) -> dict:
        """
        Process a support ticket end-to-end.

        Returns a status dictionary for upstream systems.
        """

        # Persist incoming ticket
        self.persistence.save_ticket(ticket.__dict__)

        # Retrieve relevant context
        context_chunks = self.retrieval_agent.run(
            ticket_id=ticket.ticket_id,
            query=ticket.description
        )

        # Select LLM and generate response (stub)
        model = self.llm_router.select_model(context_chunks)
        llm_response = f"[stubbed response from {model}]"

        # Evaluate response
        evaluation = self.evaluation_agent.run(
            response=llm_response,
            context={
                "ticket_id": ticket.ticket_id,
                "model": model,
                "context_size": len(context_chunks)
            }
        )

        # Persist evaluation
        self.persistence.save_evaluation(
            ticket_id=ticket.ticket_id,
            evaluation=evaluation
        )

        # Execute or escalate
        if evaluation["decision"] == "approve":
            self.action_agent.run(
                ticket_id=ticket.ticket_id,
                response=llm_response,
                approved=True
            )
            self.persistence.save_response(
                ticket_id=ticket.ticket_id,
                response=llm_response
            )
            return {"status": "success"}

        else:
            self.notifications.notify_escalation(
                ticket_id=ticket.ticket_id,
                reason="Low confidence or risk detected"
            )
            return {"status": "escalated"}

