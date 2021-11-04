import time
from pages.product_page import ProductPage
import pytest

@pytest.mark.parametrize('link', [pytest.param(i,marks=pytest.mark.xfail) if i==7 else i for i in range(10)])
def test_add_product_to_basket(browser,link):
    link=f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page=ProductPage(browser,link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_product_added_to_basket_massage()
    page.should_be_product_basket_price_massage()
    page.should_be_product_name_the_same()
    page.should_be_basket_price_the_same()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    page=ProductPage(browser,link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    page=ProductPage(browser,link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    page=ProductPage(browser,link)
    page.open()
    page.add_product_to_basket()
    page.should_message_be_disappeared()
