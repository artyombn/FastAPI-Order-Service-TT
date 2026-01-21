from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.order import OrderOutput
from app.schemas.order_product import OrderProductOutput, AddProductToOrder
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


@router.post("/add-product", response_model=OrderProductOutput)
async def add_product_to_order(
    request: AddProductToOrder,
    session: AsyncSession = Depends(get_async_session),
) -> OrderProductOutput:
    try:
        order_product = await OrderServices.add_product_to_order(
            order_id=request.order_id,
            product_id=request.product_id,
            product_quantity=request.quantity,
            session=session,
        )
        return OrderProductOutput.model_validate(order_product)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
