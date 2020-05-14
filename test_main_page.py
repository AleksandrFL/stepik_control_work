import pytest
from pages.main_page import MainPage
from pages.basket_page import BasketPage
import time


@pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина
    
    page_login = LoginPage(browser, browser.current_url)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page_login.should_be_login_page()

@pytest.mark.skip
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()              # выполняем метод страницы - переходим на страницу корзины
    time.sleep(3)
    page.is_not_items_in_basket()
    page.should_be_success_message()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()              # выполняем метод страницы - переходим на страницу корзины
    time.sleep(3)
    page.is_not_items_in_basket()
    page.should_be_success_message()

