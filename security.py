from dotenv import load_dotenv
from jose import jwt, JWTError
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

import os
from datetime import datetime, timedelta, timezone
from database import get_user_by_email



load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))


#FUNCION PARA GENERAR EL TOKEN
def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update(
        {
            "exp": expire
        }
    )

    token = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token

#FUNCION PARA VERIFICAR EL TOKEN
def verify_token(token: str):

    try:
        #Decodificamos el string
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload

    except JWTError:

        return None    



# DEPENDENCIA PARA USAR EN LAS DIFERENTES RUTAS
security = HTTPBearer() #"Espero que el cliente me envíe un token en la cabecera Authorization: Bearer ...."

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    # 1. Extraemos el JWT de la cabecera Authorization
    token = credentials.credentials

    # 2. Verificamos el JWT
    payload = verify_token(token)

    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido"
        )

    # 3. Extraemos el email del payload
    email = payload["sub"]

    # 4. Buscamos el usuario en la base de datos
    user = get_user_by_email(email)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario no encontrado"
        )

    # 5. Devolvemos el usuario autenticado
    return user