from pydantic import BaseModel, EmailStr


class CustomerCreate(BaseModel):
    name: str
    email: EmailStr | None = None
    phone: str | None = None
    address: str | None = None


class CustomerUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    phone: str | None = None
    address: str | None = None


class CustomerOut(BaseModel):
    id: str
    name: str
    email: EmailStr | None = None
    phone: str | None = None
    address: str | None = None

    class Config:
        from_attributes = True
