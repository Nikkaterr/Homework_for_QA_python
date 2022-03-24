from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pages.BasePage import BasePage


class AdminPage(BasePage):
    NAVIGATION_BUTTON = (By.ID, "button-menu")
    PRODUCT_LINK = (By.XPATH, "//*[text()='Products']")
    CATALOG_LINK = (By.ID, "menu-catalog")
    ADD_NEW_PRODUCT = (By.CSS_SELECTOR, "a[data-original-title='Add New']")
    SUCCESS_ALERT = (By.CLASS_NAME, "alert-success")
    DELETE_PRODUCT = (By.CSS_SELECTOR, "button[data-original-title='Delete']")
    CHECKBOX_LAST_PRODUCT = (By.CSS_SELECTOR, "tbody tr:last-child > td:first-child > input[type='checkbox']")
    LAST_PRODUCT = (By.XPATH, "//tbody/tr[last()]/td[3]")

    def _click_on_catalog_link(self):
        self._click(self.CATALOG_LINK)
        return self

    def _click_on_product_link(self):
        self._click(self.PRODUCT_LINK)
        return self

    def _click_on_add_new_product(self):
        self._click(self.ADD_NEW_PRODUCT)
        return self

    def _find_product(self, name_product):
        try:
            self._element((By.XPATH, f"//td[text()='{name_product}']"))
        except NoSuchElementException:
            return False
        return True

    def _check_success_alert(self):
        self._verify_element_presence(self.SUCCESS_ALERT)

    def _select_last_product(self):
        self._click(self.CHECKBOX_LAST_PRODUCT)

    def _click_on_delete(self):
        self._click(self.DELETE_PRODUCT)

    def _get_name_last_product(self):
        element = self.browser.find_element(*self.LAST_PRODUCT)
        return element.text
