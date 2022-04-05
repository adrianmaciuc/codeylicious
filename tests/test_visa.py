from selenium import webdriver
import time
from datetime import datetime
from tests.conftest import ConfigC, ConfigE
from pages.visaPage import VisaPage


    # Stefan

class Test_Visa:
    def setup(self):
        self.visa = VisaPage(ConfigC)
    
    #submitting
    def test_RO_to_US(self):
        self.visa.load()
        self.visa.RO_to_US()
        self.visa.screenshot()
        assert self.visa.browser.current_url == VisaPage.URL_SUBMIT, "The page URL is incorrect."

    def teardown(self):
        self.visa.close()