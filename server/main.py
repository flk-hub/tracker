"""Process entry points."""
from logging import DEBUG, StreamHandler, getLogger
from sys import stdout
from fastapi import FastAPI
from server.models import create_db
from server.urls.users.routes import UsersRouter


# from fastapi.staticfiles import StaticFiles

create_db()


LOGGER = getLogger("tracker")
LOGGER.setLevel(DEBUG)
LOGGER.addHandler(StreamHandler(stdout))

app = FastAPI()
app.include_router(UsersRouter)

# Place After All Other Routes
# app.mount("", StaticFiles(directory="client/dist/", html=True), name="static")
