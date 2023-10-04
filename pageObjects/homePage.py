from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    name = (By.CSS_SELECTOR, '[name="name"]')
    email = (By.CSS_SELECTOR, '[name="email"]')
    gender = (By.ID, 'exampleFormControlSelect1')

    # -------------- Locator --------------------------

    def get_name_locator(self):
        return self.driver.find_element(*HomePage.name)

    def get_email_locator(self):
        return self.driver.find_element(*HomePage.email)

    def get_gender_locator(self):
        return self.driver.find_element(*HomePage.gender)

    # ----------------Action -------------------------

    def sent_name(self, text):
        self.get_name_locator().send_keys(text)

    def send_email(self, text):
        self.get_email_locator().send_keys(text)

    def select_gender(self, text):
        sel = Select(self.get_gender_locator())
        sel.select_by_visible_text(text)
