from pydantic import BaseModel
from datetime import datetime
class CartCreate(BaseModel):
    user_id: int
    product_id: int
    quantity: int
