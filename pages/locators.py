from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM=(By.CSS_SELECTOR,'#login_form')
    REGISTRATION_FORM=(By.CSS_SELECTOR,'#register_form')
    REGISTRATION_EMAIL_FILED=(By.ID,'id_registration-email')
    REGISTRATION_PASSWORD_FIELD=(By.ID,'id_registration-password1')
    REGISTRATION_PASSWORD_CONFIRMATION_FIELD=(By.ID,'id_registration-password2')
    REGISTER_BUTTON=(By.CSS_SELECTOR,"button[name='registration_submit']")

class ProductPageLocators:
    ADD_TO_BASKET_BUTTON=(By.CSS_SELECTOR,'.btn.btn-lg.btn-primary.btn-add-to-basket')
    PRODUCT_NAME=(By.CSS_SELECTOR,'.col-sm-6.product_main h1')
    PRODUCT_PRICE=(By.CSS_SELECTOR,'.col-sm-6.product_main p')
    PRODUCT_NAME_FROM_MESSAGE=(By.CSS_SELECTOR,'#messages div:nth-child(1) .alertinner strong')
    PRODUCT_PRICE_FROM_MESSAGE=(By.CSS_SELECTOR,'#messages div:nth-child(3) .alertinner strong')
    PRODUCT_ADDED_TO_BASKET_MESSAGE=(By.CSS_SELECTOR,'#messages div:nth-child(1)')
    PRODUCT_BASKET_PRICE_MESSEGE=(By.CSS_SELECTOR,'#messages div:nth-child(3)')
    PRODUCT_SUCCESS_MESSAGE=(By.ID,'#messages div')

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators:
    BASKET_BUTTON=(By.CSS_SELECTOR,'.btn-group .btn.btn-default')
    BASKET_ITEMS_TABLE=(By.CSS_SELECTOR,'#content_inner div')
    BASKET_EMPTY_TEXT=(By.CSS_SELECTOR,'#content_inner p')
