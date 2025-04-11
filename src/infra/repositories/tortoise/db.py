from tortoise import Tortoise  # noqa

from src.settings import settings

async def init_tortoise_orm() -> None:
    config = {
        'connections': {
            'default': {
                'engine': 'tortoise.backends.asyncpg',
                'credentials': settings.make_pg_conn_creds(),
            }
        },
        'apps': {
            'models': {
                'models': ['src.infra.repositories.tortoise.models'],
                'default_connection': 'default',
            }
        },
        'use_tz': False,
        'timezone': 'Europe/Moscow',
    }

    await Tortoise.init(config=config)
