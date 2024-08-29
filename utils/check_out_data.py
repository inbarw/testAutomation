def set_checkout_delivery_data(country, first_name, last_name, address, apartment, postal_code, city):
    return {
        "country": country,
        "first_name": first_name,
        "last_name": last_name,
        "address": address,
        "apartment": apartment,
        "postal_code": postal_code,
        "city": city
        }

def set_checkout_card_number_data(card_number, expiration_date, security_code, name_on_card):
    return {
        "card_number": card_number,
        "expiration_date": expiration_date,
        "security_code": security_code,
        "name_on_card": name_on_card,
        }