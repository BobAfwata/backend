from datetime import datetime
from pydantic import BaseModel
from app.schemas.customer import CustomerOut
from app.schemas.product import ProductOut


class ReceiptItemCreate(BaseModel):
    product_id: str
    quantity: int


class ReceiptCreate(BaseModel):
    customer_id: str
    items: list[ReceiptItemCreate]
    payment_method: str = "cash"
    status: str = "paid"


class ReceiptItemOut(BaseModel):
    id: str
    product_id: str
    quantity: int
    unit_price: float
    line_total: float
    product: ProductOut | None = None

    class Config:
        from_attributes = True


class ReceiptOut(BaseModel):
    id: str
    customer_id: str
    total: float
    payment_method: str
    status: str
    created_at: datetime
    customer: CustomerOut | None = None
    items: list[ReceiptItemOut] = []

    class Config:
        from_attributes = True
