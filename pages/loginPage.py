import time
from selenium.webdriver.common.by import By

from pages.basePage import BasePage

# ADI

class LoginPage(BasePage):
    URL = "https://www.phptravels.net/login"
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BTN = (By.CSS_SELECTOR, ".btn-default.btn-lg")
    REDIRECT_AFTER_LOGIN_PAGE = "https://www.phptravels.net/account/dashboard"
    CONTACT_BTN = (By.CSS_SELECTOR, "a.icon-box")

    def load(self):
        self.browser.get(LoginPage.URL)
        self.browser.maximize_window()
    
    def login(self, username, password):
        self.browser.find_element(*LoginPage.EMAIL_INPUT).send_keys(username)
        self.browser.find_element(*LoginPage.PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*LoginPage.LOGIN_BTN).click()

    def close(self):
        self.browser.quit()

    def screenshot(self):
        date_time = time.strftime("%a.%d.%b.%Y.%H%M%S")
        self.browser.save_screenshot(f"resources\\screenshots\\{date_time}.png")

    def get_driver(self):
        return self.browser


if __name__ == "__main__":
    # For module testing run from Root folder (ex python pages\loginPage.py)
    login_page = LoginPage(Config)
    login_page.load()
    assert login_page.browser.title == "Login - PHPTRAVELS" , "opening of login page failed"
    login_page.login("user@phptravels.com","demouser")
    assert login_page.browser.current_url == "https://www.phptravels.net/account/dashboard" , "Redirection after login not performed"
    login_page.browser.quit()