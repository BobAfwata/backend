from sqlalchemy import Column, String, Boolean
from app.db.base import Base
import uuid

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String)
    email = Column(String, unique=True, nullable=False, index=True)
    password_hash = Column(String, nullable=False)
    role = Column(String, default="agent")  # agent / owner
    is_active = Column(Boolean, default=True)
