from fastapi.testclient import TestClient
from api.router import app
import os

class TestRouter:
    def test_search_cpf(self):
        """Testa o fluxo de execução da api e da extração de benefício"""

        cliente = TestClient(app)
        numero_beneficio = cliente.post(
            "/search_cpf/",
            json={
                "cpf": '216.123.905-87',
                "login": os.environ.get('USERKONSI'),
                "senha": os.environ.get('SENHAKONSI'),
            },
        ).json()
        assert numero_beneficio == {"numero_do_beneficio": "1365628920"}
