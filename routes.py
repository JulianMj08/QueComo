from fastapi import APIRouter, UploadFile, File

router = APIRouter()


@router.get("/")
def inicio():
    return {
        "mensaje": "API de reconocimiento de facturas funcionando"
    }

@router.post("/facturas")
def recibir_factura(imagen: UploadFile = File(...)):
    return {
        "nombre": imagen.filename,
        "tipo": imagen.content_type
    }    