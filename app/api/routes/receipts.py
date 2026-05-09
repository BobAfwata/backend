from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload
from app.db.session import get_db
from app.models.customer import Customer
from app.models.product import Product
from app.models.receipt import Receipt, ReceiptItem
from app.schemas.receipt import ReceiptCreate, ReceiptOut

router = APIRouter()


@router.post("/", response_model=ReceiptOut, status_code=status.HTTP_201_CREATED)
def create_receipt(data: ReceiptCreate, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.id == data.customer_id).first()
    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found",
        )

    if not data.items:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Receipt must contain at least one item",
        )

    receipt_items = []
    total = 0.0

    for item_data in data.items:
        if item_data.quantity <= 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Item quantity must be greater than zero",
            )

        product = db.query(Product).filter(Product.id == item_data.product_id).first()
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product not found: {item_data.product_id}",
            )

        if product.stock < item_data.quantity:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Not enough stock for product: {product.name}",
            )

        line_total = product.price * item_data.quantity
        total += line_total
        product.stock -= item_data.quantity

        receipt_items.append(
            ReceiptItem(
                product_id=product.id,
                quantity=item_data.quantity,
                unit_price=product.price,
                line_total=line_total,
            )
        )

    receipt = Receipt(
        customer_id=customer.id,
        total=total,
        payment_method=data.payment_method,
        status=data.status,
        items=receipt_items,
    )

    db.add(receipt)
    db.commit()
    db.refresh(receipt)
    return _get_receipt_or_404(receipt.id, db)


@router.get("/", response_model=list[ReceiptOut])
def get_receipts(db: Session = Depends(get_db)):
    return (
        db.query(Receipt)
        .options(
            joinedload(Receipt.customer),
            joinedload(Receipt.items).joinedload(ReceiptItem.product),
        )
        .order_by(Receipt.created_at.desc())
        .all()
    )


@router.get("/{receipt_id}", response_model=ReceiptOut)
def get_receipt(receipt_id: str, db: Session = Depends(get_db)):
    return _get_receipt_or_404(receipt_id, db)


@router.delete("/{receipt_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_receipt(receipt_id: str, db: Session = Depends(get_db)):
    receipt = db.query(Receipt).filter(Receipt.id == receipt_id).first()
    if not receipt:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Receipt not found",
        )

    db.delete(receipt)
    db.commit()


def _get_receipt_or_404(receipt_id: str, db: Session):
    receipt = (
        db.query(Receipt)
        .options(
            joinedload(Receipt.customer),
            joinedload(Receipt.items).joinedload(ReceiptItem.product),
        )
        .filter(Receipt.id == receipt_id)
        .first()
    )
    if not receipt:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Receipt not found",
        )
    return receipt
