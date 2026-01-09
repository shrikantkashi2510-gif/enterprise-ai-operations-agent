from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class SupportTicket:
    """
    Represents an incoming support request.

    This is the primary business object that flows
    through the agentic system.
    """

    ticket_id: str
    user_id: str
    subject: str
    description: str
    created_at: datetime
    priority: Optional[str] = "normal"
