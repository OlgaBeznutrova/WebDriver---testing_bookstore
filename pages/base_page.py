import math
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators


class BasePage:

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait = timeout

    def is_disappeared(self, how, what, timeout=4):  # ожидаем пока элемент не исчезнет
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:  # если время истекло, значит, элемент так и не исчез.  Возвращаем False
            return False
        return True

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what,
                               timeout=4):  # ожидаем, пока элемент не появится. Если так и не появился - True
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def get_text_from_element(self, how, what):
        return self.browser.find_element(how, what).text

    def go_to_basket_page(self):
        basket_link = self.browser.find_element(
            *BasePageLocators.BASKET_LINK)  # факт перехода в корзину: нашли ссылку и перешли по ней
        basket_link.click()

    def go_to_login_page(self):
        login_link = self.browser.find_element(
            *BasePageLocators.LOGIN_LINK)  # факт перехода: нашли ссылку и перешли по ней
        login_link.click()

    def open(self):
        self.browser.get(self.url)

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def should_be_basket_link(self):
        assert self.is_element_present(
            *BasePageLocators.BASKET_LINK), "Basket link is not presented"  # проверяем, что ссылка на корзину вообще представлена на странице)

    def should_be_login_link(self):
        assert self.is_element_present(
            *BasePageLocators.LOGIN_LINK), "Login link is not presented"  # проверяем, что ссылка на регистрацию вообще представлена на странице)

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")