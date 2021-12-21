from selenium.webdriver.common.by import By
from .BasePage import BasePage


class LoginAdminPage(BasePage):
    PANEL_HEADING = (By.CLASS_NAME, "panel-heading")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FORGOTTEN_PASSWORD = (By.LINK_TEXT, "Forgotten Password")
    OPENCART_LINK = (By.XPATH, "//*[text()='OpenCart']")
    INPUT_USERNAME = (By.ID, "input-username")
    INPUT_PASSWORD = (By.ID, "input-password")
    HEADER_LOGO_OPENCART = (By.ID, "header-logo")

    def login_with(self, username, password):
        self._element(self.INPUT_USERNAME).send_keys(username)
        self._element(self.INPUT_PASSWORD).send_keys(password)
        self._element(self.SUBMIT_BUTTON).click()

    def _find_panel_heading(self):
        self._element(self.PANEL_HEADING)
        return self

    def _find_submit_button(self):
        self._element(self.SUBMIT_BUTTON)
        return self

    def _find_forgotten_password(self):
        self._element(self.FORGOTTEN_PASSWORD)
        return self

    def _find_opencart_link(self):
        self._element(self.OPENCART_LINK)
        return self

    def _waiting_logo_opencart(self):
        self._verify_element_presence(self.HEADER_LOGO_OPENCART)
        return self
