from sqlalchemy import Column, Integer, String, ForeignKey, Float, Enum, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    role = Column(Enum('admin', 'customer'), default='customer')

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255))
    price = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category")
class RevokedToken(Base):
    __tablename__ = "revoked_tokens"
    
    token = Column(String, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
