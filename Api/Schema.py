from pydantic import BaseModel


class ClienteInput(BaseModel):
    """Schema do Json de input da Api
    """

    cpf: str
    login: str
    senha: str
