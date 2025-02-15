from pydantic import BaseModel

class CategoryCreate(BaseModel):
    name: str

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    category_id: int

class CartCreate(BaseModel):
    user_id: int
    product_id: int
    quantity: int

class OrderCreate(BaseModel):
    user_id: int
    cart_id: int