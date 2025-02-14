from fastapi.security import OAuth2PasswordBearer
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User, RevokedToken
from schemas import LoginSchema
import jwt
import os

# Clave secreta para firmar JWT (se recomienda cargar desde un .env)
SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter()

# Función para obtener la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login")
def login(user_data: LoginSchema, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == user_data.username).first()
    
    if not user or user.password != user_data.password:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    token = jwt.encode({"user_id": user.id}, SECRET_KEY, algorithm="HS256")
    return {"access_token": token}

@router.post("/logout")
async def logout(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    # Verificar si el token ya ha sido revocado
    existing_token = db.query(RevokedToken).filter(RevokedToken.token == token).first()
    
    if existing_token:
        return JSONResponse(content={"message": "Token already revoked."}, status_code=400)

    revoked_token = RevokedToken(token=token)
    db.add(revoked_token)
    db.commit()

    return JSONResponse(content={"message": "Logout successful. Token has been revoked."})


