from selenium.webdriver.common.by import By
from pages.base_page import Base

class LoginPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.password_field = (By.ID, "password")
        self.enter_button = (By.CSS_SELECTOR, "button[type='submit']")

    def fill_password(self, password):
        self.find_element(*self.password_field).send_keys(password)

    def enter_by_password(self, password):
        self.fill_password(password)
        self.find_element(*self.enter_button).click()