from sqlalchemy import BigInteger, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_model import Base
from .category import Category


class Product(Base):

    # Main fields
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    quantity: Mapped[int] = mapped_column(nullable=False)
    price: Mapped[int] = mapped_column(Numeric(10, 2), nullable=False)

    category_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("categories.id"),
        nullable=False,
        index=True,
    )

    # Relationships product -> category -> Many To One
    category: Mapped["Category"] = relationship(
        "Category",
        back_populates="products",
    )
