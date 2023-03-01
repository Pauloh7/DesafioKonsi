import requests, re
import sys
from SeleniumUtil import *

class RoboExtrator():
    def __init__(self):
        self.browser = None
        self.login = 'testekonsi'
        self.senha = 'testekonsi'
        self.urlconsulta = 'http://extratoblubeapp-env.eba-mvegshhd.sa-east-1.elasticbeanstalk.com/offline/listagem/074.687.335-20'
        self.url_pagina_login ="http://ionic-application.s3-website-sa-east-1.amazonaws.com/"
        self.headers = None


    def extrai_lista_cpf(self,cpf_list):
        self.browser = open_selenium(
            path_selenium='./chromedriver' if 'linux' in sys.platform else './chromedriver.exe', headless=False
        )

        if not self.browser:
            self.browser = open_selenium(
                path_selenium='../chromedriver' if 'linux' in sys.platform else '../chromedriver.exe', headless=True
            )

        tentativas = 5
        conseguiu = False

        while tentativas >= 0 and not conseguiu:
            try:
                self.faz_requisicao()
                self.insere_login_senha(self.login,self.senha)


                s = requests.session()
                if self.browser.requests[74].url == "http://extratoblubeapp-env.eba-mvegshhd.sa-east-1.elasticbeanstalk.com/usuario/logado":
                    request = self.browser.requests[74]
                elif self.browser.requests[78].url == "http://extratoblubeapp-env.eba-mvegshhd.sa-east-1.elasticbeanstalk.com/usuario/logado":
                    request = self.browser.requests[78]
                self.headers = request.headers
                for cpf in cpf_list:
                    resultado_beneficio_cpf = s.get(f"http://extratoblubeapp-env.eba-mvegshhd.sa-east-1.elasticbeanstalk.com/offline/listagem/{cpf}",headers=self.headers)
                    numero_beneficio = re.search('(\"nb\":)(\"\d+\")',str(resultado_beneficio_cpf.content)).group(2).replace("\"","")
                print(resultado_beneficio_cpf.content)
            except Exception as e:
                print(e)
                tentativas -= 1

    def faz_requisicao(self):
        time.sleep(1)
        tentativas = 5
        conseguiu = False

        while tentativas >= 0 and not conseguiu:
            try:
                self.browser.get(self.url_pagina_login)
                conseguiu = True

            except Exception as e:
                print(e)
                tentativas -= 1

    def insere_login_senha(self, usuario, senha):
        time.sleep(1)
        send_keys_by_name(self.browser, 'usuario', usuario)
        send_keys_by_name(self.browser, 'senha', senha)
        find_element_by_xpath_with_click(self.browser, '//*[@id="botao"]')


if __name__ == '__main__':
    cpf_list = ["074.687.335-20",
"216.123.905-87",
"183.235.105-04",
"112.199.985-91",
"478.130.405-20",
"259.936.315-20",
"044.284.555-34",
"126.115.815-68",
"095.310.845-72",
"162.964.945-72"]
    robo = RoboExtrator()
    resultado = robo.extrai_lista_cpf(cpf_list)



