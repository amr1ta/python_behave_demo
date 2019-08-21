from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# this Base class is serving basic attributes for every single page inherited from Page class

class Page(object):
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30
        self.driver_wait = WebDriverWait(self.driver, self.timeout)
 
    def find_element(self, *locator):
        # return self.driver.find_element(*locator)
        return self.driver_wait.until(EC.visibility_of_element_located(locator))
        
    def find_elements(self, *locator):
         return self.driver.find_elements(*locator)
        
    def open(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        
    def get_title(self):
        return self.driver.title
        
    def get_url(self):
        return self.driver.current_url
        
    def select_by_text(self, select, text):
        s = Select(self.driver.find_element(*select))
        return s.select_by_visible_text(text)

    def move_to_element(self, locator):
        el = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        return actions.move_to_element(el).click(el).perform()

    def find_by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def finds_by_xpath(self, xpath):
        return self.driver.find_elements_by_xpath(xpath)

    def quit(self):
        return self.driver.quit()
