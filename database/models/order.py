from datetime import datetime

from sqlalchemy import BigInteger, TIMESTAMP, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_model import Base
from .client import Client


class Order(Base):

    # Main fields
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, nullable=False, server_default=func.now()
    )
    status: Mapped[str] = mapped_column(nullable=False, server_default="created")

    # Relationships orders -> client -> Many to One
    client_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("clients.id"),
        nullable=True,
        index=True,
    )

    client: Mapped["Client"] = relationship(
        "Client",
        back_populates="orders",
    )
