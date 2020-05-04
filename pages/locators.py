from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    TO_BASKET = (By.CSS_SELECTOR, ".btn.btn-add-to-basket")    
    PRODUCT_NAME1 = (By.CSS_SELECTOR, ".col-sm-6>h1")    
    PRODUCT_NAME2 = (By.CSS_SELECTOR, "div.alert:nth-child(1)>div>strong")    
    PRODUCT_PRICE1 = (By.CSS_SELECTOR, ".col-sm-6>p")    
    PRODUCT_PRICE2 = (By.CSS_SELECTOR, "div.alert:nth-child(3)>div>p>strong")    

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTR_FORM = (By.CSS_SELECTOR, "#register_form")
 
