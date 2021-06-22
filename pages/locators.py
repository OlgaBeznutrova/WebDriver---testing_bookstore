from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini > span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    INPUT_EMAIL = (By.ID, "id_registration-email")
    INPUT_PASSWORD_1 = (By.ID, "id_registration-password1")
    INPUT_PASSWORD_2 = (By.ID, "id_registration-password2")
    BUTTON_REGISTRATION = (By.NAME, "registration_submit")


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BUTTON_ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-child(1)")
    SUCCESS_MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")
    MESSAGE_BASKET_PRICE = (By.CSS_SELECTOR, ".alert-info strong")


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")
