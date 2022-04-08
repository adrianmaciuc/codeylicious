from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from pages.basePage import BasePage


# CATALIN 

class FlightsPage(BasePage):
    URL = "https://www.phptravels.net/flights"
    FLYFROM = (By.NAME, "from")
    FLYTO = (By.NAME, "to")
    DATE = (By.NAME, "depart")
    PASSENGERS = (By.CSS_SELECTOR, ".dropdown-contain")
    SEARCH = (By.CSS_SELECTOR, ".ladda-label")
    DROPDOWNDEPARTURES = (By.CSS_SELECTOR, ".autocomplete-results.intro.troll")
    DROPDOWNARRIVAL = (By.CSS_SELECTOR, "._1.autocomplete-wrapper.row_2 > .autocomplete-results.intro.troll")
    TICKETQTY = (By.CSS_SELECTOR, ".dropdown-menu > .dropdown-item")
    QTYINC = (By.CSS_SELECTOR, ".qtyInc")
    NORESULT = (By.CSS_SELECTOR, "#fadein > div.container.text-center")


    def insert_departure_arrival(self, locator_value, city):
        self.browser.find_element(*locator_value).send_keys(city)

    def select_item(self, locator_value):
        self.browser.find_element(*locator_value).click()

    def select_passenger(self, option):
        dropItems = self.browser.find_elements(*FlightsPage.TICKETQTY) 
        for item in dropItems:
            if item.text == option:
                item.find_element(*FlightsPage.QTYINC).click()

    def element_presence(self, locator_value):
        visibility = True
        try:
            self.browser.find_element(*locator_value)
        except NoSuchElementException:
            visibility = False
        return visibility

    def wait_for_element(self, locator_value):
        return WebDriverWait(self.browser, 20).until(ec.element_to_be_clickable((locator_value)))
