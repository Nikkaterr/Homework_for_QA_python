from home6.pages.MainPage import MainPage
from home6.pages.CatalogPage import CatalogPage
from home6.pages.ProductPage import ProductPage
from home6.pages.RegisterPage import RegisterPage
from home6.pages.LoginAdminPage import LoginAdminPage


def test_main_page(browser):
    browser.open()
    MainPage(browser)._waiting_logo_opencart()
    MainPage(browser)._find_text_categories()
    MainPage(browser)._find_button_search()
    MainPage(browser)._find_first_swiper()
    MainPage(browser)._find_link_on_my_account()


def test_catalog_page(browser):
    browser.open(path="/smartphone")
    CatalogPage(browser)._waiting_logo_opencart()
    CatalogPage(browser)._find_counter_cart()
    CatalogPage(browser)._find_title_categories()
    CatalogPage(browser)._find_link_on_compare()
    CatalogPage(browser)._find_counter_cart()


def test_product_page(browser):
    browser.open(path="/camera/canon-eos-5d")
    ProductPage(browser)._waiting_logo_opencart()
    ProductPage(browser)._find_tab_description()
    ProductPage(browser)._find_old_price()
    ProductPage(browser)._find_link_on_brand()
    ProductPage(browser)._find_input_quantity()


def test_register_page(browser):
    browser.open(path="/index.php?route=account/register")
    RegisterPage(browser)._waiting_logo_opencart()
    RegisterPage(browser)._find_form_input_pi()
    RegisterPage(browser)._find_input_no_newsletter()
    RegisterPage(browser)._find_link_on_login_page()
    RegisterPage(browser)._find_button_submit()


def test_login_admin_page(browser):
    browser.open(path="/admin")
    LoginAdminPage(browser)._waiting_logo_opencart()
    LoginAdminPage(browser)._find_panel_heading()
    LoginAdminPage(browser)._find_submit_button()
    LoginAdminPage(browser)._find_forgotten_password()
    LoginAdminPage(browser)._find_submit_button()
