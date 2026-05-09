from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    price: float
    stock: int
    description: str | None = None
    image_url: str | None = None

class ProductOut(BaseModel):
    id: str
    name: str
    price: float
    stock: int
    description: str | None = None
    image_url: str | None = None

    class Config:
        from_attributes = True
