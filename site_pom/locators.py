from selenium.webdriver.common.by import By

class MainPageLocators(object):
  BTN_ACCEPT              = (By.XPATH, "//div/ca-privacy-notice/div/div/button")
  SELECT_BEARING_TYPE     = (By.XPATH, "//*[@id = 'mat-select-1']")
  OPTIONS_BEARING_TYPE    = (By.XPATH, "//*[contains(@id,'mat-option')]")
  INPUT_SEARCH_DSGNTN     = (By.XPATH, "/html/body/ca-app-root/div/div[2]/ca-content-panel/div/ca-type-arrangement-single-component/div/div/ca-bearing-selection/div/div[1]/ca-designation-selection-table/div[1]/div/input")
