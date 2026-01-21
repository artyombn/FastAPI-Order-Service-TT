from pydantic import BaseModel, Field


class OrderProductBase(BaseModel):
    """
    Base Order–Product schema
    """

    order_id: int = Field(description="Order_id")
    product_id: int = Field(description="Product_id")

    product_quantity: int = Field(
        ge=1,
        description="Product quantity in the order >= 1",
    )
    product_price_at_order: float = Field(
        ge=0.0,
        description="Product price at the moment of order >= 0.0",
    )


class OrderProductOutput(OrderProductBase):
    """
    Response model
    """

    model_config = {"from_attributes": True}


class AddProductToOrder(BaseModel):
    order_id: int = Field(description="Order_id")
    product_id: int = Field(description="Product_id")
    quantity: int = Field(ge=1, description="Product quantity in the order >= 1")
