from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented on main_page" # проверяем, что ссылка на регистрацию вообще представлена на странице)

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK) # факт перехода: нашли ссылку и перешли по ней
        login_link.click()
