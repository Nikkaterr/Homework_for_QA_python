from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class RegisterPage(BasePage):
    FORM_INPUT_PI = (By.ID, "account")
    INPUT_NO_NEWSLETTER = (By.CSS_SELECTOR, ".radio-inline input[value='0']")
    INPUT_YES_NEWSLETTER = (By.CSS_SELECTOR, ".radio-inline input[value='1']")
    LINK_ON_LOGIN_PAGE = (By.LINK_TEXT, "login page")
    BUTTON_SUBMIT = (By.CSS_SELECTOR, "input[type='submit']")
    INPUT_FIRSTNAME = (By.ID, "input-firstname")
    INPUT_LASTNAME = (By.ID, "input-lastname")
    INPUT_EMAIL = (By.ID, "input-email")
    INPUT_TELEPHONE = (By.ID, "input-telephone")
    INPUT_PASSWORD = (By.ID, "input-password")
    INPUT_CONFIRM_PASSWORD = (By.ID, "input-confirm")
    BUTTON_PRIVATE_POLICY = (By.NAME, "agree")
    CONFIRM_CREATING_ACCOUNT = (By.XPATH, "//h1[text()='Your Account Has Been Created!']")

    def _find_form_input_pi(self):
        self._element(self.FORM_INPUT_PI)
        return self

    def _find_input_no_newsletter(self):
        self._element(self.INPUT_NO_NEWSLETTER)
        return self

    def _find_link_on_login_page(self):
        self._element(self.LINK_ON_LOGIN_PAGE)
        return self

    def _find_button_submit(self):
        self._element(self.BUTTON_SUBMIT)
        return self

    def _input_firstname(self, value):
        locator = self.INPUT_FIRSTNAME
        self.logger.info(f"Input {value} in input {locator}")
        self._element(locator).send_keys(value)
        return self

    def _input_lastname(self, value):
        locator = self.INPUT_LASTNAME
        self.logger.info(f"Input {value} in input {locator}")
        self._element(locator).send_keys(value)
        return self

    def _input_email(self, value):
        locator = self.INPUT_EMAIL
        self.logger.info(f"Input {value} in input {locator}")
        self._element(locator).send_keys(value)
        return self

    def _input_telephone(self, value):
        locator = self.INPUT_TELEPHONE
        self.logger.info(f"Input {value} in input {locator}")
        self._element(locator).send_keys(value)
        return self

    def _input_and_confirmed_password(self, value):
        self.logger.info(f"Input password = {value} and confirm")
        self._element(self.INPUT_PASSWORD).send_keys(value)
        self._element(self.INPUT_CONFIRM_PASSWORD).send_keys(value)
        return self

    def _select_yes_newsletter(self):
        self._click(self.INPUT_YES_NEWSLETTER)
        return self

    def _set_privacy_policy(self):
        self._click(self.BUTTON_PRIVATE_POLICY)
        return self

    def _press_continue(self):
        self._click(self.BUTTON_SUBMIT)
        return self

    def _check_successful_creating(self):
                if self._element(self.CONFIRM_CREATING_ACCOUNT):
            return True
        else:
            return False
