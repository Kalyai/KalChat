from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.container import init_container
from src.settings import settings
from src.infra.repositories.tortoise.db import init_tortoise_orm
from src.api.auth.routes import router as auth_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_tortoise_orm()
    yield


def create_app() -> FastAPI:
    container = init_container()  # noqa: F841
    app = FastAPI(
        debug=settings.debug,
        lifespan=lifespan,
    )

    app.include_router(auth_router)
    return app
