from sqlalchemy import BigInteger, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_model import Base


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

    order_products: Mapped[list["OrderProduct"]] = relationship(
        "OrderProduct",
        back_populates="products",
        cascade="all, delete-orphan",
    )
