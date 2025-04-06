from dataclasses import dataclass

from src.domain.auth.account import Account
from src.services.auth.interfaces import BaseAccountService


@dataclass(kw_only=True)
class AccountService(BaseAccountService):
    async def create_account(self, login: str, password: str):
        if len(login) > 64:
            return {'status': 'error'}

        account_info = Account(login=login, password=password)
        account = await self.accounts.create(account_info)
        return account