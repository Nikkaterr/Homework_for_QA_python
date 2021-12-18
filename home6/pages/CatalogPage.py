from selenium.webdriver.common.by import By
from .BasePage import BasePage


class CatalogPage(BasePage):
    COUNTER_CART = (By.ID, "cart-total")
    BUTTON_IN_CARD = (By.CLASS_NAME, "button-group")
    LINK_ON_COMPARE = (By.LINK_TEXT, "Product Compare (0)")
    TITLE_CATEGORIES = (By.XPATH, "//*[text()='Phones & PDAs']")
