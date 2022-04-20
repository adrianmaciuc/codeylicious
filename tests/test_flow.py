import time
from pages.loginPage import LoginPage
from pages.flightsPage import FlightsPage
from pages.visaPage import VisaPage

from tests.conftest import ConfigC
from pages.basePage import BasePage


# Adi

class Test_Flows():
    def setup(self):
        self.page = BasePage(ConfigC)

    def test_first_flow(self):
        self.page.load(LoginPage.URL)
        loginPage = LoginPage(self.page.browser)
        loginPage.login(ConfigC.USERNAME, ConfigC.PASSWORD)
        
        self.page.wait_for_element(self.page.VISA_MENU_BTN)
        self.page.click_on(self.page.VISA_MENU_BTN)
        visaPage = VisaPage(self.page.browser)
        visaPage.countriesFromTo(ConfigC.VISA_FROM_COUNTRY, ConfigC.VISA_TO_COUNTRY)

        self.page.wait_for_element(self.page.FLIGHTS_MENU_BTN)
        self.page.click_on(self.page.FLIGHTS_MENU_BTN)
        flightsPage = FlightsPage(self.page.browser)
        flightsPage.insert_departure_arrival(flightsPage.FLYFROM, "Cluj-Napoca")
        flightsPage.select_item(flightsPage.DROPDOWNDEPARTURES)
        flightsPage.insert_departure_arrival(flightsPage.FLYTO, "Aurel Vlaicu")
        flightsPage.select_item(flightsPage.DROPDOWNARRIVAL)
        flightsPage.select_item(flightsPage.PASSENGERS)
        flightsPage.select_item(flightsPage.SEARCH)

        assert True == flightsPage.element_presence(flightsPage.NORESULT)

    def teardown(self):
        self.page.close()
