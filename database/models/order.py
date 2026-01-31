from datetime import datetime

from sqlalchemy import BigInteger, TIMESTAMP, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.models.base_model import Base


class Order(Base):

    # Main fields
    order_id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, autoincrement=True
    )
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, nullable=False, server_default=func.now()
    )
    status: Mapped[str] = mapped_column(nullable=False, server_default="created")

    # Relationships orders -> client -> Many to One
    client_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("clients.client_id"),
        nullable=False,
        index=True,
    )

    client: Mapped["Client"] = relationship(
        "Client",
        back_populates="order",
    )

    order_products: Mapped[list["OrderProduct"]] = relationship(
        "OrderProduct",
        back_populates="order",
        cascade="all, delete-orphan",
    )
