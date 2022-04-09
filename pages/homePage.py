from selenium.webdriver.common.by import By
import requests
from enum import Enum

# ADI

class HomePage():
    URL = "https://www.phptravels.net"

    class ElementWithLink(Enum):
        HOME_HEADER_MENU_BTN = (By.LINK_TEXT, "Home")
        HOTELS_HEADER_MENU_BTN = (By.LINK_TEXT, "Hotels")
        FLIGHTS_HEADER_MENU_BTN = (By.LINK_TEXT, "Flights")
        TOURS_HEADER_MENU_BTN = (By.LINK_TEXT, "Tours")
        VISA_HEADER_MENU_BTN = (By.LINK_TEXT, "Visa")
        BLOG_HEADER_MENU_BTN = (By.LINK_TEXT, "Blog")
        OFFERS_HEADER_MENU_BTN = (By.LINK_TEXT, "Offers")
        COMPANY_HEADER_MENU_BTN = (By.LINK_TEXT, "Company")
        SIGNUP_TOP_BTN = (By.CSS_SELECTOR, ".header-right > [href*='signup']")

    def __init__(self, driver):
        self.browser = driver 

    def home_page_link_checker(self):
        badLinks = []
        for element in HomePage.ElementWithLink:
            # ElementWithLink is a subclass of HomePage and inherits from built-in python Enum class, that lets us treat its attributes/properties like a list
            # so we can iterate thru each one. You can access the data via ElementWithLink.name for variable and ElementWithLink.value for value
            webelement = self.browser.find_element(*element.value)
            link_to_check = webelement.get_attribute("href")
        
            try:
                # requests is a  library mostly used to test API. We can use it here to test if a link returns 200 
                result = requests.get(link_to_check).status_code
                if result != 200:
                    badLinks.append(webelement)
            except:
                badLinks.append(webelement.text + " " +  webelement.aria_role)
        if badLinks == []:
            return True
        else:
            return badLinks

    def click_on(self, element):
        self.browser.find_element(*element).click()

