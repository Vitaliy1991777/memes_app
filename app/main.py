from fastapi import FastAPI
from .api.v1 import memes
from .dependencies import get_db

app = FastAPI()

app.include_router(memes.router, prefix="/memes", tags=["memes"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Memes API"}
