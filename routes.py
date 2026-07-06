from fastapi import APIRouter, UploadFile, File
from pathlib import Path
import shutil

from config import UPLOADS_DIR
from ia import extraer_factura
from database import guardar_factura

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
        
        resultado = extraer_factura(str(ruta))

        guardar_factura(resultado)

    return {
        "mensaje": "Imagen procesada correctamente",
        "resultado": resultado,
        
        # "archivo": imagen.filename Ya no necesitamos extraer la imagen(eso era solo para pruebas) ahora necesitamos solo extraer lo datos de la imagen
    }   