from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.api.auth.routes import router as auth_router
from src.container import init_container
from src.settings import settings
from src.infra.repositories.tortoise.db import init_tortoise_orm


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_tortoise_orm()
    container = init_container()
    app.state.container = container

    yield


def create_app() -> FastAPI:
    app = FastAPI(
        debug=settings.debug,
        lifespan=lifespan,
    )

    app.include_router(auth_router)

    return app
