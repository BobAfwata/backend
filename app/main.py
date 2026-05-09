from fastapi import FastAPI
from app.api.routes import auth, customers, messages, products, receipts, users, whatsapp
from app.db.base import Base
from app.db.session import engine
from app import models


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router, prefix="/auth")
app.include_router(customers.router, prefix="/customers")
app.include_router(products.router, prefix="/products")
app.include_router(messages.router, prefix="/messages")
app.include_router(receipts.router, prefix="/receipts")
app.include_router(users.router, prefix="/users")
app.include_router(whatsapp.router, prefix="/whatsapp")

@app.get("/")
def root():
    return {"status": "running"}
