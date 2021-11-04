from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_button=self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def should_be_product_name_the_same(self):
        product_name=self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_from_massage = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_FROM_MESSAGE).text
        assert product_name == product_name_from_massage,'Product names are different'

    def should_be_basket_price_the_same(self):
        product_price=self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_price_from_massage = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_FROM_MESSAGE).text
        assert product_price == product_price_from_massage

    def should_be_product_added_to_basket_massage(self):
        product_added_to_basket_message=self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_TO_BASKET_MESSAGE)
        assert product_added_to_basket_message, 'Product added to basket message is missing'

    def should_be_product_basket_price_massage(self):
        product_added_to_basket_message=self.browser.find_element(*ProductPageLocators.PRODUCT_BASKET_PRICE_MESSEGE)
        assert product_added_to_basket_message, 'Product basket price_massage is missing'

    def should_not_be_success_message(self):

        assert self.is_not_element_preset(*ProductPageLocators.PRODUCT_SUCCESS_MESSAGE), 'Message is present'

    def should_message_be_disappeared(self):
        assert self.is_element_disappeared(*ProductPageLocators.PRODUCT_SUCCESS_MESSAGE), 'Message is not dissapered'