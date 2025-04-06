from dataclasses import dataclass

from src.domain.auth.common import BaseEntity

@dataclass(kw_only=True)
class Account(BaseEntity):
    id: int | None = None
    login: str
    password: str

    def to_orm(self):
        orm_model = {
            'login': self.login,
            'password': self.password,
        }

        if self.id:
            orm_model['id'] = self.id
        return orm_model
