import time
from selenium.webdriver.common.by import By

from pages.basePage import BasePage
from tests.conftest import ConfigC

# ADI

class LoginPage(BasePage):
    URL = "https://www.phptravels.net/login"
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BTN = (By.CSS_SELECTOR, ".btn-default.btn-lg")
    REDIRECT_AFTER_LOGIN_PAGE = "https://www.phptravels.net/account/dashboard"
    CONTACT_BTN = (By.CSS_SELECTOR, "a.icon-box")

  
    def login(self, username, password):
        self.browser.find_element(*LoginPage.EMAIL_INPUT).send_keys(username)
        self.browser.find_element(*LoginPage.PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*LoginPage.LOGIN_BTN).click()


if __name__ == "__main__":
    # For module testing run from Root folder (ex python pages\loginPage.py)
    login_page = LoginPage(ConfigC)
    login_page.load(login_page.URL)
