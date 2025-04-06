from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from src.api.auth.schemas import RegisterSchema
from src.container import Container
from src.services.auth.interfaces import BaseAccountService

router = APIRouter(tags=['AUTH'], prefix='/auth')

@router.post('')
@inject
async def register(
        schema: RegisterSchema,
        service: BaseAccountService = Depends(Provide[Container.account_service]),
):
    return await service.create_account(schema.login, schema.password)
