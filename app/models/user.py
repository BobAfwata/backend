from sqlalchemy import Column, String, Boolean
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password_hash = Column(String)
    role = Column(String)  # agent / owner
    is_active = Column(Boolean, default=True)