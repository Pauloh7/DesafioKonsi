from pydantic import BaseModel


class Cliente(BaseModel):
    cpf: str
    login: str
    senha: str
