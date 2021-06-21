import time

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_added_to_basket(self):
        self.should_be_button_for_adding_to_basket()
        self.add_product_to_basket()
        self.solve_quiz_and_get_code()
        self.should_be_alert_about_successful_addition()
        self.should_be_product_name_in_successful_alert()
        self.should_be_alert_about_basket_total_price()
        self.should_be_correct_basket_total_price_in_alert()

    def should_be_button_for_adding_to_basket(self):
        assert self.is_element_present(
            *ProductPageLocators.BUTTON_ADD_TO_BASKET), "Button for adding to basket is not presented on product_page"

    def add_product_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()

    def should_be_alert_about_successful_addition(self):
        assert self.is_element_present(
            *ProductPageLocators.ALERT_SUCCESSFUL_ADDITION), "No alert about successful product addition"

    def should_be_product_name_in_successful_alert(self):
        current_product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        alert_product_name = self.browser.find_element(
            *ProductPageLocators.ALERT_SUCCESSFUL_ADDITION_PRODUCT_NAME).text
        assert alert_product_name == current_product_name, \
            f"No match: {alert_product_name} instead of '{current_product_name}'"

    def should_be_alert_about_basket_total_price(self):
        assert self.is_element_present(
            *ProductPageLocators.ALERT_BASKET_INFO), "No alert about basket total price"

    def should_be_correct_basket_total_price_in_alert(self):
        current_product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_total_price_in_alert = self.browser.find_element(
            *ProductPageLocators.ALERT_TOTAL_BASKET_PRICE).text
        assert current_product_price == basket_total_price_in_alert, \
            f"No match: {basket_total_price_in_alert} instead of '{current_product_price}'"
