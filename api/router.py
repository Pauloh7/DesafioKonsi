from fastapi import FastAPI,HTTPException
from api import schema
from crawler.robo_extrator import RoboExtrator


app = FastAPI()
@app.post("/consultacpf/")
async def consulta_cpf(cliente: schema.ClienteInput):
    """Parte da api que recebe o post com dados do cliente e executa chamada para extracao dos beneficios

    Args:
        cliente (schema.ClienteInput): json com dados do cliente

    Returns:
        resultado_dict (dict): dicionario com numero do beneficio
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