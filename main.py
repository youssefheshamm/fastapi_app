from fastapi import FASTAPI
from app.routers import utils, tasks

app = FASTAPI()

app.include_router(utils.router)
app.include_router(tasks.router)
