import time
import re
import requests
import sys
from Crawler.SeleniumUtil import (
    open_selenium,
    find_element_by_xpath_with_click,
    send_keys_by_name,
)
from tenacity import retry, wait_fixed, stop_after_attempt
import logging

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
        time.sleep(1)
        try:
            self.browser.get(self.url_pagina_login)
        except Exception as e:
            logger.exception(e)
            raise

    def insere_login_senha(self, usuario, senha):
        time.sleep(1)
        send_keys_by_name(self.browser, "usuario", usuario)
        send_keys_by_name(self.browser, "senha", senha)
        find_element_by_xpath_with_click(self.browser, '//*[@id="botao"]')

    @retry(wait=wait_fixed(1), stop=stop_after_attempt(5))
    def extrai_beneficio(self, cpf, login, senha):
        self.browser = open_selenium(
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
        except Exception as e:
            logger.exception(e)
            raise
        return numero_beneficio