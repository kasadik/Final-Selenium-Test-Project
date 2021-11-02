from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login'in self.browser.current_url, '"login" is missing from url'

    def should_be_login_form(self):
        login_form=self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        assert login_form

    def should_be_register_form(self):
        registration_form=self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM)
        assert registration_form