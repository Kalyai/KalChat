from functools import cached_property

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool = False
    PG_CRED: str

    @cached_property
    def make_pg_cred(self):
        PG_HOST, PG_PORT, PG_DATABASE, PG_USER, PG_PASSWORD = self.PG_CRED.split(':')  # noqa
        return {
            'host': PG_HOST,
            'port': int(PG_PORT),
            'database': PG_DATABASE,
            'user': PG_USER,
            'password': PG_PASSWORD,
        }

    class Config:
        env_file = ".env"


settings = Settings()  # noqa
