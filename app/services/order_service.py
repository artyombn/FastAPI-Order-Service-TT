from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import Product as Product_db
from database.models import Order as Order_db
from database.models import OrderProduct as OrderProduct_db


class OrderServices:

    @classmethod
    async def find_one_or_none_by_id(
        cls,
        order_id: int,
        session: AsyncSession,
    ) -> Order_db | None:
        query = select(Order_db).where(Order_db.id == order_id)
        order = await session.execute(query)
        return order.scalar_one_or_none()

    @classmethod
    async def add_product_to_order(
        cls,
        product_id: int,
        order_id: int,
        product_quantity: int,
        session: AsyncSession,
    ) -> OrderProduct_db:
        if product_quantity <= 0:
            raise ValueError("Product quantity must be >= 1")

        query_product = select(Product_db).where(Product_db.id == product_id)
        query_order = select(Order_db).where(Order_db.id == order_id)

        result_product = await session.execute(query_product)
        result_order = await session.execute(query_order)

        product = result_product.scalar_one_or_none()
        if not product:
            raise ValueError(f"Product not found, id={id}")
        order = result_order.scalar_one_or_none()
        if product.quantity < product_quantity:
            raise ValueError(
                f"Not enough product in stock. Available only -> {product.quantity}"
            )
        query_is_product = select(OrderProduct_db).where(
            OrderProduct_db.order_id == order_id,
            OrderProduct_db.product_id == product_id,
        )
        is_product_in_order = await session.execute(query_is_product)
        order_product = is_product_in_order.scalar_one_or_none()

        if order_product:
            order_product.product_quantity += product_quantity
        else:
            order_product = OrderProduct_db(
                order_id=order_id,
                product_id=product_id,
                product_quantity=product_quantity,
                product_price_at_order=product.price,
            )
            session.add(order_product)

        product.quantity -= product_quantity

        await session.commit()
        await session.refresh(order_product)

        return order_product
