from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    name: str | None = None
    role: str = "agent"
    is_active: bool = True


class UserOut(BaseModel):
    id: str
    email: EmailStr
    name: str | None = None
    role: str
    is_active: bool

    class Config:
        from_attributes = True
