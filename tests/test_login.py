
from tests.conftest import Config
from pages.loginPage import LoginPage

from selenium import webdriver



class Test_login():
    def setup(self):
        self.login_page = LoginPage(Config)

    def test_login_front_end_user(self):
        self.login_page.load()
        self.login_page.login(Config.USERNAME, Config.PASSWORD)  
        self.login_page.screenshot()

    def test_login_admin(self):
        self.login_page.load()
        self.login_page.login(Config.USERNAME_ADMIN, Config.PASSWORD_ADMIN)    

    def teardown(self):
        self.login_page.close()


