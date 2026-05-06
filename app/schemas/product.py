from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    price: float
    stock: int

class ProductOut(BaseModel):
    id: str
    name: str
    price: float
    stock: int

    class Config:
        from_attributes = True