from selenium.webdriver.common.by import By
from pages.base_page import Base

class HeaderMenu(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.catalog_link = (By.CSS_SELECTOR, "a[href='/collections/all']")
        self.search_icon = (By.CSS_SELECTOR, "svg[class*='modal__toggle-open']")
        self.search_field = (By.ID, "Search-In-Modal")
        self.product_option = (By.XPATH, "//h3[text()='PRODUCT_NAME']")
        self.cart_icon = (By.ID, "cart-icon-bubble")

    def search_product_from_catalog(self, product_name):
        self.driver.execute_script("arguments[0].click();", self.find_element(*self.catalog_link))
        self.find_element(*self.search_icon).click()
        self.find_element(*self.search_field).send_keys(product_name)
        product_option_locator = (self.product_option[0], self.product_option[1].replace("PRODUCT_NAME", product_name))
        self.wait_for_element_to_be_visible(product_option_locator)
        self.find_element(*product_option_locator).click()

    def go_to_cart(self):
        self.find_element(*self.cart_icon).click()
