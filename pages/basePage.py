
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

        self.BASE_URL = "https://www.phptravels.net/"
        self.SIGNUP_URL = self.BASE_URL + "signup"
        self.LOGIN_URL = self.BASE_URL + "login"
        self.HOTELS_URL = self.BASE_URL + "hotels"
        self.FLIGHTS_URL = self.BASE_URL + "flights"
        self.TOURS_URL = self.BASE_URL + "tours"
        self.VISA_URL = self.BASE_URL + "visa"
        self.BLOG_URL = self.BASE_URL + "blog"
        self.OFFERS_URL = self.BASE_URL + "offers"
        self.COMPANY_URL = self.BASE_URL + "company"
        self.BLOG_URL = self.BASE_URL + "blog"
        self.ABOUT_URL = self.BASE_URL + "about-us"
        self.TERMS_OF_USE_URL = self.BASE_URL + "terms-of-use"
        self.FAQ_URL = self.BASE_URL + "faq"
        self.HOW_TO_BOOK_URL = self.BASE_URL + "how-to-book"
        self.ACCOUNT_DASHBOARD_URL = self.BASE_URL + "account/dashboard"
        self.ACCOUNT_BOOKINGS_URL = self.BASE_URL + "account/bookings"
        self.ACCOUNT_PROFILE_URL = self.BASE_URL + "account/profile"
        self.ACCOUNT_DASHBOARD_URL = self.BASE_URL + "account/dashboard"
        self.HOME_MENU_BTN = (By.LINK_TEXT, "Home")
        self.HOTELS_MENU_BTN = (By.LINK_TEXT, "Hotels")
        self.FLIGHTS_MENU_BTN = (By.LINK_TEXT, "Flights")
        self.TOURS_MENU_BTN = (By.LINK_TEXT, "Tours")
        self.VISA_MENU_BTN = (By.LINK_TEXT, "Visa")
        self.BLOG_MENU_BTN = (By.LINK_TEXT, "Blog")
        self.OFFERS_MENU_BTN = (By.LINK_TEXT, "Offers")
        self.COMPANY_MENU_BTN = (By.LINK_TEXT, "Company")
        self.SIGNUP_TOP_BTN = (By.CSS_SELECTOR, ".header-right > [href*='signup']")
        self.LOGIN_TOP_BTN = (By.LINK_TEXT, "Login")

    def navigate_to(self, URL):
        self.browser.get(URL)

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

    def click_on(self, element):
        self.browser.find_element(*element).click()

    def wait_for_element(self, locator):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((locator)))