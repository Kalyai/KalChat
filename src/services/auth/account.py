from dataclasses import dataclass

from src.domain.auth.account import Account
from src.services.auth.interfaces import BaseAccountService


@dataclass(kw_only=True)
class AccountService(BaseAccountService):
    async def create_account(self, login: str, password: str):
        if len(login) > 64:
            raise ValueError('login must be less than 64 characters')
        if await self.accounts.login_exsits(login):
            raise ValueError('login is already taken')

        account_info = Account(login=login, password=password)
        account = await self.accounts.create(account_info)
        return account

    async def authenticate_account(self, login: str, password: str):
        if not await self.accounts.login_exsits(login):
            raise ValueError('Not valid login or password')



