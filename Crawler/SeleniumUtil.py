import time

from seleniumwire import webdriver
from selenium.webdriver.common.by import By
import logging

logger = logging.getLogger()
def abre_selenium(
    path_selenium,
    headless=False,
):
    """
    Executa o selenium e abre uma instancia de navegador
    param:
        path_selenium(str): caminho do chromedriver
        headless(bolean): determina se o selenium abre ou nao uma janela quando executado
    return:
        browser(seleniumwire.webdriver.Chrome): objeto seleniumwire (janela do navegador)
    """
    browser = None

    try:
        chrome_options = webdriver.ChromeOptions()

        if headless:
            chrome_options.add_argument("enable-automation")
            chrome_options.add_argument("--disable-infobars")
            chrome_options.add_argument("--disable-browser-side-navigation")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--incognito")

        browser = webdriver.Chrome(
            chrome_options=chrome_options, executable_path=path_selenium
        )
        time.sleep (1)


    except Exception as e:
        logger.exception(e)
        raise

    return browser


def encontra_elemento_por_xpath_com_click(browser, element_xpath):
    """
    Simula clique do mouse em elemento da pagina com selenium
    param:
        browser(seleniumwire.webdriver.Chrome): objeto seleniumwire (janela do navegador)
        element_xpath: xpath do elemento que se deseja o clique
    """
    browser.find_element(By.XPATH, element_xpath).click()
    time.sleep(1)


def envia_chaves_por_nome(browser, element_name, value):
    """
    encontra
    param:
        browser:
        element_name:
        value:
    """
    browser.find_element(By.NAME, element_name).send_keys(value)
    time.sleep(1)
