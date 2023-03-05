import time
import re
import requests
import sys
import logging
from crawler.selenium_util import (
    abre_selenium,
    encontra_elemento_por_xpath_com_click,
    envia_chaves_por_nome,
)
from tenacity import (
    retry,
    wait_fixed,
    stop_after_attempt,
)


logger = logging.getLogger()


class RoboExtrator:
    def __init__(self):
        self.browser = None
        self.urlconsulta = (
            "http://extratoblubeapp-env.eba-mvegshhd.sa-east-1.elasticbeanstalk.com"
        )
        self.url_pagina_login = (
            "http://ionic-application.s3-website-sa-east-1.amazonaws.com/"
        )
        self.headers = None

    def faz_requisicao(self):
        """Executa primeira requisicao ao site utilizando webdriver selenium"""

        time.sleep(1)
        try:
            self.browser.get(self.url_pagina_login)
        except Exception as e:
            logger.exception(e)
            raise

    def insere_login_senha(self, login: str, senha: str):
        """Busca inputs de usuario e senha, os preenche e clica no botão para requisitar acesso

        Args:
            login (str): Usuário do requisitante
            senha(str): Senha do requisitante
        """

        time.sleep(1)
        envia_chaves_por_nome(self.browser, "usuario", login)
        envia_chaves_por_nome(self.browser, "senha", senha)
        encontra_elemento_por_xpath_com_click(self.browser, '//*[@id="botao"]')

    @retry(wait=wait_fixed(1), stop=stop_after_attempt(5))
    def extrai_beneficio(self, cpf: str, login: str, senha: str) -> str:
        """Executa extração do numero de beneficio

        Args:
            cpf (str): Cpf a ter beneficio extraido
            login (str): Usuário do requisitante
            senha (str): Senha do requisitante

        Returns:
            numero_beneficio (str): Número do beneficio extraido

        Raises:
        AttributeError: Erro causado por não haver benefício a ser extraido
        """

        numero_beneficio = None
        self.browser = abre_selenium(
            path_selenium="./chromedriver"
            if "linux" in sys.platform
            else "./chromedriver.exe",
            headless=True,
        )
        try:
            self.faz_requisicao()
            self.insere_login_senha(login, senha)

            s = requests.session()
            time.sleep(1)
            request = [
                request
                for request in self.browser.requests
                if request.url == f"{self.urlconsulta}/usuario/logado"
            ]
            self.headers = request[0].headers
            resultado_beneficio_cpf = s.get(
                f"{self.urlconsulta}/offline/listagem/{cpf}", headers=self.headers
            )
            numero_beneficio = (
                re.search(r'("nb":)("\d+")', str(resultado_beneficio_cpf.content))
                .group(2)
                .replace('"', "")
            )
        except AttributeError as e:
            return numero_beneficio
        except Exception as e:
            logger.exception(e)
            raise
        return numero_beneficio
