from fastapi import FastAPI
import schema
from RoboExtrator import RoboExtrator

app = FastAPI()
@app.post("/requisicao/")
async def create_item(cliente: schema.Cliente):
    robo = RoboExtrator()
    numero_beneficio = robo.extrai_lista_cpf(cliente.cpf,cliente.senha,cliente.login)
    resultado_dict = {"numero_do_beneficio":numero_beneficio}
    return resultado_dict