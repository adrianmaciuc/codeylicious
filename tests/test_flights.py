from selenium import webdriver
import time
from tests.conftest import ConfigC, ConfigE
from pages.flightsPage import FlightsPage



    # Catalin

class Test_Flights:
    def setup(self):
        self.flights = FlightsPage(ConfigC)


    def test_search(self):
        self.flights.load(FlightsPage.URL)
        self.flights.insert_departure_arrival(self.flights.FLYFROM, "Cluj-Napoca")
        self.flights.select_item(self.flights.DROPDOWNDEPARTURES)
        self.flights.insert_departure_arrival(self.flights.FLYTO, "Aurel Vlaicu")
        self.flights.select_item(self.flights.DROPDOWNARRIVAL)
        self.flights.select_item(self.flights.PASSENGERS)
        self.flights.wait_for_element(self.flights.TICKETQTY)
        self.flights.select_passenger("Adults")
        self.flights.select_passenger("Childs")
        self.flights.select_item(self.flights.SEARCH)
        assert True == self.flights.element_presence(self.flights.NORESULT)

    def teardown(self):
        self.flights.close()