from fastapi import FastAPI
from app.routers import utils, tasks

app = FastAPI()

app.include_router(utils.router)
app.include_router(tasks.router)
