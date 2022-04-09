from pages.basePage import BasePage
from tests.conftest import ConfigC
from pages.homePage import HomePage


# Adi

class Test_home_page():
    def setup(self):
        self.page = BasePage(ConfigC)

    def test_link_checks(self):
        self.page.load(self.page.BASE_URL)
        home = HomePage(self.page.browser)

        results = home.home_page_link_checker()
        assert results == True, "One or more bad link(s) found"

    def teardown(self):
        self.page.close()
