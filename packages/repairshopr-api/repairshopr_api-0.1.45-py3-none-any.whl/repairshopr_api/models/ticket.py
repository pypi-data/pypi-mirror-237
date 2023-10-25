from dataclasses import dataclass, field
from datetime import datetime

from repairshopr_api.base.model import BaseModel


@dataclass
class Comment(BaseModel):
    id: int
    created_at: str = None
    updated_at: str = None
    ticket_id: int = None
    subject: str = None
    body: str = None
    tech: str = None
    hidden: bool = None
    user_id: int = None


@dataclass
class Properties(BaseModel):
    id: int = None
    day: str = None
    case: str = None
    other: str = None
    s_n_num: str = None
    tag_num: str = None
    claim_num: str = None
    location: str = None


@dataclass
class Ticket(BaseModel):
    id: int
    number: int = None
    subject: str = None
    created_at: datetime = None
    customer_id: int = None
    customer_business_then_name: str = None
    due_date: datetime = None
    resolved_at: datetime = None
    start_at: datetime = None
    end_at: datetime = None
    location_id: int = None
    problem_type: str = None
    status: str = None
    ticket_type_id: int = None
    properties: Properties = field(default_factory=Properties)
    user_id: int = None
    updated_at: str = None
    pdf_url: str = None
    priority: str = None
    comments: list[Comment] = field(default_factory=list)
