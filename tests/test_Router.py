from fastapi.testclient import TestClient
from api.Router import app
class TestRoboExtrator:

    def test_consulta_cpf(self):
        cliente = TestClient(app)
        numero_beneficio = cliente.post(
            "/consultacpf/",
            json={"cpf": "216.123.905-87", "login": "testekonsi", "senha": "testekonsi"},
        ).json()
        assert numero_beneficio == {'numero_do_beneficio': '1365628920'}