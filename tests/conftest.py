from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as service_chrome
from selenium.webdriver.edge.service import Service as service_edge


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture(scope='class')
def driver(request):
    browser = request.config.getoption('--browser')
    if browser == 'edge':
        service = service_edge()
        driver = webdriver.Edge(service=service)
    else:
        service = service_chrome()
        driver = webdriver.Chrome(service=service)
    driver.get('https://rahulshettyacademy.com/angularpractice/')
    driver.maximize_window()
    # request.cls.driver = driver - assign the class driver variable to driver
    yield driver
    sleep(10)
    driver.close()


@pytest.fixture(params=[('Racahana', 'rachana@gmail.com', 'Female'), ('AAkash', 'Sharma', 'Male'), ('AAkash', 'Sharma', 'Male')])
def getData(request):
    return request.param
