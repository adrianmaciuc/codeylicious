from tests.conftest import ConfigC
from pages.basePage import BasePage
from pages.flightsPage import FlightsPage


    # Catalin

class Test_Flights:
    def setup(self):
        self.page = BasePage(ConfigC)

    def test_search(self):
        self.page.load(FlightsPage.URL)
        flights = FlightsPage(self.page.browser)
        
        flights.insert_departure_arrival(flights.FLYFROM, "Cluj-Napoca")
        flights.select_item(flights.DROPDOWNDEPARTURES)
        flights.insert_departure_arrival(flights.FLYTO, "Aurel Vlaicu")
        flights.select_item(flights.DROPDOWNARRIVAL)
        flights.select_item(flights.PASSENGERS)
        flights.wait_for_element(flights.TICKETQTY)
        flights.select_passenger("Adults")
        flights.select_passenger("Childs")
        flights.select_item(flights.SEARCH)
        assert True == flights.element_presence(flights.NORESULT)

    def teardown(self):
        self.page.close()
