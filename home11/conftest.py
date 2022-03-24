import logging

import pytest
import requests
import allure
import time
import json

from selenium import webdriver


@allure.step("Waiting for resource availability {url}")
def wait_url_data(url, timeout=20):
    while timeout:
        response = requests.get(url)
        if not response.ok:
            time.sleep(1)
            timeout -= 1
        else:
            if 'video' in url:
                return response.content
            else:
                return response.text
    return None


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
# https://github.com/pytest-dev/pytest/issues/230#issuecomment-402580536
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.outcome != 'passed':
        item.status = 'failed'
    else:
        item.status = 'passed'


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--tolerance", type=int, default=3)
    parser.addoption("--executor", default="192.168.0.4")
    parser.addoption("--versiya", action="store", default="95.0")
    parser.addoption("--vnc", action="store_true", default=True)
    parser.addoption("--logs", action="store_true", default=False)
    parser.addoption("--video", action="store_true", default=False)
    parser.addoption("--picture", action="store_true", default=False)
    parser.addoption("--opencart_url", default="http://192.168.0.4:8081/")


@pytest.fixture
def browser(request):
    # Сбор параметров запуска для pytest
    browser = request.config.getoption("--browser")
    tolerance = request.config.getoption("--tolerance")
    executor = request.config.getoption("--executor")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    video = request.config.getoption("--video")
    version = request.config.getoption("--versiya")
    picture = request.config.getoption("--picture")
    base_url = request.config.getoption("--opencart_url")

    executor_url = f"http://{executor}:4444/wd/hub"

    capabilities = {
        "browserName": browser,
        "browserVersion": version,
        "screenResolution": "1920x1080",
        "selenoid:options": {
            "enableVNC": vnc,
            "enableVideo": video,
            "enableLog": logs
        },
        "name": "QAPython"
    }

    driver = webdriver.Remote(
        command_executor=executor_url,
        desired_capabilities=capabilities
    )

    # Attach browser data
    allure.attach(
        name=driver.session_id,
        body=json.dumps(driver.capabilities),
        attachment_type=allure.attachment_type.JSON)

    def finalizer():
        log_url = f"{executor}/logs/{driver.session_id}.log"
        video_url = f"http://{executor}:8080/video/{driver.session_id}.mp4"
        driver.quit()

        if request.node.status != 'passed':
            if logs:
                allure.attach(
                    name="selenoid_log_" + driver.session_id,
                    body=wait_url_data(log_url),
                    attachment_type=allure.attachment_type.TEXT)
            if picture:
                allure.attach(
                    body=driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=allure.attachment_type.PNG
                )
            if video:
                allure.attach(
                    body=wait_url_data(video_url),
                    name="video_for_" + driver.session_id,
                    attachment_type=allure.attachment_type.MP4)

        # Clear video and logs from selenoid
        if video and wait_url_data(video_url):
            requests.delete(url=video_url)

        if logs and wait_url_data(log_url):
            requests.delete(url=log_url)

        # Add environment info to allure-report
        with open("allure-results/environment.xml", "w+") as file:
            file.write(f"""<environment>
                    <parameter>
                        <key>Browser</key>
                        <value>{browser}</value>
                    </parameter>
                    <parameter>
                        <key>Browser.Version</key>
                        <value>{version}</value>
                    </parameter>
                    <parameter>
                        <key>Executor</key>
                        <value>{executor_url}</value>
                    </parameter>
                </environment>
                """)

    def open_page(path=''):
        with allure.step(f"Открываю {base_url + path}"):
            return driver.get(base_url + path)

    driver.open_page = open_page
    driver.test_name = request.node.name
    driver.log_level = logging.DEBUG
    driver.t = tolerance
    driver.base_url = base_url

    request.addfinalizer(finalizer)
    return driver
