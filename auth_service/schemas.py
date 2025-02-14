from pydantic import BaseModel

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
