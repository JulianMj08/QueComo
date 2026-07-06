from fastapi import FastAPI
from routes import router
from database import crear_base_datos   

crear_base_datos()

app = FastAPI()

app.include_router(router)