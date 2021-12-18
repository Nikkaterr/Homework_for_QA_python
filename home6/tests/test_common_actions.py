from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from home6.pages.MainPage import MainPage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


def test_change_currency(browser):
    browser.open()
    MainPage(browser)._click(MainPage.BUTTON_CURRENCY)
    MainPage(browser)._click(MainPage.DROPDOWN_LIST_CURRENCY)
    # проблемы, не может найти локатор хотя по нему кликает
    MainPage(browser)._click(MainPage.POUND_BUTTON)
    MainPage(browser)._element(MainPage.ICON_POUND)


