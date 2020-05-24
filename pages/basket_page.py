from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .locators import MainPageLocators
from selenium.common.exceptions import TimeoutException  


class BasketPage(BasePage): 
    def go_to_basket(self):
        link = self.browser.find_element(*MainPageLocators.GO_TO_BASKET)
        link.click()

    def is_not_items_in_basket(self):
        assert self.is_not_element_present(*MainPageLocators.NOT_EMPTY_BASKET), \
           "Items in basket"                
        
    def should_be_success_message(self):
        assert self.is_element_present(*MainPageLocators.EMPTY_BASKET), "Basket is not empty"
