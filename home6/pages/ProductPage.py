from selenium.webdriver.common.by import By
from .BasePage import BasePage


class ProductPage(BasePage):
    TAB_DESCRIPTION = (By.ID, "tab-description")
    OLD_PRICE = (By.CSS_SELECTOR, "span[style*= 'line-through;']")
    LINK_ON_BRAND = (By.LINK_TEXT, "Canon")
    INPUT_QUANTITY = (By.NAME, "quantity")

    def _find_tab_description(self):
        self._element(self.TAB_DESCRIPTION)
        return self

    def _find_old_price(self):
        self._element(self.OLD_PRICE)
        return self

    def _find_link_on_brand(self):
        self._element(self.LINK_ON_BRAND)
        return self

    def _find_input_quantity(self):
        self._element(self.INPUT_QUANTITY)
        return self
