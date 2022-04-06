from selenium import webdriver
import time

from tests.conftest import ConfigC, ConfigE
from pages.flightsPage import FlightsPage



    # Catalin

class Test_Flights:
    def setup(self):
        self.flights = FlightsPage(ConfigC)


    def test_search(self):
        self.flights.load()
        self.flights.insert_departure_arrival(self.flights.FLYFROM, "Cluj-Napoca")
        self.flights.select_item(self.flights.DROPDOWN)
        self.flights.insert_departure_arrival(self.flights.FLYTO, "Aurel Vlaicu")
        self.flights.select_item(self.flights.DROPDOWN2)
        self.flights.select_item(self.flights.PASSENGERS)
        self.flights.wait_for_element(self.flights.TICKETQTY)
        self.flights.select_passenger("Adults")
        self.flights.select_passenger("Childs")
        self.flights.select_item(self.flights.SEARCH)
        # n-am apucat sa pun assertu ca nu mai mere site-ul :( 
