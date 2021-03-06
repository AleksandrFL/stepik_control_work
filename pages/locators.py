from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    TO_BASKET = (By.CSS_SELECTOR, ".btn.btn-add-to-basket")    
    GO_TO_BASKET = (By.CSS_SELECTOR, ".basket-mini>span>a")
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner>p")
    NOT_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner>form")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTR_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_REGISTR_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD1_REGISTR_FORM = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD2_REGISTR_FORM = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTR_FORM = (By.CSS_SELECTOR, "#register_form>button")
 
class ProductPageLocators():
    PRODUCT_NAME1 = (By.CSS_SELECTOR, ".col-sm-6>h1")    
    PRODUCT_NAME2 = (By.CSS_SELECTOR, "div.alert:nth-child(1)>div>strong")    
    PRODUCT_PRICE1 = (By.CSS_SELECTOR, ".col-sm-6>p")    
    PRODUCT_PRICE2 = (By.CSS_SELECTOR, "div.alert:nth-child(3)>div>p>strong")    
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")    

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    