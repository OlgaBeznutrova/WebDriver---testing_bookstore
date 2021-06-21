from pages.login_page import LoginPage
from pages.main_page import MainPage


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()  # кликнет по ссылке логина
    login_page = LoginPage(browser, browser.current_url)  # тут же создали экземпляр LoginPage
    login_page.should_be_login_page()  # и воспользовались методом LoginPage класса, т.е. фактически тестируется сам переход от одной страницы к другой
