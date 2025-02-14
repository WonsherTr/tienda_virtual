from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Order
from schemas import OrderCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_orders(order: OrderCreate, db: Session = Depends(get_db)):
    db_orders = Order(**order.dict())
    db.add(db_orders)
    db.commit()
    return db_orders

@router.get("/")
def list_cart(db: Session = Depends(get_db)):
    return db.query(Order).all()