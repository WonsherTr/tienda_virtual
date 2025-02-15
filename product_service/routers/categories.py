from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Category
from database import SessionLocal
from schemas import CategoryCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_categories(db: Session = Depends(get_db)):
    return db.query(Category).all()

@router.post("/")
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    print(category)
    db_category = Category(**category.dict())
    db.add(db_category)
    db.commit()
    return db_category