from dataclasses import dataclass

from base import BaseAccountsRepo
from src.domain.auth.account import Account
from src.infra.repositories.tortoise.base import BaseTortoiseOrm
from src.infra.repositories.tortoise.models import AccountModel


@dataclass(kw_only=True)
class TortoiseAccountsRepo(BaseAccountsRepo, BaseTortoiseOrm):
    async def create(self, model: Account):
        try:
            account = await AccountModel.create(**model.to_orm())
        except Exception as e:
            ...

    async def get(self):
        ...

    async def get_all(self):
        ...
