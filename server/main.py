from fastapi import FastAPI
from server.models import create_db
from server.routes import Router
from server.utils import get_logger_to_file


# from fastapi.staticfiles import StaticFiles
LOGGER = get_logger_to_file(__name__, f"{__name__}.log")


LOGGER.info("Setting the database...")
create_db()
LOGGER.info("Database setup complete.")


app = FastAPI()
app.include_router(Router)

# Place After All Other Routes
# app.mount("", StaticFiles(directory="client/dist/", html=True), name="static")
