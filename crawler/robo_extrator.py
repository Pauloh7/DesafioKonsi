import time
import re
import requests
import sys
import logging
from crawler.selenium_util import (
    open_selenium,
    find_element_by_xpath_with_click,
    send_keys_by_name,
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

    def get_login_page(self):
        """Executa primeira requisicao ao site utilizando webdriver selenium"""

        time.sleep(1)
        try:
            self.browser.get(self.url_pagina_login)
        except Exception as e:
            logger.exception(e)
            raise

    def set_login_senha(self, login: str, senha: str):
        """Busca inputs de usuário e senha, os preenche e clica no botão para requisitar acesso

        Args:
            login (str): Usuário do requisitante
            senha(str): Senha do requisitante
        """

        time.sleep(1)
        send_keys_by_name(self.browser, "usuario", login)
        send_keys_by_name(self.browser, "senha", senha)
        find_element_by_xpath_with_click(self.browser, '//*[@id="botao"]')

    @retry(wait=wait_fixed(1), stop=stop_after_attempt(5))
    def get_beneficio(self, cpf: str, login: str, senha: str) -> str:
        """Executa extração do número de benefício

        Args:
            cpf (str): Cpf a ter benefício extraído
            login (str): Usuário do requisitante
            senha (str): Senha do requisitante

        Returns:
            numero_beneficio (str): Número do benefício extraído

        Raises:
        AttributeError: Erro causado por não haver benefício a ser extraído
        """

        numero_beneficio = None
        self.browser = open_selenium(
            path_selenium="./chromedriver"
            if "linux" in sys.platform
            else "./chromedriver.exe",
            headless=True,
        )
        try:
            self.get_login_page()
            self.set_login_senha(login, senha)

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
