from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from home6.pages.MainPage import MainPage
from home6.pages.CatalogPage import CatalogPage
from home6.pages.ProductPage import ProductPage
from home6.pages.RegisterPage import RegisterPage
from home6.pages.LoginAdminPage import LoginAdminPage


def test_main_page(browser):
    browser.open()
    MainPage(browser)._verify_element_presence((By.ID, "logo"))
    MainPage(browser)._element(MainPage.TEXT_CATEGORIES)
    MainPage(browser)._element(MainPage.BUTTON_SEARCH)
    MainPage(browser)._element(MainPage.FIRST_SWIPER)
    MainPage(browser)._element(MainPage.lINK_ON_MY_ACCOUNT)


def test_catalog_page(browser):
    browser.open(path="/smartphone")
    CatalogPage(browser)._verify_element_presence((By.ID, "logo"))
    CatalogPage(browser)._element(CatalogPage.COUNTER_CART)
    CatalogPage(browser)._element(CatalogPage.BUTTON_IN_CARD)
    CatalogPage(browser)._element(CatalogPage.LINK_ON_COMPARE)
    CatalogPage(browser)._element(CatalogPage.TITLE_CATEGORIES)


def test_product_page(browser):
    browser.open(path="/camera/canon-eos-5d")
    ProductPage(browser)._verify_element_presence((By.ID, "logo"))
    ProductPage(browser)._element(ProductPage.TAB_DESCRIPTION)
    ProductPage(browser)._element(ProductPage.OLD_PRICE)
    ProductPage(browser)._element(ProductPage.LINK_ON_BRAND)
    ProductPage(browser)._element(ProductPage.INPUT_QUANTITY)


def test_register_page(browser):
    browser.open(path="/index.php?route=account/register")
    RegisterPage(browser)._verify_element_presence((By.ID, "logo"))
    RegisterPage(browser)._element(RegisterPage.FORM_INPUT_PI)
    RegisterPage(browser)._element(RegisterPage.INPUT_NO_NEWSLETTER)
    RegisterPage(browser)._element(RegisterPage.LINK_ON_LOGIN_PAGE)
    RegisterPage(browser)._element(RegisterPage.BUTTON_SUBMIT)


def test_login_admin_page(browser):
    browser.open(path="/admin")
    LoginAdminPage(browser)._verify_element_presence((By.ID, "header-logo"))
    LoginAdminPage(browser)._element(LoginAdminPage.PANEL_HEADING)
    LoginAdminPage(browser)._element(LoginAdminPage.SUBMIT_BUTTON)
    LoginAdminPage(browser)._element(LoginAdminPage.FORGOTTEN_PASSWORD)
    LoginAdminPage(browser)._element(LoginAdminPage.OPENCART_LINK)
