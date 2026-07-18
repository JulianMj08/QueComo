from fastapi import APIRouter

import json
from fastapi.responses import FileResponse

from models.schemas import RegisterUser
from models.schemas import LoginUser
from database.database import create_user
from database.database import login_user
from security import create_access_token

auth_router = APIRouter()
#--------------------- BACK ---------------------
#ENDPONT PARA ENVIAR LA CREACION NUEVO USUARIO.  
@auth_router.post("/registro")
def new_user_registered(user: RegisterUser):

    create_user(
        user.name,
        user.email,
        user.password
    )

    access_token = create_access_token({
        "sub": user.email    
})
    return {
        "message": "Usuario creado correctamente",

         "success": True,

        "token": access_token, #El backend le va a devolver el token a register.js
    }

@auth_router.post("/login")
def login(user: LoginUser):

    print("Entró al endpoint login")
    print(user)

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

#--------------------- FRONT ---------------------

#ENDPONT PARA MOSTRAR LA PANTALLA DE CREACION DE USUARIO.
@auth_router.get("/registro")
def register_page():
    return FileResponse("static/register.html")    

#ENDPONT PARA MOSTRAR LA PANTALLA DE LOGIN DE USUARIO.
@auth_router.get("/login")
def login_page():
    return FileResponse("static/login.html")    

