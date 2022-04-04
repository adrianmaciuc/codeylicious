from multiprocessing.sharedctypes import Value
import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.basePage import BasePage


# Stefan 

class VisaPage(BasePage):
    URL = "https://www.phptravels.net/visa"
    FROM_COUNTRY_DROPDOWN = (By.ID, "select2-from_country-container")
    TO_COUNTRY_DROPDOWN = (By.ID, "select2-to_country-container")
    COUNTRY_INPUT = (By.CLASS_NAME, "select2-search__field")
    DATE_PICKER = (By.ID, "date")
    SUBMIT = (By.ID, "submit")
    TODAY = datetime.today().strftime('%d-%m-%Y')
    # TODAY_PLUS_10 = DATE_PICKER.__getattribute__("value")
    # URL_SUBMIT = f"https://www.phptravels.net/visa/submit/ro/us/{TODAY_PLUS_10}"
    URL_SUBMIT = "https://www.phptravels.net/visa/submit/ro/us/15-04-2022"

    def load(self):
        self.browser.get(VisaPage.URL)
        self.browser.maximize_window()

    def RO_to_US(self):
        self.browser.find_element(*VisaPage.FROM_COUNTRY_DROPDOWN).click()
        self.browser.find_element(*VisaPage.COUNTRY_INPUT).send_keys("Romania")
        self.browser.find_element(*VisaPage.COUNTRY_INPUT).send_keys(Keys.ENTER)
        self.browser.find_element(*VisaPage.TO_COUNTRY_DROPDOWN).click()
        self.browser.find_element(*VisaPage.COUNTRY_INPUT).send_keys("United")
        self.browser.find_element(*VisaPage.COUNTRY_INPUT).send_keys(Keys.ARROW_DOWN)
        self.browser.find_element(*VisaPage.COUNTRY_INPUT).send_keys(Keys.ARROW_DOWN)
        self.browser.find_element(*VisaPage.COUNTRY_INPUT).send_keys(Keys.ARROW_DOWN)
        self.browser.find_element(*VisaPage.COUNTRY_INPUT).send_keys(Keys.ENTER)
        self.browser.find_element(*VisaPage.SUBMIT).click()
    
    def close(self):
        self.browser.close()
    
    def screenshot(self):
        date_time = time.strftime("%a.%d.%b.%Y.%H%M%S")
        self.browser.save_screenshot(f"resources\\screenshots\\{date_time}.png")