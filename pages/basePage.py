from selenium import webdriver


class BasePage():
    def __init__(self, Configurations):
        if Configurations.BROWSER_TYPE == "Chrome":
            webdriver.chrome.service.Service(Configurations.DRIVER_PATH)
            self.options = webdriver.ChromeOptions()
            self.options.add_argument('log-level=3')
            self.browser = webdriver.Chrome(options=self.options)

        elif Configurations.BROWSER_TYPE == "Edge": 
            webdriver.edge.service.Service(Configurations.DRIVER_PATH)
            self.options = webdriver.edge.options.Options()
            self.options.add_argument('log-level=3')
            self.browser = webdriver.Edge(options=self.options)

    def get_driver(self):
        return self.browser