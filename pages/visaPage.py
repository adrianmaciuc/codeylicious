from multiprocessing.sharedctypes import Value
import time
from tests.conftest import ConfigC
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
    SUBMIT_BTN = (By.ID, "submit")
    TODAY = datetime.today().strftime('%d-%m-%Y')

    def load(self):
        self.browser.get(VisaPage.URL)
        self.browser.maximize_window()
    
    def countriesFromTo(self,VISA_FROM_COUNTRY, VISA_TO_COUNTRY):
        self.browser.find_element(*VisaPage.FROM_COUNTRY_DROPDOWN).click()
        self.browser.find_element(*VisaPage.COUNTRY_INPUT).send_keys(VISA_FROM_COUNTRY)
        self.browser.find_element(*VisaPage.COUNTRY_INPUT).send_keys(Keys.ENTER)
        self.browser.find_element(*VisaPage.TO_COUNTRY_DROPDOWN).click()
        self.browser.find_element(*VisaPage.COUNTRY_INPUT).send_keys(VISA_TO_COUNTRY)
        self.browser.find_element(*VisaPage.COUNTRY_INPUT).send_keys(Keys.ENTER)
        self.browser.find_element(*VisaPage.SUBMIT_BTN).click()

    def close(self):
        self.browser.close()
    
    def screenshot(self):
        date_time = time.strftime("%a.%d.%b.%Y.%H%M%S")
        self.browser.save_screenshot(f"resources\\screenshots\\{date_time}.png")

    def getAttrValue(self, element, atribut):
        return self.browser.find_element(*element).get_attribute(atribut)


if __name__ == "__main__":
    visapage = VisaPage(ConfigC)
    visapage.load()
    valoare = visapage.getAttrValue(VisaPage.DATE_PICKER, "value")
    visapage.countriesFromTo(ConfigC.VISA_FROM_COUNTRY, ConfigC.VISA_TO_COUNTRY)