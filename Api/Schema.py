from pydantic import BaseModel
"""
Schema do Json de input da Api
"""

class ClienteInput(BaseModel):
    cpf: str
    login: str
    senha: str
