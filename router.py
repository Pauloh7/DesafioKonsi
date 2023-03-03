from urllib.error import HTTPError
from fastapi import FastAPI
from api import schema
from Crawler.RoboExtrator import RoboExtrator

app = FastAPI()
@app.post("/requisicao/")
async def create_item(cliente: schema.ClienteInput):
    try:
        robo = RoboExtrator()
        numero_beneficio = robo.extrai_lista_cpf(cliente.cpf, cliente.login, cliente.senha)
        resultado_dict = {"numero_do_beneficio": numero_beneficio}
        return resultado_dict
    except Exception as e:
        raise HTTPError(e)