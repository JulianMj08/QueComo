from fastapi import APIRouter, UploadFile, File
from pathlib import Path
import shutil
import json
from fastapi.responses import FileResponse

from config import UPLOADS_DIR
from ia import extraer_factura
from database import guardar_factura
from database import obtener_facturas


router = APIRouter()


@router.get("/")    
def inicio():
    return FileResponse("static/index.html") #En lugar de devolver un JSON, devuelve este archivo
    

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

#ENDPONT PARA OBTENER TODASS LAS FACTURAS QUE HA INGRESADO EL USUARIO
@router.get("/despensa")
def obtener_despensa():

    filas = obtener_facturas()

    productos = []

    for fila in filas:

        factura = json.loads(fila[0])

        if "productos" in factura:
            productos.extend(factura["productos"])

        elif "nombre_del_producto_con_su_precio" in factura:
            productos.extend(factura["nombre_del_producto_con_su_precio"]) # Solo agregamos esto por ahora, ya que esto hara que funcione porque lo que esta pasando es que la bd cuando se creo guardaba los productos asi, pero luego lo cambie a solo "productos"

    return {

        "productos": productos

    }    