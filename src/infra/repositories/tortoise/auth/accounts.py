from dataclasses import dataclass

from tortoise.exceptions import MultipleObjectsReturned, DoesNotExist

from src.infra.repositories.tortoise.auth.base import BaseAccountsRepo
from src.domain.auth.account import Account
from src.infra.repositories.tortoise.base import BaseTortoiseOrm
from src.infra.repositories.tortoise.models import AccountModel


@dataclass(kw_only=True)
class TortoiseAccountsRepo(BaseAccountsRepo, BaseTortoiseOrm):
    async def create(self, model: Account) -> None:
        try:
            account = await AccountModel.create(**model.to_orm())
        except Exception as e:
            ...

    async def get(self, login: str) -> AccountModel | None:
        try:
            account = await AccountModel.get(login=login)
            return account
        except MultipleObjectsReturned as e:
            ...
        except DoesNotExist as e:
            ...
        except Exception as e:
            ...

    async def get_all(self):
        ...

    async def login_exsits(self, login: str) -> bool:
        return await AccountModel.exists(login=login)
