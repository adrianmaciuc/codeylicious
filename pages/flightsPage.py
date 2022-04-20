from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException


# CATALIN 

class FlightsPage():
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

    def __init__(self, driver):
        self.browser = driver

    def insert_departure_arrival(self, locator_value, city):
        self.browser.find_element(*locator_value).send_keys(city)

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
