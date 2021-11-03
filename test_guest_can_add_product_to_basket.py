import time

from pages.product_page import ProductPage

def test_add_product_to_basket(browser):
    link='http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019'
    page=ProductPage(browser,link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_product_added_to_basket_massage()
    page.should_be_product_basket_price_massage()
    page.should_be_product_name_the_same()
    page.should_be_basket_price_the_same()
