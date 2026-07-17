from pydantic import BaseModel, EmailStr # con estas librerias validará automáticamente: no falten campos, email tenga un formato válido, el cuerpo de la petición sea correcto. 


class RegisterUser(BaseModel):

    name: str

    email: EmailStr 

    password: str

class LoginUser(BaseModel):

    email: EmailStr

    password: str    