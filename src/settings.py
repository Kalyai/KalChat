from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    debug: bool = False
    PG_CRED: str

    def make_pg_conn_creds(self):
        creds = self.PG_CRED.split(':')
        return {
            'host': creds[0],
            'port': creds[1],
            'database': creds[2],
            'user': creds[3],
            'password': creds[4]
        }


settings = Settings()
