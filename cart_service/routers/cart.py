from fastapi import APIRouter, Depends, HTTPException
from datetime import datetime
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
    db_cart = Cart(**cart.dict())  # Aquí usas Cart en lugar de cart
    db_cart.added_at = datetime.today()  # Asegúrate de llamar a la función con `()`
    db.add(db_cart)
    db.commit()
    db.refresh(db_cart)  # Refresca para obtener la data actualizada de la BD
    return db_cart


@router.get("/")
def list_cart(db: Session = Depends(get_db)):
    return db.query(Cart).all()



