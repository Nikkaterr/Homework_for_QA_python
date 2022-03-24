import pytest
from pages.MainPage import MainPage
from pages.LoginAdminPage import LoginAdminPage
from pages.AdminPage import AdminPage
from pages.RegisterPage import RegisterPage
from pages.elements.AddProductForm import AddProductForm
from selenium.webdriver.common.alert import Alert
import allure


@allure.title('Изменение валюты на сайте')
def test_change_currency(browser):
    browser.open_page()
    with allure.step("Клик на иконку смены валюты и выбор фунта"):
        MainPage(browser) \
            ._click_on_button_currency() \
            ._click_on_pound_button()
    with allure.step("Проверка иконки фута на сайте"):
        assert MainPage(browser)._find_icon_pound() is True


@allure.title('Добавление товара в каталог')
@pytest.mark.parametrize("product, price, module, quantity",
                         [("Test Product", "25", "Test Module", "5")]
                         )
def test_add_product(browser, product, price, quantity, module):
    login = "user"
    password = "bitnami"
    browser.open_page(path='/admin')
    with allure.step(f"Заходим в систему под админом c логином: {login}, паролем: {password}"):
        LoginAdminPage(browser).login_with(login, password)
    with allure.step("Раскрываем меню"):
        AdminPage(browser)._click_on_catalog_link()
    with allure.step("Выбираем пункт 'Product' из меню"):
        AdminPage(browser)._click_on_product_link()
    with allure.step("Жмём на кнопку добавить новый продукт"):
        AdminPage(browser)._click_on_add_new_product()
        with allure.step(f"Вводим имя продукта и тэг {product}"):
            AddProductForm(browser) \
                ._input_product_name(product) \
                ._input_meta_tag_title(product)
        with allure.step("Переходим на следующую страницу заполнения данных о товаре"):
            AddProductForm(browser)._click_on_data_tab()
        with allure.step(f"Указываем модуль: {module}, цену: {price}, количество {quantity}"):
            AddProductForm(browser) \
                ._input_model(module) \
                ._input_price(price) \
                ._input_quantity(quantity)
        with allure.step("Сохраняем изменения"):
            AddProductForm(browser)._save()
    with allure.step("Ждём подтверждения успешного добавления нового продукта"):
        AdminPage(browser)._check_success_alert()
    with allure.step("Находим новый товар в списке всех товаров"):
        assert AdminPage(browser)._find_product(product) is True


@allure.title('Удаление товара из каталога')
def test_delete_last_product(browser):
    login = "user"
    password = "bitnami"
    browser.open_page(path='/admin')
    with allure.step(f"Заходим в систему под админом c логином: {login}, паролем: {password}"):
        LoginAdminPage(browser).login_with(login, password)
    with allure.step("Раскрываем меню"):
        AdminPage(browser)._click_on_catalog_link()
    with allure.step("Выбираем пункт 'Product' из меню"):
        AdminPage(browser)._click_on_product_link()
    with allure.step("Выбираем последний добавленный продукт"):
        AdminPage(browser)._select_last_product()
    with allure.step("Получаем имя выбранного продукта"):
        last_product = AdminPage(browser)._get_name_last_product()
    with allure.step("Удаляем продукт"):
        AdminPage(browser)._click_on_delete()
    with allure.step("Подтверждаем удаление"):
        Alert(browser).accept()
    with allure.step(f"Проверяем что имени удаленного продукта: {last_product} нет в каталоге"):
        assert AdminPage(browser)._find_product(last_product) is False


@allure.title('Регистрация нового пользователя')
@pytest.mark.parametrize("firstname, lastname, email, telephone, password",
                         [("Ivanov", "Ivan", "ivan@bk.ru", "1234567890", "qwerty")]
                         )
def test_register_new_account(browser, firstname, lastname, email, telephone, password):
    browser.open_page()
    with allure.step("Переходим на страницу регистрации"):
        MainPage(browser) \
            ._click_on_link_my_account() \
            ._click_on_link_page_register()
    with allure.step(f"Вводим данные для регистрации: firstname-{firstname}, lastname-{lastname}, email-{email}, "
                     f"telephone-{telephone}, password-{password}"):
        RegisterPage(browser) \
            ._input_firstname(firstname) \
            ._input_lastname(lastname) \
            ._input_email(email) \
            ._input_telephone(telephone) \
            ._input_and_confirmed_password(password)
    with allure.step("Выбираем подписку на новости"):
        RegisterPage(browser)._select_yes_newsletter()
    with allure.step("Подтверждаем что смотрели политику приватности"):
        RegisterPage(browser)._set_privacy_policy()
    with allure.step("Ждём далее"):
        RegisterPage(browser)._press_continue()
    with allure.step("Ждём подтверждение успешной регистрации"):
        RegisterPage(browser)._check_successful_creating()
