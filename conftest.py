import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


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
    parser.addoption(
        "--tolerance",
        type=int,
        default=3
    )


@pytest.fixture
def browser(request):
    # Сбор параметров запуска для pytest
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    drivers = request.config.getoption("--drivers")
    service = Service(executable_path=drivers + "/chromedriver.exe")
    tolerance = request.config.getoption("--tolerance")

    if browser == "chrome":
        # В selenium 4 рекомендуют использование такого подхода
        driver = webdriver.Chrome(service=service)
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=drivers + "/geckodriver.exe")
    elif browser == "opera":
        driver = webdriver.Opera(executable_path=drivers + "/operadriver.exe")
    elif browser == "yandex":
        driver = webdriver.Chrome(service=service)

    def open(path=""):
        return driver.get(url + path)

    driver.maximize_window()

    driver.open = open
    driver.open()
    driver.t = tolerance

    request.addfinalizer(driver.close)

    return driver
