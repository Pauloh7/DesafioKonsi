from pydantic import BaseModel


class ClienteInput(BaseModel):
    cpf: str
    login: str
    senha: str
