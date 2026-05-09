from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.db.base import Base
import uuid


class Customer(Base):
    __tablename__ = "customers"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    phone = Column(String, index=True)
    address = Column(String)

    receipts = relationship("Receipt", back_populates="customer")
