from selenium.webdriver.common.by import By

class MainPageLocators(object):
  BTN_ACCEPT              = (By.XPATH, "//div/ca-privacy-notice/div/div/button")
  IMG_SINGLE_BEARING      = (By.XPATH, "/html/body/ca-app-root/div/div[2]/ca-content-panel/div/ca-one-or-two/div/div[1]/div[2]/div[1]/div[1]/img")
  SELECT_BEARING_TYPE     = (By.XPATH, "//*[@id = 'mat-select-1']")
  OPTIONS_BEARING_TYPE    = (By.XPATH, "//*[contains(@id,'mat-option')]")
  INPUT_SEARCH_DSGNTN     = (By.XPATH, "/html/body/ca-app-root/div/div[2]/ca-content-panel/div/ca-type-arrangement-single-component/div/div/ca-bearing-selection/div/div[1]/ca-designation-selection-table/div[1]/div/input")



class LoginPageLocators(object):
  EMAIL         = (By.ID, 'ap_email')
  PASSWORD      = (By.ID, 'ap_password')
  SUBMIT        = (By.ID, 'signInSubmit-input')
  ERROR_MESSAGE = (By.ID, 'message_error')
