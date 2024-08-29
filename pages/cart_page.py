from selenium.webdriver.common.by import By
from pages.base_page import Base

class CartPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.check_out_button = (By.ID, "checkout")

    def go_to_checkout(self):
        self.find_element(*self.check_out_button).click()