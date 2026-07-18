from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routes.auth import auth_router
from routes.profile import profile_router
from routes.tickets import tickets_router
from routes.pantry import pantry_router
from routes.pages import pages_router


from database.database import create_db

create_db()

app = FastAPI()

app.include_router(auth_router)
app.include_router(profile_router)
app.include_router(tickets_router)
app.include_router(pantry_router)
app.include_router(pages_router)

app.mount("/static", StaticFiles(directory="static"), name="static") # servir archivos statics