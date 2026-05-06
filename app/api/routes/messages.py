from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.message import Message

router = APIRouter()

@router.post("/")
def send_message(content: str, db: Session = Depends(get_db)):
    msg = Message(content=content, sender="agent")
    db.add(msg)
    db.commit()
    return {"status": "stored", "id": msg.id}

@router.get("/")
def get_messages(db: Session = Depends(get_db)):
    return db.query(Message).all()