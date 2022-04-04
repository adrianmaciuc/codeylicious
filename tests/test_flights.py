from selenium import webdriver
import time

from tests.conftest import ConfigC, ConfigE
from pages.flightsPage import FlightsPage


    # Catalin

class Test_Flights:
    def setup(self):
        self.flights = FlightsPage(ConfigC)


