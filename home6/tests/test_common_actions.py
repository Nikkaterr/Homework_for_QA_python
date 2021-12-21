import pytest
from home6.pages.MainPage import MainPage
from home6.pages.LoginAdminPage import LoginAdminPage
from home6.pages.AdminPage import AdminPage
from home6.pages.RegisterPage import RegisterPage
from home6.pages.elements.AddProductForm import AddProductForm
from selenium.webdriver.common.alert import Alert


def test_change_currency(browser):
    browser.open()
    MainPage(browser) \
        ._click_on_button_currency() \
        ._click_on_pound_button()
    assert MainPage(browser)._find_icon_pound() is True


@pytest.mark.parametrize("product, price, module, quantity",
                         [("Test Product", "25", "Test Module", "5")]
                         )
def test_add_product(browser, product, price, quantity, module):
    browser.open(path="/admin")
    LoginAdminPage(browser).login_with("user", "bitnami")
    AdminPage(browser)._click_on_catalog_link()
    AdminPage(browser)._click_on_product_link()
    AdminPage(browser)._click_on_add_new_product()
    AddProductForm(browser) \
        ._input_product_name(product) \
        ._input_meta_tag_title(product)
    AddProductForm(browser)._click_on_data_tab()
    AddProductForm(browser) \
        ._input_model(module) \
        ._input_price(price) \
        ._input_quantity(quantity)
    AddProductForm(browser)._save()
    AdminPage(browser)._check_success_alert()
    assert AdminPage(browser)._find_product(product) is True


def test_delete_last_product(browser):
    browser.open(path="/admin")
    LoginAdminPage(browser).login_with("user", "bitnami")
    AdminPage(browser)._click_on_catalog_link()
    AdminPage(browser)._click_on_product_link()
    AdminPage(browser)._select_last_product()
    last_product = AdminPage(browser)._get_name_last_product()
    AdminPage(browser)._click_on_delete()
    Alert(browser).accept()
    assert AdminPage(browser)._find_product(last_product) is False


@pytest.mark.parametrize("firstname, lastname, email, telephone, password",
                         [("Ivanov", "Ivan", "ivan@bk.ru", "1234567890", "qwerty")]
                         )
def test_register_new_account(browser, firstname, lastname, email, telephone, password):
    browser.open()
    MainPage(browser) \
        ._click_on_link_my_account() \
        ._click_on_link_page_register()
    RegisterPage(browser) \
        ._input_firstname(firstname) \
        ._input_lastname(lastname) \
        ._input_email(email) \
        ._input_telephone(telephone) \
        ._input_and_confirmed_password(password)
    RegisterPage(browser)._select_yes_newsletter()
    RegisterPage(browser)._set_privacy_policy()
    RegisterPage(browser)._press_continue()
    RegisterPage(browser)._check_successful_creating()
