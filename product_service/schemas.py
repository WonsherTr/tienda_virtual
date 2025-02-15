from pydantic import BaseModel
class CategoryCreate(BaseModel):
    name: str

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    category_id: int
