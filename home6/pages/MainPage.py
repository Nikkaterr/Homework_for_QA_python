from selenium.webdriver.common.by import By
from .BasePage import BasePage


class MainPage(BasePage):
    TEXT_CATEGORIES = (By.XPATH, "//span[text()='Categories']")
    BUTTON_SEARCH = (By.CSS_SELECTOR, "#search button[type='button']")
    FIRST_SWIPER = (By.CLASS_NAME, "swiper-wrapper")
    lINK_ON_MY_ACCOUNT = (By.XPATH, "//a[text()='My Account']")
    BUTTON_CURRENCY = (By.CSS_SELECTOR, "#form-currency > div > button")
    DROPDOWN_LIST_CURRENCY = (By.CSS_SELECTOR, "#form-currency .dropdown-menu")
    POUND_BUTTON = (By.CSS_SELECTOR, "button[name = 'GBP']")
    ICON_POUND = (By.XPATH, "//p[text()[contains(.,'£')]]")
