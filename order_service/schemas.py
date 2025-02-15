from pydantic import BaseModel

class OrderDetailCreate(BaseModel):
    order_id: int
    product_id: int
    quantity: int
    subtotal: float

class OrderCreate(BaseModel):
    user_id: int
    cart_id: int





