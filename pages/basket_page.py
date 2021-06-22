from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket is not empty, but should be"

    def should_not_be_disappeared_message_about_empty_basket(self):
        assert not self.is_disappeared(*BasketPageLocators.EMPTY_BASKET), \
            "Message about empty basket disappeared, but should not be"
