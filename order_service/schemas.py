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

class OrderDetailCreate(BaseModel):
    order_id: int
    product_id: int
    quantity: int
    subtotal: float

class OrderCreate(BaseModel):
    user_id: int
    total: float
    created_at: datetime
    status: str





