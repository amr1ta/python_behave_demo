from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from site_pom.base import Page


def before_all(context):
    browser = context.config.userdata['browser']
    if browser == "chrome":
        context.driver = Page(webdriver.Chrome(
            ChromeDriverManager().install()))
    context.homepage_url = context.config.userdata['homepage_url']
    
def after_all(context):
    context.driver.quit()
