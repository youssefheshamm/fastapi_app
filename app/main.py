from app.routers import tasks, utils
from fastapi import FastAPI
import os
from dotenv import load_dotenv
load_dotenv()


# Access environment variables
BASIC_AUTH_USERNAME = os.getenv("BASIC_AUTH_USERNAME")
BASIC_AUTH_PASSWORD_HASH = os.getenv("BASIC_AUTH_PASSWORD_HASH")


app = FastAPI()

app.include_router(tasks.router)
app.include_router(utils.router)
