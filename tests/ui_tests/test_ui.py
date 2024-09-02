from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.confirmation_page import ConfirmationPage
from pages.header_menu import HeaderMenu
from pages.product_page import ProductPage
from utils.check_out_data import set_checkout_delivery_data, set_checkout_card_number_data

def test_positive(browser, login_by_password):
    header_menu = HeaderMenu(browser)
    header_menu.search_product_from_catalog("Dropit Hamburger (QA Automation)")
    product_page = ProductPage(browser)
    assert product_page.get_product_name() == "Dropit Hamburger (QA Automation)"
    product_page.add_product_to_cart({"Medium": 2, "So large you can't eat it": 1})

    header_menu.search_product_from_catalog("Dropit Chips (QA Automation)")
    assert product_page.get_product_name() == "Dropit Chips (QA Automation)"
    product_page.add_product_to_cart({"Large": 2, "Too much for you to handle": 1})

    header_menu.go_to_cart()

    cart_page = CartPage(browser)
    cart_page.go_to_checkout()

    check_out_page = CheckoutPage(browser)
    assert check_out_page.get_total_cost() == "£56.99"

    user_delivery_data = set_checkout_delivery_data("", "Bogus", "Gateway", "test address", "4", "6100000", "Tel Aviv")
    user_card_data = set_checkout_card_number_data("1", "12/26", "777", "Bogus Gateway")
    check_out_page.fill_checkout_fields("test@gmail.com", user_delivery_data["country"], user_delivery_data["first_name"], user_delivery_data["last_name"],
                                        user_delivery_data["address"], user_delivery_data["apartment"], user_delivery_data["postal_code"], user_delivery_data["city"],
                                        user_card_data["card_number"], user_card_data["expiration_date"], user_card_data["security_code"], user_card_data["name_on_card"])

    confirmation_page = ConfirmationPage(browser)
    assert confirmation_page.get_confirmation_header_text() != None


def test_negative(browser, login_by_password):
    header_menu = HeaderMenu(browser)
    header_menu.search_product_from_catalog("Dropit Hamburger (QA Automation)")
    product_page = ProductPage(browser)
    assert product_page.get_product_name() == "Dropit Hamburger (QA Automation)"
    product_page.add_product_to_cart({"Medium": 1})

    header_menu.search_product_from_catalog("Dropit Chips (QA Automation)")
    assert product_page.get_product_name() == "Dropit Chips (QA Automation)"
    product_page.add_product_to_cart({"Large": 1})

    header_menu.go_to_cart()

    cart_page = CartPage(browser)
    cart_page.go_to_checkout()

    check_out_page = CheckoutPage(browser)
    check_out_page.fill_contact("a")
    user_card_data = set_checkout_card_number_data("", "12", "7777", "")
    check_out_page.fill_payment(user_card_data["card_number"], user_card_data["expiration_date"], user_card_data["security_code"], user_card_data["name_on_card"])
    assert check_out_page.validate_invalid_field_error("Enter a valid email") != None
    assert check_out_page.validate_invalid_field_error("Enter a valid expiration date") != None
    assert check_out_page.validate_invalid_field_error("Enter the CVV or security code on your card") != None
    check_out_page.click_pay_now()
    assert check_out_page.verify_payment_section() != None
    assert check_out_page.validate_invalid_field_error("Enter a card number") != None
    assert check_out_page.validate_invalid_field_error("Enter your name exactly as it’s written on your card") != None

