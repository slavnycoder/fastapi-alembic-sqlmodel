from fastapi import FastAPI

from app.db import init_db
from app.models import *

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await init_db()


@app.get("/health")
async def root():
    return {}


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
