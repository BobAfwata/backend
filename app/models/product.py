from sqlalchemy import Column, String, Float, Integer
from app.db.base import Base
import uuid

class Product(Base):
    __tablename__ = "products"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False, default=0)
    description = Column(String)
    image_url = Column(String)
