"""Process entry points"""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Place After All Other Routes
app.mount("", StaticFiles(directory="client/dist/", html=True), name="static")
