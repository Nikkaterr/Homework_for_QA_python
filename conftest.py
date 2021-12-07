import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        choices=["chrome", "firefox", "opera", "yandex"]
    )
    parser.addoption(
        "--url",
        action="store",
        default="http://192.168.0.4:8081/",
        help="Local address"
    )
    parser.addoption(
        "--drivers",
        action="store",
        default="C:/Users/katus/Downloads/drivers",
        help="Path for local windows"
    )


@pytest.fixture
def browser(request):
    # Сбор параметров запуска для pytest
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    drivers = request.config.getoption("--drivers")
    service = Service(executable_path=drivers + "/chromedriver.exe")

    if browser == "chrome":
        # В selenium 4 рекомендуют использование такого подхода
        driver = webdriver.Chrome(service=service)
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=drivers + "/geckodriver.exe")
    elif browser == "opera":
        driver = webdriver.Opera(executable_path=drivers + "/operadriver.exe")
    elif browser == "yandex":
        driver = webdriver.Chrome(service=service)

    driver.maximize_window()

    request.addfinalizer(driver.close)

    driver.get(url)
    driver.url = url

    return driver


@pytest.fixture
def wait(browser):
    time_wait = WebDriverWait(browser, 3)
    return time_wait
