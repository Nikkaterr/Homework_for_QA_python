import logging
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    LOGO_OPENCART = (By.ID, "logo")

    def __init__(self, browser, wait=3):
        self.browser = browser
        self.wait = WebDriverWait(browser, wait)
        self.actions = ActionChains(browser)
        self.__config_logger()

    def __config_logger(self, to_file=False):
        self.logger = logging.getLogger(type(self).__name__)
        os.makedirs("logs", exist_ok=True)
        if to_file:
            self.logger.addHandler(logging.FileHandler(f"logs/{self.browser.test_name}.log"))
        self.logger.setLevel(level=self.browser.log_level)

    def _open(self, url="http://192.168.0.4:8081", path=""):
        self.logger.info(f"Opening url: {url+path}")
        return self.browser.get(url + path)

    def _verify_element_presence(self, locator: tuple):
        self.logger.info(f"Check if element {locator} is present")
        try:
            return WebDriverWait(self.browser, self.browser.t).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(locator))

    def _element(self, locator: tuple):
        self.logger.info(f"Find element: {locator}")
        return self.browser.find_element(*locator)

    def _click(self, locator: tuple):
        self.logger.info(f"Clicking element: {locator}")
        element = self._element(locator)
        ActionChains(self.browser).pause(0.10).move_to_element(element).click(element).perform()

    def _waiting_logo_opencart(self):
        self.logger.info(f"Check if element Logo Opencart is present")
        self._verify_element_presence(self.LOGO_OPENCART)
        return self
