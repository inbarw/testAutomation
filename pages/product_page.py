from selenium.webdriver.common.by import By
from pages.base_page import Base

class ProductPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.quantity_add_button = (By.CSS_SELECTOR, "button[name='plus']")
        self.quantity_remove_button = (By.CSS_SELECTOR, "button[name='minus']")
        self.add_to_cart_button = (By.CSS_SELECTOR, "button[name='add']")
        self.product_title = (By.CLASS_NAME, "product__title")
        self.close_cart_notification = (By.CSS_SELECTOR, "button[class*='cart-notification__close modal']")

    def get_product_name(self):
        return self.find_element(*self.product_title).text

    def add_quantity(self, quantity):
        for i in range(quantity - 1):
            self.find_element(*self.quantity_add_button).click()

    def remove_quantity(self, quantity):
        for i in range(quantity - 1):
            self.find_element(*self.quantity_remove_button).click()

    def add_product_to_cart(self, size_quantity_dict):
        for size, quantity in size_quantity_dict.items():
            product_size_locator = (By.XPATH, f"//label[contains(text(),\"{size}\")]")
            self.find_element(*product_size_locator).click()
            self.add_quantity(quantity)
            self.hover_over_element(*self.add_to_cart_button)
            self.find_element(*self.add_to_cart_button).click()
            self.wait_for_element_to_be_visible(self.close_cart_notification)
            self.wait_for_element_to_be_clickable_and_click(self.close_cart_notification)
            self.remove_quantity(quantity)



