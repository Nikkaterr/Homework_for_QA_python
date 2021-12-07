import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_main_page(browser, wait):
    browser.get(browser.url)
    wait.until(EC.visibility_of_element_located((By.ID, "logo")))
    browser.find_element(By.XPATH, "//span[text()='Categories']")
    browser.find_element(By.CSS_SELECTOR, "#search button[type='button']")
    browser.find_element(By.CLASS_NAME, "swiper-wrapper")
    browser.find_element(By.XPATH, "//a[text()='My Account']")


def test_catalog_page(browser, wait):
    browser.get(browser.url + "/smartphone")
    wait.until(EC.visibility_of_element_located((By.ID, "logo")))
    browser.find_element(By.ID, "cart-total")
    browser.find_element(By.CLASS_NAME, "button-group")
    browser.find_element(By.LINK_TEXT, "Product Compare (0)")
    browser.find_element(By.XPATH, "//*[text()='Phones & PDAs']")


def test_product_page(browser, wait):
    browser.get(browser.url + "/camera/canon-eos-5d")
    wait.until(EC.visibility_of_element_located((By.ID, "logo")))
    browser.find_element(By.ID, "tab-description")
    browser.find_element(By.CSS_SELECTOR, "span[style*= 'line-through;']")
    browser.find_element(By.LINK_TEXT, "Canon")
    browser.find_element(By.NAME, "quantity")


def test_register_page(browser, wait):
    browser.get(browser.url + "/index.php?route=account/register")
    wait.until(EC.visibility_of_element_located((By.ID, "logo")))
    browser.find_element(By.ID, "account")
    browser.find_element(By.CSS_SELECTOR, ".radio-inline input[value='0']")
    browser.find_element(By.LINK_TEXT, "login page")
    browser.find_element(By.CSS_SELECTOR, "input[type='submit']")


def test_login_page(browser, wait):
    browser.get(browser.url + "/admin")
    wait.until(EC.visibility_of_element_located((By.ID, "header-logo")))
    browser.find_element(By.CLASS_NAME, "panel-heading")
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    browser.find_element(By.LINK_TEXT, "Forgotten Password")
    browser.find_element(By.XPATH, "//*[text()='OpenCart']")
