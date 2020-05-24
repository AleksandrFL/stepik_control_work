from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import MainPageLocators
from .locators import ProductPageLocators


class ProductPage(BasePage): 
    def add_product_to_basket(self):
        to_basket = self.browser.find_element(*MainPageLocators.TO_BASKET)
        to_basket.click() 
        
        
    def should_be_add_product_to_basket(self):
        self.should_be_name_product_to_basket()
        self.should_be_price_product_to_basket()

    def should_be_name_product_to_basket(self):
        name1 = self.return_text_element(*ProductPageLocators.PRODUCT_NAME1)
        name2 = self.return_text_element(*ProductPageLocators.PRODUCT_NAME2)
        print("name1 "+name1+" name2 "+name2)
        assert name1 == name2, "Не совпадают названия книги"

    def should_be_price_product_to_basket(self):
        price1 = self.return_text_element(*ProductPageLocators.PRODUCT_PRICE1)
        price2 = self.return_text_element(*ProductPageLocators.PRODUCT_PRICE2)
        print("price1 "+price1+" price2 "+price2)
        assert price1 == price2, "Не совпадают цены книги"
            
    def should_not_be_success_message(self):
        print("Проверка")
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"        

    def should_not_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is not disappeared, but should not be"        
