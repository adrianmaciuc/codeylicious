from selenium import webdriver
import time

from tests.conftest import ConfigC, ConfigE
from pages.hotelsPage import HotelsPage


    # Norbert

class Test_Hotels:
    def setup(self):
        self.hotels = HotelsPage(ConfigC)


    def booking_hotels(self):
        self.hotels.load()
    
    def test_search_city(self):
        self.hotels.search_city('Cluj-Napoca')
        
    def test_checkin(self):    
        self.hotels.date_picker_checkin('15')

    def test_checkout(self):
        self.hotels.date_picker_checkout('25')

    def test_travellers(self):
        self.hotels.travellers_choice(HotelsPage.ADULTS)
        
    def test_travellers_nationality(self):
        self.hotels.travellers_nationality(HotelsPage.NATIONALITIES[3])

    def teardown(self):
        self.hotels.close()