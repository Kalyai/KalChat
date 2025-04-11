from dataclasses import dataclass

from src.infra.repositories.base import BaseOrmRepo


@dataclass(kw_only=True)
class BaseTortoiseOrm(BaseOrmRepo):
    ...
