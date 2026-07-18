from fastapi import APIRouter

from fastapi.responses import FileResponse

pages_router = APIRouter()

#--------------------- FRONT ---------------------
@pages_router.get("/")    
def index_page():
    return FileResponse("static/index.html") #En lugar de devolver un JSON, devuelve este archivo.

#ENDPOINT PARA IR A LA PAGINA PRINCIPAL DE LA APP (SUBIR FACTURA)
@pages_router.get("/app")
def application():
    return FileResponse("static/my_pantry.html")