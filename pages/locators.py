from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BUTTON_ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    ALERT_SUCCESSFUL_ADDITION = (By.CSS_SELECTOR, ".alert-success:nth-child(1)")
    ALERT_SUCCESSFUL_ADDITION_PRODUCT_NAME = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")
    ALERT_BASKET_INFO = (By.CLASS_NAME, "alert-info")
    ALERT_TOTAL_BASKET_PRICE = (By.CSS_SELECTOR, ".alert-info strong")

