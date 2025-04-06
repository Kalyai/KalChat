from pydantic import BaseModel

class RegisterSchema(BaseModel):
    login: str
    password: str