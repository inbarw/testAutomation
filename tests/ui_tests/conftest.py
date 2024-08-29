import pytest
from selenium import webdriver
from config.config_ui import Config
from pages.login_page import LoginPage

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def login_by_password(browser):
    browser.get(Config.BASE_URL)
    login_page = LoginPage(browser)
    credentials = Config.LOGIN_CREDENTIALS
    login_page.enter_by_password(credentials["password"])