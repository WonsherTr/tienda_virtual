from fastapi import FastAPI
from routers.auth import router as auth_router
from database import Base
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Auth Service")
app.include_router(auth_router, prefix="/auth")

@app.get("/")
def health_check():
    return {"message": "Auth Service Running"}
