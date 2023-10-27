import logging
from time import sleep

from fastapi import FastAPI
from tortoise import Tortoise

from src.epona.auth import routers as auth
from src.epona.pessoas import routers as pessoas

from .config import get_settings, Settings
from .routes import ping
from .db import init_db

log = logging.getLogger("uvicorn")
settings: Settings = get_settings()


def create_application() -> FastAPI:
    application = FastAPI(name="api-core")

    application.include_router(auth.router, prefix="/auth", tags=["auth"])
    application.include_router(pessoas.router, prefix="/pessoas", tags=["pessoas"])
    application.include_router(ping.router, prefix="/ping", tags=["ping"])

    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    sleep(15)
    Tortoise.init_models([
        "src.epona.auth.models",
        "src.epona.pessoas.models"
    ], "models")
    init_db(app)
    log.info("Initialization finished")


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
