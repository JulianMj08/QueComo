# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def inicio():
#     return {"mensaje": "Hola Mundo, de nuevo"}

from fastapi import FastAPI
from routes import router

app = FastAPI()

app.include_router(router)