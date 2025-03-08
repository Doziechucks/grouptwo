import re

from pyexpat.errors import messages


class passwordValidateException(Exception):
    pass

class passwordException(passwordValidateException):
    def __init__(self):
            message = f"check your password and try again"
            super().__init__(message)


def validate_email(email_address):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(pattern, email_address):
        raise emailException(email_address)
    return email_address


class emailException(Exception):
    def __init__(self,email):
        message = f"{email} is not a valid email"
        super().__init__(message)

class nameValidationException(Exception):
    pass

class nameException(nameValidationException):
    def __init__(self):
        message = f"It is not a valid name, require only letters"
        super().__init__(message)
