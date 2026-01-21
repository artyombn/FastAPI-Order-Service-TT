from pydantic import BaseModel, Field, EmailStr


class ClientBase(BaseModel):
    """
    Base Client schema
    """

    first_name: str = Field(
        min_length=2,
        max_length=50,
        description="Client first name",
    )
    last_name: str = Field(
        min_length=2,
        max_length=50,
        description="Client last name",
    )
    email: EmailStr = Field(
        description="Unique client email address",
    )
    address: str = Field(
        min_length=5,
        max_length=255,
        description="Client address",
    )


class ClientOutput(ClientBase):
    """
    Response model
    """

    id: int

    model_config = {"from_attributes": True}
