from selenium.webdriver.common.by import By
from .BasePage import BasePage


class RegisterPage(BasePage):
    FORM_INPUT_PI = (By.ID, "account")
    INPUT_NO_NEWSLETTER = (By.CSS_SELECTOR, ".radio-inline input[value='0']")
    LINK_ON_LOGIN_PAGE = (By.LINK_TEXT, "login page")
    BUTTON_SUBMIT = (By.CSS_SELECTOR, "input[type='submit']")
