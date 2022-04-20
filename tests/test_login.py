from cmath import log
from selenium import webdriver
import time

from tests.conftest import ConfigC, ConfigE
from pages.loginPage import LoginPage
from pages.basePage import BasePage
from pages.flightsPage import FlightsPage


# Adi

class Test_login():
    def setup(self):
        self.page = BasePage(ConfigC)

    def test_login_front_end_user(self):
        self.page.load(LoginPage.URL)
        self.login_page = LoginPage(self.page.browser)
        self.login_page.login(ConfigC.USERNAME, ConfigC.PASSWORD)  
        self.page.screenshot()
        assert self.login_page.browser.current_url == LoginPage.REDIRECT_AFTER_LOGIN_PAGE

    def test_login_admin(self):
        self.page.load(LoginPage.URL)
        self.login_page = LoginPage(self.page.browser)
        self.login_page.login(ConfigC.USERNAME_ADMIN, ConfigC.PASSWORD_ADMIN)
        time.sleep(2)
        assert self.page.browser.current_url == LoginPage.REDIRECT_AFTER_LOGIN_PAGE    

    def test_loginpage_contact_link(self):

        self.page.load(LoginPage.URL)
        self.login_page = LoginPage(self.page.browser)
        self.login_page.browser.find_element(*LoginPage.CONTACT_BTN).click()
        assert self.login_page.browser.current_url == "https://www.phptravels.net/contact"

    def teardown(self):
        self.page.close()


