from pages.basePage import BasePage
from tests.conftest import ConfigC
from pages.visaPage import VisaPage


    # Stefan

class Test_Visa:
    def setup(self):
        self.page = BasePage(ConfigC)
    
    #submitting Visa request
    def testSubmitCountries(self):
        self.page.load(VisaPage.URL)
        visa = VisaPage(self.page.browser)

        visa.countriesFromTo(ConfigC.VISA_FROM_COUNTRY, ConfigC.VISA_TO_COUNTRY)
        self.page.screenshot()
        assert "https://www.phptravels.net/visa/submit/" in visa.browser.current_url, "The page URL is incorrect."

    def teardown(self):
        self.page.close()