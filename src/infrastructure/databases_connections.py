from tortoise import Tortoise

from src.settings import settings

async def tortoise_connection():
    config = {
        "connections": {
            "default": {
                "engine": "tortoise.backends.asyncpg",
                "credentials": settings.make_pg_cred,
                "echo": True,
            }
        },
        "apps": {
            "models": {
                "models": [
                    "src.infrastructure.models",
                ],
                "default_connection": "default",
            }
        },
        "use_tz": False,
        "timezone": "Europe/Moscow",
    }

    await Tortoise.init(config=config)
