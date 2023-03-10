from fastapi import FastAPI, HTTPException
from api import schema
from crawler.robo_extrator import RoboExtrator

app = FastAPI()


@app.post("/search_cpf/")
async def search_cpf(cliente: schema.ClienteInput) -> dict:
    """Parte da api que recebe o post com dados do cliente e executa chamada para extração dos benefícios

    Args:
        cliente (schema.ClienteInput): Json com dados do cliente

    Returns:
        resultado_dict (dict): Dicionário com número do benefício

    Raises:
        HTTPException: Erro de processamento na requisição
    """

    try:
        robo = RoboExtrator()
        if numero_beneficio := robo.extract_cpf_info(
            cliente.cpf, cliente.login, cliente.senha
        ):
            return {"numero_do_beneficio": numero_beneficio}

        return {"detalhes": "Não foram encontrados benefícios para o CPF informado."}

    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro ao processar a requisição.")
