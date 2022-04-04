from selenium import webdriver
import time

from tests.conftest import ConfigC, ConfigE
from pages.loginPage import LoginPage


# Adi

class Test_login():
    def setup(self):
        self.login_page = LoginPage(ConfigC)

    def test_login_front_end_user(self):
        self.login_page.load()
        self.login_page.login(LoginPage.USERNAME, LoginPage.PASSWORD)  
        self.login_page.screenshot()
        assert self.login_page.browser.current_url == LoginPage.REDIRECT_AFTER_LOGIN_PAGE

    def test_login_admin(self):
        self.login_page.load()
        self.login_page.login(ConfigC.USERNAME_ADMIN, ConfigC.PASSWORD_ADMIN)
        time.sleep(2)
        assert self.login_page.browser.current_url == LoginPage.REDIRECT_AFTER_LOGIN_PAGE    

    def test_loginpage_links(self):
        self.login_page.load()
        self.login_page.browser.find_element(*LoginPage.CONTACT_BTN).click()
        assert self.login_page.browser.current_url == "https://www.phptravels.net/contact"

    def teardown(self):
        self.login_page.close()


