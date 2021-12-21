from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from .BasePage import BasePage


class MainPage(BasePage):
    TEXT_CATEGORIES = (By.XPATH, "//span[text()='Categories']")
    BUTTON_SEARCH = (By.CSS_SELECTOR, "#search button[type='button']")
    FIRST_SWIPER = (By.CLASS_NAME, "swiper-wrapper")
    LINK_ON_MY_ACCOUNT = (By.CSS_SELECTOR, "ul.list-inline li.dropdown")
    LINK_ON_PAGE_REGISTER = (By.CSS_SELECTOR, "li.dropdown.open > ul > li:first-child")
    BUTTON_CURRENCY = (By.ID, "form-currency")
    DROPDOWN_LIST_CURRENCY = (By.CSS_SELECTOR, "#form-currency .dropdown-menu")
    POUND_BUTTON = (By.NAME, "GBP")
    ICON_POUND = (By.XPATH, "//p[text()[contains(.,'£')]]")

    def _find_text_categories(self):
        self._element(self.TEXT_CATEGORIES)
        return self

    def _find_button_search(self):
        self._element(self.BUTTON_SEARCH)
        return self

    def _find_first_swiper(self):
        self._element(self.FIRST_SWIPER)
        return self

    def _find_link_on_my_account(self):
        self._element(self.LINK_ON_MY_ACCOUNT)
        return self

    def _click_on_button_currency(self):
        self._click(MainPage.BUTTON_CURRENCY)
        return self

    def _click_on_pound_button(self):
        self._click(MainPage.POUND_BUTTON)
        return self

    def _find_icon_pound(self):
        try:
            self._element(MainPage.ICON_POUND)
        except NoSuchElementException:
            return False
        return True

    def _click_on_link_my_account(self):
        self._click(self.LINK_ON_MY_ACCOUNT)
        return self

    def _click_on_link_page_register(self):
        self._click(self.LINK_ON_PAGE_REGISTER)
        return self
