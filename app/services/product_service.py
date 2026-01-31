from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import Product as Product_db


class ProductServices:

    @classmethod
    async def find_one_or_none_by_id(
        cls,
        product_id: int,
        session: AsyncSession,
    ) -> Product_db | None:
        query = select(Product_db).where(Product_db.product_id == product_id)
        product = await session.execute(query)
        return product.scalar_one_or_none()
