from fastapi import APIRouter, UploadFile, File
from pathlib import Path
import shutil
import json
from fastapi.responses import FileResponse
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from config import UPLOADS_DIR
from ia import extract_ticket
from database import save_ticket
from database import get_ticket
from schemas import RegisterUser
from schemas import LoginUser
from database import create_user
from database import login_user
from security import create_access_token
from security import get_current_user



router = APIRouter()


@router.get("/")    
def index_page():
    return FileResponse("static/register.html") #En lugar de devolver un JSON, devuelve este archivo.

#ENDPOINT PARA IR A LA PAGINA PRINCIPAL DE LA APP (SUBIR FACTURA)
@router.get("/app")
def application():

    return FileResponse("static/index.html")    
    
# ENDPONT PARA ENVIAR TICKETS A LA BASE DE DATOS.
@router.post("/facturas")
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

#ENDPONT PARA OBTENER TODAS LAS FACTURAS QUE HA INGRESADO EL USUARIO.
@router.get("/despensa")
def get_pantry(current_user = Depends(get_current_user)):

    rows = get_ticket(current_user["id"])

    productos = []

    for row in rows:

        ticket = json.loads(row[0])

        if "productos" in ticket:
            productos.extend(ticket["productos"])

        elif "nombre_del_producto_con_su_precio" in ticket:
            productos.extend(ticket["nombre_del_producto_con_su_precio"]) # Solo agregamos esto por ahora, ya que esto hara que funcione porque lo que esta pasando es que la bd cuando se creo guardaba los productos asi, pero luego lo cambie a solo "productos"

    return {

        "productos": productos

    }   
    
#ENDPONT PARA ENVIAR LA CREACION NUEVO USUARIO.  
@router.post("/registro")
def new_user_registered(user: RegisterUser):

    create_user(
        user.name,
        user.email,
        user.password
    )

    return {
        "message": "Usuario creado correctamente"
    }

#ENDPONT PARA MOSTRAR LA PANTALLA DE CREACION DE USUARIO.
@router.get("/registro")
def register_page():
    return FileResponse("static/register.html")    

#ENDPONT PARA MOSTRAR LA PANTALLA DE LOGIN DE USUARIO.
@router.get("/login")
def login_page():

    return FileResponse("static/login.html")    

@router.post("/login")
def login(user: LoginUser):

    user = login_user(
        user.email,
        user.password
    )

    if user is None:

        return {

            "success": False,

            "message": "Credenciales incorrectas"

        }

    access_token = create_access_token({
        "sub": user["email"]    
})

    return {

        "success": True,

        "message": "Bienvenido",

        "token": access_token,

    }    

#ENDPONT PARA MOSTRAR LA PANTALLA DE PERFIL DE USUARIO.
@router.get("/perfil")
def profile_page():
    return FileResponse("static/profile.html")



@router.get("/api/perfil")
def profile(current_user = Depends(get_current_user)):

    return {
        "id": current_user["id"],
        "name": current_user["name"],
        "email": current_user["email"]
    }  