from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductOut

router = APIRouter()


# CREATE PRODUCT
@router.post("/", response_model=ProductOut)
def create_product(data: ProductCreate, db: Session = Depends(get_db)):
    try:
        # Pydantic v2 fix
        product = Product(**data.model_dump())

        db.add(product)
        db.commit()
        db.refresh(product)

        return product

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


# GET ALL PRODUCTS
@router.get("/", response_model=list[ProductOut])
def get_products(db: Session = Depends(get_db)):
    try:
        products = db.query(Product).all()
        return products

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        raise HTTPException(status_code=500, detail=str(e))