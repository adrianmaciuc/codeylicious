from tests.conftest import ConfigC
from pages.basePage import BasePage
from pages.flightsPage import FlightsPage


    # Catalin

class Test_Flights:
    def setup(self):
        self.page = BasePage(ConfigC)

    def test_search(self):
        self.page.load(FlightsPage.URL)
        self.flights = FlightsPage(self.page.browser)
        self.flights.insert_departure_arrival(self.flights.FLYFROM, "Cluj-Napoca")
        self.page.click_on(self.flights.DROPDOWNDEPARTURES)
        self.flights.insert_departure_arrival(self.flights.FLYTO, "Aurel Vlaicu")
        self.page.click_on(self.flights.DROPDOWNARRIVAL)
        self.page.click_on(self.flights.PASSENGERS)
        self.page.wait_for_element(self.flights.TICKETQTY)
        self.flights.select_passenger("Adults")
        self.flights.select_passenger("Childs")
        self.page.click_on(self.flights.SEARCH)
        assert True == self.flights.element_presence(self.flights.NORESULT)

    def teardown(self):
        self.page.close()
