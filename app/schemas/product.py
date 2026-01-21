from pydantic import BaseModel, Field


class ProductBase(BaseModel):
    """
    Base Product schema
    """

    name: str = Field(
        min_length=3,
        max_length=100,
        description="Product name must be between 3 and 100 characters",
    )
    quantity: int = Field(ge=0, description="Must be int and >= 0")
    price: float = Field(
        gt=0.0,
        le=9999999.99,
    )
    category_id: int = Field(
        description="Category ID",
    )


class ProductCreate(ProductBase):
    """
    Create a new Product
    """


class ProductOutput(ProductBase):
    """
    Response model
    """

    id: int

    model_config = {"from_attributes": True}
