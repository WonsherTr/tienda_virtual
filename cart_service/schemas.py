from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    password: str
    email: str

class CategoryCreate(BaseModel):
    name: str

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    category_id: int

class LoginSchema(BaseModel):
    username: str
    password: str

class CartCreate(BaseModel):
    user_id: int
    product_id: int
    quantity: int
    added_at: datetime
