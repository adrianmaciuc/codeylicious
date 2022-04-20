from selenium import webdriver
import time

from tests.conftest import ConfigC, ConfigE
from pages.hotelsPage import HotelsPage
from pages.basePage import BasePage


    # Norbert

class Test_Hotels:
    def setup(self):
        self.page = BasePage(ConfigC)


    def test_booking_hotels(self):
        self.hotels = HotelsPage(self.page.browser)
        self.hotels.load()
        self.hotels.search_city('Cluj-Napoca')
        self.hotels.date_picker_checkin('15')
        self.hotels.date_picker_checkout('25')
        self.hotels.travellers_choice(HotelsPage.ADULTS)
        self.hotels.travellers_nationality(HotelsPage.NATIONALITIES[3])
  
    def teardown(self):
        self.hotels.close()


    # def teardown_custom(self):
    #     self.hotels.custom_close()