from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_model import Base


class Client(Base):

    # Main fields
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    address: Mapped[str] = mapped_column(nullable=False)

    # Relationships client -> orders -> One To Many
    order: Mapped[list["Order"]] = relationship(
        back_populates="client",
        cascade="all, delete, delete-orphan",
    )
