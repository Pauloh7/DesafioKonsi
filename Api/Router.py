from fastapi import FastAPI,HTTPException
from Api import Schema
from Crawler.RoboExtrator import RoboExtrator


app = FastAPI()
@app.post("/consultacpf/")
async def create_item(cliente: Schema.ClienteInput):
    try:
        robo = RoboExtrator()
        numero_beneficio = robo.extrai_beneficio(cliente.cpf, cliente.login, cliente.senha)
        resultado_dict = {"numero_do_beneficio": numero_beneficio}
        return resultado_dict
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail='Erro ao processar a requisição.')