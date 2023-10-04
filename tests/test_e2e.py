from time import sleep

import pytest
from selenium.webdriver.common.by import By

from pageObjects.homePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self, driver, getData):
        home_page = HomePage(driver)
        home_page.sent_name(getData[0])
        print("E2e test")
        driver.refresh()

    def test_e2e_second(self, driver, getData):
        home_page = HomePage(driver)
        home_page.send_email(getData[1])
        self.wait_for_element(home_page.name, driver)
        home_page.select_gender(getData[2])
        print("e2e second")
        driver.refresh()
