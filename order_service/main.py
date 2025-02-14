from fastapi import FastAPI
from routers.orders import router as order_service

app = FastAPI(title="Auth Service")
app.include_router(order_service, prefix="/orders")

@app.get("/")
def health_check():
    return {"message": "Order Service Running"}
