import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.support import expected_conditions


@pytest.mark.usefixtures('driver')
class BaseClass:

    def wait_for_element(self, locator, driver):
        wait = WebDriverWait(driver, 15)
        wait.until(expected_conditions.presence_of_element_located(locator))