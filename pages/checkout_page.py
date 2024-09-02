from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import Base

class CheckoutPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.total_cost = (By.XPATH, "//span[text()='Total']/ancestor::div[@role='row']/descendant::div[contains(@class,'fragempf')]")
        self.contact_field = (By.ID, "email")
        self.first_name_field = (By.CSS_SELECTOR, "input[name='firstName']")
        self.last_name_field = (By.CSS_SELECTOR, "input[name='lastName']")
        self.address_field = (By.CSS_SELECTOR, "input[name='address1']")
        self.apartment_field = (By.CSS_SELECTOR, "input[name='address2']")
        self.postal_code_field = (By.CSS_SELECTOR, "input[name='postalCode']")
        self.city_field = (By.CSS_SELECTOR, "input[name='city']")
        self.country_dropdown = (By.CSS_SELECTOR, "select[name='countryCode']")
        self.card_number_field = (By.CSS_SELECTOR, "input#number")
        self.expiration_field = (By.CSS_SELECTOR, "input#expiry")
        self.security_code_field = (By.CSS_SELECTOR, "input#verification_value")
        self.name_on_card_field = (By.CSS_SELECTOR, "input#name")
        self.shipping_checkbox = (By.ID, "billingAddress")
        self.pay_now_button = (By.ID, "checkout-pay-button")
        self.calculating_price_message = (By.XPATH, "//span[contains(text(),'Calculating')]")
        self.shipping_price = (By.XPATH, "//span[text()='£23.99']")
        self.invalid_field_error = (By.XPATH, "//p[text()='ERROR_TEXT']")
        self.payment_section = (By.CSS_SELECTOR, "section[aria-label='Payment']")
        self.card_number_iframe = (By.XPATH, "//div[@id='number']/iframe")
        self.expiry_iframe = (By.XPATH, "//div[@id='expiry']/iframe")
        self.security_code_iframe = (By.XPATH, "//div[@id='verification_value']/iframe")
        self.name_on_card_iframe = (By.XPATH, "//div[@id='name']/iframe")

    def get_total_cost(self):
        self.wait_for_element_not_to_be_visible(self.calculating_price_message)
        self.wait_for_element_to_be_visible(self.shipping_price)
        return self.find_element(*self.total_cost).text.split('\n')[-1]

    def fill_contact(self, contact_details):
        self.find_element(*self.contact_field).send_keys(contact_details)

    def chose_country(self, country):
        self.select_dropdown_option(*self.country_dropdown, country)

    def fill_first_name(self, first_name):
        self.find_element(*self.first_name_field).send_keys(first_name)

    def fill_last_name(self, last_name):
        self.find_element(*self.last_name_field).send_keys(last_name)

    def fill_address(self, address):
        self.find_element(*self.address_field).send_keys(address)

    def fill_apartment(self, apartment):
        self.find_element(*self.apartment_field).send_keys(apartment)

    def fill_postal_code(self, postal_code):
        self.find_element(*self.postal_code_field).send_keys(postal_code)

    def fill_city(self, city):
        self.find_element(*self.city_field).send_keys(city)

    def fill_delivery(self, country, first_name, last_name, address, apartment, postal_code, city):
        if country != '':
            self.chose_country(country)
        if first_name != '':
            self.fill_first_name(first_name)
        self.fill_last_name(last_name)
        self.fill_address(address)
        if apartment != '':
            self.fill_apartment(apartment)
        if postal_code != '':
            self.fill_postal_code(postal_code)
        self.fill_city(city)

    def fill_card_number(self, card_number):
        self.switch_to_iframe(self.card_number_iframe)
        self.find_element(*self.card_number_field).send_keys(card_number)
        self.switch_to_default_iframe()

    def fill_expiration_date(self, expiration_date):
        self.switch_to_iframe(self.expiry_iframe)
        self.find_element(*self.expiration_field).send_keys(expiration_date)
        self.switch_to_default_iframe()

    def fill_security_code(self, security_code):
        self.switch_to_iframe(self.security_code_iframe)
        self.find_element(*self.security_code_field).send_keys(security_code)
        self.switch_to_default_iframe()

    def fill_name_on_card(self, name):
        self.switch_to_iframe(self.name_on_card_iframe)
        name_on_card_element = self.find_element(*self.name_on_card_field)
        name_on_card_element.clear()
        name_on_card_element.send_keys(name)
        self.switch_to_default_iframe()

    def fill_payment(self, card_number, expiration_date, security_code, name_on_card):
        self.fill_card_number(card_number)
        self.fill_expiration_date(expiration_date)
        self.fill_security_code(security_code)
        self.fill_name_on_card(name_on_card)

    def click_pay_now(self):
        self.find_element(*self.pay_now_button).click()

    def fill_checkout_fields(self, contact, country, first_name, last_name, address, apartment, postal_code, city, card_number, expiration_date,
                             security_code, name_on_card):
        self.fill_contact(contact)
        self.fill_delivery(country, first_name, last_name, address, apartment, postal_code, city)
        self.fill_payment(card_number, expiration_date, security_code, name_on_card)
        self.click_pay_now()

    def validate_invalid_field_error(self, error_text):
        try:
            error_locator =(self.invalid_field_error[0], self.invalid_field_error[1].replace("ERROR_TEXT", error_text))
            return self.find_element(*error_locator)
        except NoSuchElementException:
            return None

    def verify_payment_section(self):
        try:
            return self.find_element(*self.payment_section)
        except NoSuchElementException:
            return None
