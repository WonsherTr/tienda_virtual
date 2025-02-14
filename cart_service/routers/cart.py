from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Cart
from schemas import CartCreate



router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_cart(cart: CartCreate, db: Session = Depends(get_db)):
    db_cart = cart(**cart.dict())
    db.add(db_cart)
    db.commit()
    return db_cart

@router.get("/")
def list_cart(db: Session = Depends(get_db)):
    return db.query(Cart).all()



