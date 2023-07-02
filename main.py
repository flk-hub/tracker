"""Process entry points."""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

data = [{"name": "ikl"}]


@app.get("/get_users")
def get_users():
    """Get users."""
    return data


# Place After All Other Routes
app.mount("", StaticFiles(directory="client/dist/", html=True), name="static")
