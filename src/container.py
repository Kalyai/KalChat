from functools import lru_cache

from dependency_injector import containers, providers

from src.infra.repositories.tortoise.auth.accounts import TortoiseAccountsRepo
from src.services.auth.account import AccountService


@lru_cache(1)
def init_container():
    container = Container()
    container.wire(modules=['src.api.auth.routes'])
    return container


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            'src.api.auth.routes',
        ]
    )

    accounts = providers.Factory(TortoiseAccountsRepo)

    account_service = providers.Factory(
        AccountService,
        accounts=accounts
    )
