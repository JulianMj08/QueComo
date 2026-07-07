from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routes import router
from database import crear_base_datos   

crear_base_datos()

app = FastAPI()

app.include_router(router)

app.mount("/static", StaticFiles(directory="static"), name="static") # servir archivos statics