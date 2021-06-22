from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_added_to_basket_quiz(self):
        self.add_product_to_basket()
        self.solve_quiz_and_get_code()
        self.should_be_product_name_in_success_message()
        self.should_be_correct_basket_price_in_message()

    def should_be_product_added_to_basket(self):
        self.add_product_to_basket()
        self.should_be_product_name_in_success_message()
        self.should_be_correct_basket_price_in_message()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message disappeared, but should not be"

    def add_product_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()

    def should_be_product_name_in_success_message(self):
        success_message_product_name = self.get_text_from_element(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME)
        current_product_name = self.get_text_from_element(*ProductPageLocators.PRODUCT_NAME)
        assert success_message_product_name == current_product_name, \
            f"Incorrect product name in success message: {success_message_product_name} instead of '{current_product_name}'"

    def should_be_correct_basket_price_in_message(self):
        message_basket_price = self.get_text_from_element(*ProductPageLocators.MESSAGE_BASKET_PRICE)
        current_product_price = self.get_text_from_element(*ProductPageLocators.PRODUCT_PRICE)
        assert current_product_price == message_basket_price, \
            f"No match: {message_basket_price} instead of '{current_product_price}'"
