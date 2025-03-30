from typing import Optional
from uuid import UUID, uuid4
from dataclasses import dataclass, field

from common import BaseEntity

@dataclass(kw_only=True)
class Users(BaseEntity):
    id: UUID = field(default_factory=uuid4)
    name: str
    password: str
    connected_users: Optional[list[UUID]] = None

    @classmethod
    def create(cls, name: str, password: str):
        ...

    @classmethod
    def get(cls, name: str):
        ...

