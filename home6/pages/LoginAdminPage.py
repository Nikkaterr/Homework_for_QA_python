from selenium.webdriver.common.by import By
from .BasePage import BasePage


class LoginAdminPage(BasePage):
    PANEL_HEADING = (By.CLASS_NAME, "panel-heading")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FORGOTTEN_PASSWORD = (By.LINK_TEXT, "Forgotten Password")
    OPENCART_LINK = (By.XPATH, "//*[text()='OpenCart']")
