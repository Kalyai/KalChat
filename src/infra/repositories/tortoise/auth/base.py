from abc import abstractmethod
from dataclasses import dataclass

from src.domain.auth.account import Account
from src.infra.repositories.tortoise.base import BaseTortoiseOrm


@dataclass(kw_only=True)
class BaseAccountsRepo(BaseTortoiseOrm):
    @abstractmethod
    async def create(self, model: Account):
        ...

    @abstractmethod
    async def get(self, login: str):
        ...

    @abstractmethod
    async def get_all(self):
        ...

    @abstractmethod
    async def login_exsits(self, login: str):
        ...
