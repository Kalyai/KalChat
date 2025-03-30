from fastapi import FastAPI
from contextlib import asynccontextmanager
from infrastructure.databases_connections import tortoise_connection
from src.settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    await tortoise_connection()

    yield


def create_app() -> FastAPI:
    app = FastAPI(
        debug=settings.DEBUG,
        lifespan=lifespan,
    )

    # app.include_router(router)

    return app