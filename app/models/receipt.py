from datetime import datetime
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base
import uuid


class Receipt(Base):
    __tablename__ = "receipts"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    customer_id = Column(String, ForeignKey("customers.id"), nullable=False)
    total = Column(Float, nullable=False, default=0)
    payment_method = Column(String, default="cash")
    status = Column(String, default="paid")
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    customer = relationship("Customer", back_populates="receipts")
    items = relationship(
        "ReceiptItem",
        back_populates="receipt",
        cascade="all, delete-orphan",
    )


class ReceiptItem(Base):
    __tablename__ = "receipt_items"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    receipt_id = Column(String, ForeignKey("receipts.id"), nullable=False)
    product_id = Column(String, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Float, nullable=False)
    line_total = Column(Float, nullable=False)

    receipt = relationship("Receipt", back_populates="items")
    product = relationship("Product")
