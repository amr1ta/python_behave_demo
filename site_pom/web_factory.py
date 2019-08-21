from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from site_pom.base import Page


def get_browser_context(browser):
    if browser == "chrome":
        return Page(webdriver.Chrome(ChromeDriverManager().install()))