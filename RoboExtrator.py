import time
import re
import requests
import sys
from SeleniumUtil import (
    open_selenium,
    find_element_by_xpath_with_click,
    send_keys_by_name,
)
from tenacity import retry, wait_fixed, stop_after_attempt
import logging


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
        self.logger = logging.getLogger()

    @retry(wait=wait_fixed(1), stop=stop_after_attempt(5))
    def extrai_lista_cpf(self, cpf_list,login,senha):
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
            for cpf in cpf_list:
                resultado_beneficio_cpf = s.get(
                    f"{self.urlconsulta}/offline/listagem/{cpf}", headers=self.headers
                )
                numero_beneficio = (
                    re.search('("nb":)("\d+")', str(resultado_beneficio_cpf.content))
                    .group(2)
                    .replace('"', "")
                )
                print(numero_beneficio)
        except Exception as e:
            self.logger.exception(e)
            raise

    def faz_requisicao(self):
        time.sleep(1)
        try:
            self.browser.get(self.url_pagina_login)
        except Exception as e:
            self.logger.exception(e)
            raise

    def insere_login_senha(self, usuario, senha):
        time.sleep(1)
        send_keys_by_name(self.browser, "usuario", usuario)
        send_keys_by_name(self.browser, "senha", senha)
        find_element_by_xpath_with_click(self.browser, '//*[@id="botao"]')


if __name__ == "__main__":
    cpf_list = [
        "074.687.335-20",
        "216.123.905-87",
        "183.235.105-04",
        "112.199.985-91",
        "478.130.405-20",
        "259.936.315-20",
        "044.284.555-34",
        "126.115.815-68",
        "095.310.845-72",
        "162.964.945-72",
    ]
    robo = RoboExtrator()
    resultado = robo.extrai_lista_cpf(cpf_list,"testekonsi","testekonsi")
