from fastapi import FastAPI,HTTPException
from Api import Schema
from Crawler.RoboExtrator import RoboExtrator


app = FastAPI()
@app.post("/consultacpf/")
async def consulta_cpf(cliente: Schema.ClienteInput):
    """
    Parte da Api que recebe o post com dados do cliente e executa chamada
    para extracao dos beneficios
    param:
        cliente(Schema.ClienteInput):json com dados do cliente
    return:
        resultado_dict(dict):dicionario com numero do beneficio
    """
    try:
        robo = RoboExtrator()
        numero_beneficio = robo.extrai_beneficio(cliente.cpf, cliente.login, cliente.senha)
        resultado_dict = {"numero_do_beneficio": numero_beneficio}
        return resultado_dict
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail='Erro ao processar a requisição.')