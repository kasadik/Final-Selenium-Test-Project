from pages.base_page import BasePage
from pages.locators import BasketPageLocators

class BasketPage(BasePage):

    def should_be_empty_basket(self):
        items_in_basket=self.is_element_present(*BasketPageLocators.BASKET_ITEMS_TABLE)
        assert not items_in_basket, 'Items present in basket'

    def should_be_empty_basket_text(self):
        empty_basket_text=self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_TEXT).text
        assert empty_basket_text,'Empty basket text is missing'
