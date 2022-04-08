from selenium import webdriver
import time


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

    def load(self, URL):
        self.browser.get(URL)
        self.browser.maximize_window()

    def screenshot(self):
        date_time = time.strftime("%a.%d.%b.%Y.%H%M%S")
        self.browser.save_screenshot(f"resources\\screenshots\\{date_time}.png")

    def close(self):
        self.browser.quit()