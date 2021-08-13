import os
import pytest
from selenium import webdriver

DRIVERS = os.path.expanduser("~\\Downloads\\drivers")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "firefox", "opera"])
    parser.addoption("--url", action="store", default="https://demo.opencart.com/")


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(request):
    _browser = request.config.getoption("--browser")

    if _browser == "chrome":
        driver = webdriver.Chrome(executable_path=f"{DRIVERS}\\chromedriver.exe")
    elif _browser == "opera":
        driver = webdriver.Opera(executable_path=f"{DRIVERS}\\operadriver.exe")
    elif _browser == "firefox":
        driver = webdriver.Firefox(executable_path=f"{DRIVERS}\\geckodriver.exe")

    request.addfinalizer(driver.quit)
    return driver
