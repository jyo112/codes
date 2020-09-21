import pytest
from selenium import webdriver
from drivers.driverfactory import *
@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    df=DriverFactory(browser)
    driver=df.getWebDriverInstance()
    if request.cls is not None:
        request.cls.driver = driver
    yield
    driver.quit()
def pytest_addoption(parser):
    parser.addoption("--browser", help="Type of operating system")
#
@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

