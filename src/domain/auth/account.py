from dataclasses import dataclass

from src.domain.auth.common import BaseEntity

@dataclass(kw_only=True)
class Account(BaseEntity):
    id: int | None = None
    login: str
    password: str

    def to_orm(self):
        return {
            'login': self.login,
            'password': self.password,
        }
