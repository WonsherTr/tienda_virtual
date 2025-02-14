from fastapi import APIRouter

router = APIRouter()

@router.get("/categories")
def get_categories():
    return {"message": "Lista de categorías"}
