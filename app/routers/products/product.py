from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.order import OrderOutput
from app.schemas.product import ProductOutput
from app.services.product_service import ProductServices
from database.db_session import get_async_session

router = APIRouter(
    prefix="/products",
    tags=["products"],
)


@router.get("/{product_id}", response_model=ProductOutput)
async def get_product_by_id(
    product_id: int,
    session: AsyncSession = Depends(get_async_session),
) -> ProductOutput:
    try:
        product = await ProductServices.find_one_or_none_by_id(
            product_id=product_id,
            session=session,
        )
        return ProductOutput.model_validate(product)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=f"Product not found: {product_id}")
