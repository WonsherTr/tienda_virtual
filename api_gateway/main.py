# API Gateway - Comunicación entre microservicios
from fastapi import FastAPI
import httpx

app = FastAPI(title="API Gateway")

@app.get("/")
def health_check():
    return {"message": "API Gateway Running"}

@app.get("/products")
async def get_products():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://product_service:8002/products")
        return response.json()

@app.get("/cart")
async def get_cart():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://cart_service:8003/cart")
        return response.json()

@app.get("/orders")
async def get_orders():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://order_service:8004/orders")
        return response.json()

