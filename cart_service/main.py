from fastapi import FastAPI
from routers.cart import router as cart_service

app = FastAPI(title="Cart Service")
app.include_router(cart_service, prefix="/cart")

@app.get("/")
def health_check():
    return {"message": "Cart Service Running"}
