from selenium import webdriver
import time

from tests.conftest import ConfigC, ConfigE
from pages.visaPage import VisaPage


    # Stefan

class Test_Visa:
    def setup(self):
        self.visa = VisaPage(ConfigC)
    
    #submitting Visa request
    def testSubmitCountries(self):
        self.visa.load(VisaPage.URL)
        self.visa.countriesFromTo(ConfigC.VISA_FROM_COUNTRY, ConfigC.VISA_TO_COUNTRY)
        self.visa.screenshot()
        assert "https://www.phptravels.net/visa/submit/" in self.visa.browser.current_url, "The page URL is incorrect."

    def teardown(self):
        self.visa.close()