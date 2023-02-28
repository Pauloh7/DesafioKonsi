from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

import time

def open_selenium(path_selenium, headless=False, options=None, minimize_window=False, path_download_file=None):

    browser = None

    try:
        chrome_options = webdriver.ChromeOptions()

        if headless:
            chrome_options.add_argument("enable-automation")
            chrome_options.add_argument("--disable-infobars")
            chrome_options.add_argument("--disable-browser-side-navigation")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--incognito')

        browser = webdriver.Chrome (chrome_options=chrome_options, executable_path=path_selenium) # path sempre contendo o .exe no windows
        time.sleep (2)

        if not headless and minimize_window:
            browser.minimize_window ()

    except Exception as e:
        pass

    return browser

def find_element_by_xpath_with_click(browser, element_xpath):

    browser.find_element(By.XPATH, element_xpath).click()
    time.sleep(1)

def send_keys_by_xpath(browser, element_xpath, value):
    browser.find_element(By.XPATH, element_xpath).send_keys(value)
    time.sleep(1)
