from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.basePage import BasePage
from selenium import webdriver
from selenium.webdriver.support.ui import Select


# Norbert 

class HotelsPage():
    URL = "https://www.phptravels.net/hotels"
    CITY_NAME= (By.CSS_SELECTOR, ".select2-selection")
    CITY_NAME_SEARCH =(By.CSS_SELECTOR, ".select2-search__field")
    CITY_SELECT =(By.CSS_SELECTOR, ".select2-results__option")
    CHECK_IN = (By.CSS_SELECTOR, ".checkin")
    CHECK_IN_DATEPICKER = (By.CSS_SELECTOR, ".datepicker ")
    CHECK_OUT =(By.CSS_SELECTOR, ".checkout")
    CHECK_OUT_DATEPICKER = (By.CSS_SELECTOR, ".datepicker")
    DROPDOWN_TRAVELLERS = (By.CSS_SELECTOR, ".dropdown-toggle.travellers")
    DROPDOWN_TRAVELLERS_NATIONALITY = (By.CSS_SELECTOR, ".form-select.nationality")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".btn-primary")
    NO_MATCH_SCREEN = (By.CSS_SELECTOR, ".container.text-center")
    ROOMS = 'Rooms'
    CHILDREN = 'Children'
    ADULTS = 'Adults'
    NATIONALITIES = ['Norway', 'Panama', 'Poland', 'Portugal', 'Qatar']
    #Nationalities se poate scoate, a fost lasat doar pentru practice for myself.
    #A fost doar asa sa fac indexare sa ma "re-obisnuiesc" ca parametrii pot fi si de genul

    def __init__(self, driver):
        self.browser = driver 

    def date_picker_checkin(self, ziua):
        self.browser.find_element(*HotelsPage.CHECK_IN).click()
        datepicker = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".datepicker")))
        datepicker_days= datepicker.find_elements(By.CSS_SELECTOR, ".day:not(.disabled)")
        for zile in datepicker_days:
            if zile.text == ziua:
                zile.click()
                break

    ## ZIUA CAND O BAG TREBUIE SA FIE STRING NU INT
    def date_picker_checkout(self, ziua):
        datepicker_days= self.browser.find_elements(By.CSS_SELECTOR, ".day:not(.disabled)")
        for zile in datepicker_days:
            if zile.text == ziua:
                zile.click()
                break
    
    ## ZIUA CAND O BAG TREBUIE SA FIE STRING NU INT
    def travellers_choice(self, type0):
        drop_down = self.browser.find_element(*HotelsPage.DROPDOWN_TRAVELLERS)
        drop_down.click()
        drop_down_options = self.browser.find_elements(By.CSS_SELECTOR, ".dropdown-item")
        for options in drop_down_options:
            if type0 in options.text:
                options.find_element(By.CSS_SELECTOR, ".qtyInc").click()

    def travellers_nationality(self, nationality):
        nationality_dropdown = Select(self.browser.find_element(*HotelsPage.DROPDOWN_TRAVELLERS_NATIONALITY))
        nationality_dropdown.select_by_visible_text((nationality.title()))

        # Din pacate site-ul la nationality se refera la tara, gen: Romania nu la nationalitate "Romania(n)"

        
    def search_city(self, city):
        self.browser.find_element(*HotelsPage.CITY_NAME).click()
        self.browser.find_element(*HotelsPage.CITY_NAME_SEARCH).send_keys(city)
        element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".select2-results__option--highlighted")))
        element.click()
        
    
    def custom_close(self):
        img = self.browser.find_element(*HotelsPage.NO_MATCH_SCREEN)
        source = img.get_attribute("src")
        if source == "https://www.phptravels.net/app/themes/default/assets/img/no_results.gif":
            self.broswer.close()
