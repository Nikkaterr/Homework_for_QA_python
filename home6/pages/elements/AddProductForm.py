from selenium.webdriver.common.by import By
from home6.pages.BasePage import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class AddProductForm(BasePage):
    INPUT_PRODUCT_NAME = (By.ID, "input-name1")
    INPUT_META_TAG_TITLE = (By.ID, "input-meta-title1")
    TAB_DATA = (By.XPATH, "//a[text()='Data']")
    INPUT_MODEL = (By.ID, "input-model")
    INPUT_PRICE = (By.ID, "input-price")
    INPUT_QUANTITY = (By.ID, "input-quantity")
    BUTTON_SAVE = (By.CSS_SELECTOR, "button[type='submit']")

    def _click_input(self, locator: tuple):
        element = self._element(locator)
        ActionChains(self.browser).click(element).perform()

    def _input_product_name(self, name):
        self._click_input(self.INPUT_PRODUCT_NAME)
        element = self._element(self.INPUT_PRODUCT_NAME)
        element.send_keys(Keys.BACK_SPACE)
        element.send_keys(name)
        return self

    def _input_meta_tag_title(self, title):
        self._element(self.INPUT_META_TAG_TITLE).send_keys(title)
        return self

    def _click_on_data_tab(self):
        self._click(self.TAB_DATA)

    def _input_model(self, model):
        self._element(self.INPUT_MODEL).send_keys(model)
        return self

    def _input_price(self, price):
        self._element(self.INPUT_PRICE).send_keys(price)
        return self

    def _input_quantity(self, quantity):
        element = self._element(self.INPUT_QUANTITY)
        element.send_keys(Keys.BACK_SPACE)
        element.send_keys(quantity)
        return self

    def _save(self):
        self._click(self.BUTTON_SAVE)
