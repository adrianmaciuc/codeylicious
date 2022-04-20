import time
from selenium.webdriver.common.by import By
# from pages.basePage import BasePage
from tests.conftest import ConfigC

# ADI

class LoginPage():
    URL = "https://www.phptravels.net/login"
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BTN = (By.CSS_SELECTOR, ".btn-default.btn-lg")
    REDIRECT_AFTER_LOGIN_PAGE = "https://www.phptravels.net/account/dashboard"
    CONTACT_BTN = (By.CSS_SELECTOR, "a.icon-box")

    def __init__(self,driver):
        self.browser = driver
  
    def login(self,username, password):
        self.browser.find_element(*LoginPage.EMAIL_INPUT).send_keys(username)
        self.browser.find_element(*LoginPage.PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*LoginPage.LOGIN_BTN).click()

    def click_on(self, element):
        self.browser.find_element(*element).click()
