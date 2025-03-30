from fastapi import APIRouter

router = APIRouter(tags=["auth"])

@router.get("/login")
async def login():
    ...

@router.post("/registration")
async def registration():
    ...
