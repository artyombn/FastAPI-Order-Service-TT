from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class OrderBase(BaseModel):
    """
    Base Order schema
    """

    created_at: Optional[datetime] = Field(
        description="Order creation datetime",
    )
    status: Optional[str] = Field(
        min_length=3,
        max_length=30,
        description="Order status",
    )
    client_id: int = Field(
        description="Client_id",
    )


class OrderOutput(OrderBase):
    """
    Response model
    """

    id: int

    model_config = {"from_attributes": True}
