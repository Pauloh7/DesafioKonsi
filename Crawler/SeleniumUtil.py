import time

from seleniumwire import webdriver
from selenium.webdriver.common.by import By
import logging


def open_selenium(
    path_selenium,
    headless=False,
):
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
        logger = logging.getLogger()
        logger.exception(e)
        pass

    return browser


def find_element_by_xpath_with_click(browser, element_xpath):
    browser.find_element(By.XPATH, element_xpath).click()
    time.sleep(1)


def send_keys_by_name(browser, element_xpath, value):
    browser.find_element(By.NAME, element_xpath).send_keys(value)
    time.sleep(1)
