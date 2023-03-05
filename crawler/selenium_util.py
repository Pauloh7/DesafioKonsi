import time
import logging
from seleniumwire import webdriver
from selenium.webdriver.common.by import By


logger = logging.getLogger()


def abre_selenium(
    path_selenium: str,
    headless: bool = False,
) -> webdriver.Chrome:
    """Executa o selenium e abre uma instancia de navegador

    Args:
        path_selenium (str): Caminho do chromedriver
        headless (bolean): Determina se o selenium abre ou nao uma janela quando executado

    returns:
        browser (webdriver.Chrome): Objeto webdriver  (janela do navegador)
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
        time.sleep(1)

    except Exception as e:
        logger.exception(e)
        raise

    return browser


def encontra_elemento_por_xpath_com_click(
    browser: webdriver.Chrome, element_xpath: str
):
    """Simula clique do mouse em elemento da pagina com selenium

    Args:
        browser (webdriver.Chrome): Objeto webdriver (janela do navegador)
        element_xpath (str): Xpath do elemento que se deseja o clique
    """

    browser.find_element(By.XPATH, element_xpath).click()
    time.sleep(1)


def envia_chaves_por_nome(browser: webdriver.Chrome, element_name: str, value: str):
    """Encontra elemento, envia e preenche com valor

    Args:
        browser (webdriver.Chrome): Objeto webdriver  (janela do navegador)
        element_name (str): Nome do elemento a ser encontrado
        value (str): Valor que deve preencher o elemento
    """

    browser.find_element(By.NAME, element_name).send_keys(value)
    time.sleep(1)
