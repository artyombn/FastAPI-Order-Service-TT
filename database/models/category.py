from typing import Optional

from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_model import Base


class Category(Base):

    # Main fields
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    parent_id: Mapped[Optional[int]] = mapped_column(
        BigInteger,
        ForeignKey("categories.id"),
        nullable=True,
        index=True,
    )

    # Relationships child -> parent -> Many To One
    parent: Mapped[Optional["Category"]] = relationship(
        "Category",
        remote_side=[id],
        back_populates="children",
    )

    # Relationships parent -> children -> One To Many
    children: Mapped[list["Category"]] = relationship(
        "Category",
        back_populates="parent",
        cascade="all, delete-orphan",
    )
