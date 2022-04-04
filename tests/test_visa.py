from selenium import webdriver
import time

from tests.conftest import ConfigC, ConfigE
from pages.visaPage import VisaPage


    # Stefan

class Test_Flights:
    def setup(self):
        self.flights = VisaPage(ConfigC)