from fastapi import APIRouter, UploadFile, File
from pathlib import Path
import shutil

from config import UPLOADS_DIR

router = APIRouter()


@router.get("/")    
def inicio():
    return {
        "mensaje": "API de reconocimiento de facturas funcionando"
    }

@router.post("/facturas")
async def recibir_factura(imagen: UploadFile = File(...)):

    ruta = UPLOADS_DIR / imagen.filename

    with open(ruta, "wb") as buffer:
        shutil.copyfileobj(imagen.file, buffer)

    return {
        "mensaje": "Imagen guardada correctamente",
        "archivo": imagen.filename
    }   