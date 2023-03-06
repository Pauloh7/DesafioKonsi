from fastapi.testclient import TestClient
from api.router import app
import os

class TestRouter:
    def test_consulta_cpf(self):
        """Testa o fluxo de execução da api e da extração de benefício"""

        cliente = TestClient(app)
        numero_beneficio = cliente.post(
            "/consultacpf/",
            json={
                "cpf": os.environ.get('CPFKONSI'),
                "login": os.environ.get('USERKONSI'),
                "senha": os.environ.get('SENHAKONSI'),
            },
        ).json()
        assert numero_beneficio == {"numero_do_beneficio": "1365628920"}
