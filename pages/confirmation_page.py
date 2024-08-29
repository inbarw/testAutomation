from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import Base

class ConfirmationPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.confirmation_header = (By.XPATH, "//h2[text()='Your order is confirmed']")

    def get_confirmation_header_text(self):
        try:
            self.wait_for_element_to_be_visible(self.confirmation_header)
            return self.find_element(*self.confirmation_header).text
        except NoSuchElementException:
            print("Confirmation header wasn't found")
            return None
