from selenium.webdriver.common.by import By
from .BasePage import BasePage


class CatalogPage(BasePage):
    COUNTER_CART = (By.ID, "cart-total")
    BUTTON_IN_CARD = (By.CLASS_NAME, "button-group")
    LINK_ON_COMPARE = (By.LINK_TEXT, "Product Compare (0)")
    TITLE_CATEGORIES = (By.XPATH, "//*[text()='Phones & PDAs']")

    def _find_counter_cart(self):
        self._element(self.COUNTER_CART)
        return self

    def _find_button_in_card(self):
        self._element(self.BUTTON_IN_CARD)
        return self

    def _find_link_on_compare(self):
        self._element(self.LINK_ON_COMPARE)
        return self

    def _find_title_categories(self):
        self._element(self.TITLE_CATEGORIES)
        return self
