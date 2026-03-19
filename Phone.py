import phonenumbers

phone_number = phonenumbers.parse("+number")  # Replace with your phone number
valid = phonenumbers.is_valid_number(phone_number)