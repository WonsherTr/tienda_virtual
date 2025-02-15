from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from database import SessionLocal
from models import Order, Cart, Product
from schemas import OrderCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    db_order = Order(**order.dict())
    db_order.created_at = datetime.today()
    db_order.status = "completed"

    db_cart = db.query(Cart).filter(Cart.id == order.cart_id).first()
    db_product = db.query(Product).filter(Product.id == db_cart.product_id).first()
    if db_cart and db_product:
        db_order.total = db_product.price * db_cart.quantity

    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

@router.get("/")
def list_cart(db: Session = Depends(get_db)):
    return db.query(Order).all()
