from sqlalchemy import BigInteger, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.models.base_model import Base


class OrderProduct(Base):
    __tablename__ = "orders_products"

    # Main foreign keys
    order_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("orders.id"), primary_key=True
    )
    product_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("products.id"), primary_key=True
    )

    # Extra info
    product_quantity: Mapped[int] = mapped_column(nullable=False)
    product_price_at_order: Mapped[float] = mapped_column(
        Numeric(10, 2),
        nullable=False,
    )

    # Relationships
    order: Mapped["Order"] = relationship(
        "Order",
        back_populates="order_products",
    )
    product: Mapped["Product"] = relationship(
        "Product",
        back_populates="order_products",
    )
