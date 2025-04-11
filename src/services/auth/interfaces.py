from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.infra.repositories.tortoise.auth.base import BaseAccountsRepo


@dataclass(kw_only=True)
class BaseAccountService(ABC):
    accounts: BaseAccountsRepo

    @abstractmethod
    async def create_account(self, login: str, password: str):
        ...
