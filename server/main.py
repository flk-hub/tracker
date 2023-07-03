"""Process entry points."""
from fastapi import FastAPI

from server.databases.system import create_db
from server.services.users.routes import UsersRouter

# from fastapi.staticfiles import StaticFiles


create_db()

app = FastAPI()
app.include_router(UsersRouter)

# Place After All Other Routes
# app.mount("", StaticFiles(directory="client/dist/", html=True), name="static")
