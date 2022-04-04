from selenium import webdriver
from tests.conftest import Config


class BasePage():
    def __init__(self, Config):
        if Config.BROWSER_TYPE == "Chrome":
            webdriver.chrome.service.Service(Config.DRIVER_PATH)
            self.options = webdriver.ChromeOptions()
            self.options.add_argument('log-level=3')
            self.browser = webdriver.Chrome(options=self.options)

        elif Config.BROWSER_TYPE == "Edge": 
            webdriver.edge.service.Service(Config.DRIVER_PATH)
            self.options = webdriver.edge.options.Options()
            self.options.add_argument('log-level=3')
            self.browser = webdriver.Edge(options=self.options)

    def get_driver(self):
        return self.browser