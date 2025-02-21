from fastapi import FastAPI, Body, Request
import httpx
from schemas import (
    ProductCreate,
    CategoryCreate,
    CartCreate,
    OrderCreate
)

app = FastAPI(title="API Gateway")

@app.get("/")
def health_check():
    return {"message": "API Gateway Running"}


##------------------------------Products------------------------------------#
@app.get("/products")
async def get_products():
    async with httpx.AsyncClient() as client:
        response = httpx.get("http://product_service:8002/products", follow_redirects=True)
        return response.json()
    
@app.post("/products")
async def create_product(product: ProductCreate = Body(...)):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://product_service:8002/products",
            json=product.model_dump(),
            follow_redirects=True
        )
    return response.json()


##------------------------------Categories----------------------------------#
@app.get("/categories")
async def get_categories():
    async with httpx.AsyncClient() as client:
        response = httpx.get("http://product_service:8002/categories", follow_redirects=True)
        return response.json()
    
@app.post("/categories")
async def create_category(category: CategoryCreate = Body(...)):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://product_service:8002/categories",
            json=category.model_dump(),
            follow_redirects=True
        )
    return response.json()


##------------------------------Cart---------------------------------------#
@app.get("/cart")
async def get_cart():
    async with httpx.AsyncClient() as client:
        response = httpx.get("http://cart_service:8003/cart", follow_redirects=True)
        return response.json()
    
@app.post("/cart")
async def create_category(cart: CartCreate = Body(...)):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://cart_service:8003/cart",
            json=cart.model_dump(),
            follow_redirects=True
        )
    return response.json()
    

##------------------------------Orders--------------------------------------#

@app.get("/orders")
async def get_orders():
    async with httpx.AsyncClient() as client:
        response = httpx.get("http://order_service:8004/orders", follow_redirects=True)
        return response.json()


@app.post("/orders")
async def create_order(order: OrderCreate = Body(...)):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://order_service:8004/orders",
            json=order.model_dump(),
            follow_redirects=True
        )
    return response.json()

##--------------------------------auth services---------------------------------#

@app.post("/auth/login")
async def login(request: Request):
    async with httpx.AsyncClient() as client:
        response = await client.post("http://auth_service:8001/login", json=await request.json())
        return response.json()


