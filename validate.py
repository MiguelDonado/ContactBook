import re
from email_validator import validate_email, EmailNotValidError


def main():
    pass


def validation(name=None, address=None, phone=None, email=None, prev_phone=None):
    def validate_name(name):
        name = name.lower().strip()
        if not re.search(r"^[a-z]+\s?(?:[a-z]+)?$", name):
            raise ValueError("The name expression is incorrect")

    def validate_address(address):
        address = address.lower()
        if not re.search(r"^\d{5}, [a-z\s]+$", address):
            raise ValueError("The address expression is incorrect")

    def validate_phone(phone):
        phone = str(phone).strip()
        if not re.search(r"^\d{9}$", phone):
            raise ValueError("The phone expression is incorrect")

    def validating_email(email):
        try:
            v = validate_email(email)
        except EmailNotValidError as e:
            raise ValueError(str(e))

    if name:
        validate_name(name)
    if address:
        validate_address(address)
    if phone:
        validate_phone(phone)
    if email:
        validating_email(email)
    if prev_phone:
        validate_phone(prev_phone)


if __name__ == "__main__":
    main()
