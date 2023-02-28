import requests, re
import time
import sys
from SeleniumUtil import *

class RoboExtrator():
    def __init__(self):
        self.browser = None
        self.login = 'testekonsi'
        self.senha = 'testekonsi'
        self.urlconsulta = 'http://extratoblubeapp-env.eba-mvegshhd.sa-east-1.elasticbeanstalk.com/offline/listagem/074.687.335-20'
        self.url_login = "http://extratoblubeapp-env.eba-mvegshhd.sa-east-1.elasticbeanstalk.com/login"
        # self.parampost = {"login": self.login,
        #             "senha": self.senha
        #             }
        self.headers = {"Host": "extratoblubeapp-env.eba-mvegshhd.sa-east-1.elasticbeanstalk.com",
                   "User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
                   "Accept": 'application/json,text/plain, */* ',
                   "Accept-Language": "pt-BR,pt;q=0.8,en-US;q = 0.5,en;q=0.3",
                   "Accept-Encoding": "utf-8",
                   "Content-Type": "application/json",
                   "Content-Length": "43",
                   "Origin": "http://ionic-application.s3-website-sa-east-1.amazonaws.com",
                   "Connection": "keep-alive",
                   "Referer": "http://ionic-application.s3-website-sa-east-1.amazonaws.com/"
                   }


    def extrai_lista_cpf(self,cpf_list):
        self.browser = open_selenium(
            path_selenium='./chromedriver' if 'linux' in sys.platform else './chromedriver.exe', headless=True
        )

        if not self.browser:
            self.browser = open_selenium(
                path_selenium='../chromedriver' if 'linux' in sys.platform else '../chromedriver.exe', headless=True
            )

        self.faz_requisicao()
        self.insere_login_senha(self.login,self.senha)

    def faz_requisicao(self):

        tentativas = 5
        conseguiu = False

        while tentativas >= 0 and not conseguiu:
            try:
                self.browser.get(self.url_login)
                conseguiu = True

            except Exception as e:
                print(e)
                tentativas -= 1

    def insere_login_senha(self, usuario, senha):
#todo continuar a partir daqui pegar xpath do login do site
        time.sleep(2)
        send_keys_by_xpath(self.browser, '//*[@id="usernameForm"]', '01105013731' if usuario is None else usuario)
        send_keys_by_xpath(self.browser, '//*[@id="passwordForm"]', 'Ruthemi123!' if senha is None else senha)
        find_element_by_xpath_with_click(self.browser, '//*[@id="pbEntrar"]')


if __name__ == '__main__':

    robo = RoboExtrator()
    resultado = robo.extrai_lista_cpf()



