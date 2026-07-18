from fastapi import APIRouter
import json
from fastapi import Depends, HTTPException, status

from database.database import get_ticket
from security import get_current_user

pantry_router = APIRouter()

#ENDPONT PARA OBTENER TODAS LAS FACTURAS QUE HA INGRESADO EL USUARIO.
@pantry_router.get("/despensa") #back
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