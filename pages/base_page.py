from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Base():
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def navigate(self, url):
        self.driver.get(url)

    def find_element(self, by: By, value: str):
        return self.driver.find_element(by, value)

    def wait_for_element_to_be_visible(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.visibility_of_element_located(locator))

    def hover_over_element(self, by: By, value: str):
        element_to_hover = self.find_element(by, value)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_hover).perform()

    def wait_for_element_not_to_be_visible(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.invisibility_of_element_located(locator))

    def switch_to_iframe(self, locator):
        WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it(locator))

    def switch_to_default_iframe(self):
        self.driver.switch_to.default_content()

    def select_dropdown_option(self, by: By, value: str, option: str):
        dropdown_element = self.find_element(by, value)
        select = Select(dropdown_element)
        select.select_by_visible_text(option)

    def wait_for_element_to_be_clickable_and_click(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()