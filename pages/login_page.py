from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in str(self.url), "Login link is not presented"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login from is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTR_FORM), "Registr from is not presented"

    def register_new_user(self, email, password):
        reg_email = self.browser.find_element(*LoginPageLocators.LOGIN_REGISTR_FORM)
        reg_email.send_keys(email)
        reg_passw1 = self.browser.find_element(*LoginPageLocators.PASSWORD1_REGISTR_FORM)
        reg_passw1.send_keys(password)
        reg_passw2 = self.browser.find_element(*LoginPageLocators.PASSWORD2_REGISTR_FORM)
        reg_passw2.send_keys(password)
        btn_reg = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTR_FORM)
        btn_reg.click()
        
        