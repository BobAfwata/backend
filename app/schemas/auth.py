from pydantic import BaseModel, EmailStr
from app.schemas.user import UserCreate


class UserRegister(UserCreate):
    pass


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class TokenOut(BaseModel):
    access_token: str
    token_type: str = "bearer"
