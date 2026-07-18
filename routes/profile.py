from fastapi import APIRouter
from fastapi.responses import FileResponse
from fastapi import Depends, HTTPException, status

from security import get_current_user

profile_router = APIRouter()
#--------------------- BACK ---------------------
#ENDPONT PARA AUTORIZAR Y DEVOLVER DATOS DEL USUARIO A FETCH /perfil.
@profile_router.get("/api/perfil")
def profile(current_user = Depends(get_current_user)):

    return {
        "id": current_user["id"],
        "name": current_user["name"],
        "email": current_user["email"]
    } 

#--------------------- FRONT ---------------------
#ENDPONT PARA MOSTRAR LA PANTALLA DE PERFIL DE USUARIO.
@profile_router.get("/perfil") #front
def profile_page():
    return FileResponse("static/profile.html")