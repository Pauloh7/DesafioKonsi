import sys
import seleniumwire.webdriver
from seleniumwire import webdriver
from Crawler.SeleniumUtil import abre_selenium

class TestSeleniumUtil:
    def test_abre_selenium(self):
        """
        Testa modulo que abre uma instancia de selenium
        """
        browser_teste = abre_selenium(path_selenium="./chromedriver"
            if "linux" in sys.platform
            else "./chromedriver.exe",
                                      headless=True,
                                      )

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("enable-automation")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-browser-side-navigation")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--incognito")

        assert type(browser_teste) is type(seleniumwire.webdriver.Chrome(chrome_options=chrome_options))
