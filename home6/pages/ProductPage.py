from selenium.webdriver.common.by import By
from .BasePage import BasePage


class ProductPage(BasePage):
    TAB_DESCRIPTION = (By.ID, "tab-description")
    OLD_PRICE = (By.CSS_SELECTOR, "span[style*= 'line-through;']")
    LINK_ON_BRAND = (By.LINK_TEXT, "Canon")
    INPUT_QUANTITY = (By.NAME, "quantity")
