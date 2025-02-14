from fastapi import FastAPI
from routers.products import router as products_router
from routers.categories import router as categories_router

app = FastAPI(title="Product Service")

# Incluir routers de productos y categorías
app.include_router(products_router, prefix="/products", tags=["Products"])
app.include_router(categories_router, prefix="/categories", tags=["Categories"])

# Endpoint de verificación del servicio
@app.get("/")
def health_check():
    return {"message": "Product Service Running"}
