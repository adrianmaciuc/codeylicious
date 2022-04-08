import time

from tests.conftest import ConfigC
from pages.homePage import HomePage


# Adi

class Test_home_page():
    def setup(self):
        self.home_page = HomePage(ConfigC)

    def test_link_checks(self):
        self.home_page.load(self.home_page.URL)
        results = self.home_page.link_checker()
        assert results == True, "One or more bad link(s) found"

 
    def teardown(self):
        self.home_page.close()
