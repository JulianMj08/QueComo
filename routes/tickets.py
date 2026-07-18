from fastapi import APIRouter, UploadFile, File
from pathlib import Path
import shutil
from fastapi import Depends, HTTPException, status

from config import UPLOADS_DIR
from ai.ia import extract_ticket
from database.database import save_ticket
from security import get_current_user

tickets_router = APIRouter()

# ENDPONT PARA ENVIAR TICKETS A LA BASE DE DATOS.
@tickets_router.post("/facturas") #back
async def upload_ticket(img: UploadFile = File(...), current_user = Depends(get_current_user) ):

    route = UPLOADS_DIR / img.filename

    with open(route, "wb") as buffer:
        shutil.copyfileobj(img.file, buffer)
        
        result = extract_ticket(str(route))

        save_ticket(current_user["id"], result)

    return {
        "mensaje": "Imagen procesada correctamente",
        "resultado": result,
        
        # "archivo": imagen.filename Ya no necesitamos extraer la imagen(eso era solo para pruebas) ahora necesitamos solo extraer lo datos de la imagen
    } 