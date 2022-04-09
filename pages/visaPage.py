from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Stefan 

class VisaPage():
    URL = "https://www.phptravels.net/visa"
    FROM_COUNTRY_DROPDOWN = (By.ID, "select2-from_country-container")
    TO_COUNTRY_DROPDOWN = (By.ID, "select2-to_country-container")
    COUNTRY_INPUT = (By.CLASS_NAME, "select2-search__field")
    DATE_PICKER = (By.ID, "date")
    SUBMIT_BTN = (By.ID, "submit")
    TODAY = datetime.today().strftime('%d-%m-%Y')

    def __init__(self, driver):
        self.browser = driver
   
    def countriesFromTo(self,VISA_FROM_COUNTRY, VISA_TO_COUNTRY):
        self.browser.find_element(*VisaPage.FROM_COUNTRY_DROPDOWN).click()
        self.browser.find_element(*VisaPage.COUNTRY_INPUT).send_keys(VISA_FROM_COUNTRY)
        self.browser.find_element(*VisaPage.COUNTRY_INPUT).send_keys(Keys.ENTER)
        self.browser.find_element(*VisaPage.TO_COUNTRY_DROPDOWN).click()
        self.browser.find_element(*VisaPage.COUNTRY_INPUT).send_keys(VISA_TO_COUNTRY)
        self.browser.find_element(*VisaPage.COUNTRY_INPUT).send_keys(Keys.ENTER)
        self.browser.find_element(*VisaPage.SUBMIT_BTN).click()

    def getAttrValue(self, element, atribut):
        return self.browser.find_element(*element).get_attribute(atribut)

    def click_on(self, element):
        self.browser.find_element(*element).click()