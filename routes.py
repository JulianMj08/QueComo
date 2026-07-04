from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def inicio():
    return {
        "mensaje": "API de reconocimiento de facturas funcionando"
    }