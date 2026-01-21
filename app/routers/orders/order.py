from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.order import OrderOutput
from app.schemas.order_product import OrderProductOutput
from app.services.order_service import OrderServices
from database.db_session import get_async_session

router = APIRouter(
    prefix="/orders",
    tags=["orders"],
)


@router.get("/{order_id}", response_model=OrderOutput)
async def get_order_by_id(
    order_id: int,
    session: AsyncSession = Depends(get_async_session),
) -> OrderOutput:
    try:
        order = await OrderServices.find_one_or_none_by_id(
            order_id=order_id,
            session=session,
        )
        return OrderOutput.model_validate(order)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=f"Order not found: {order_id}")


@router.post("/{order_id}/products/{product_id}")
async def add_product_to_order(
    order_id: int,
    product_id: int,
    quantity: int,
    session: AsyncSession = Depends(get_async_session),
) -> OrderProductOutput:
    try:
        order_product = await OrderServices.add_product_to_order(
            order_id=order_id,
            product_id=product_id,
            product_quantity=quantity,
            session=session,
        )
        return OrderProductOutput.model_validate(order_product)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
