from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.core.security import hash_password, create_token

router = APIRouter()

@router.post("/register")
def register(email: str, password: str, db: Session = Depends(get_db)):
    user = {"email": email, "password": hash_password(password)}
    return {"msg": "user created"}

@router.post("/login")
def login(email: str, password: str):
    token = create_token({"sub": email})
    return {"access_token": token}