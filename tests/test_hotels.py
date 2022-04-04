from selenium import webdriver
import time

from tests.conftest import ConfigC, ConfigE
from pages.hotelsPage import HotelsPage


    # Norbert

class Test_Flights:
    def setup(self):
        self.flights = HotelsPage(ConfigC)