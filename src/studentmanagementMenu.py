
import re
from unittest import case

from pyexpat.errors import messages

from src.studentmanagement.exception import passwordException, passwordValidateException, emailException, \
    validate_email, nameValidationException, nameException



def mainMenu():
    while True:
        menu = input("""
   !!!! Welcome to ADC Student Management System !!!!
        1. Facilitator register
        2. Facilitator login
        3. Student register
        4. Student login
        0.Back
    """)
        match(menu):
                case "1":
                    facilitatorRegister()
                case "2":
                    facilitatorLogin()
                case "0":
                    mainMenu()
                case _:
                    print("Enter correct input!!!")


def facilitatorRegister():
            firstName = input("Please enter your first name: ")
            try:
                if not re.search("[A-Za-z]", firstName):
                    raise nameException
            except nameValidationException as e:
                print(f"Invalid first name: {e}")

            secondName = input("Please enter your last name: ")
            try:
                if not re.search("[A-Za-z]", secondName):
                    raise nameException
            except nameValidationException as e:
                print(f"Invalid last name: {e}")

            facilitatorPassword = input("Please enter your facilitator password: ")
            if len(facilitatorPassword) < 8:
                print("Your facilitator password must be at least 8 characters long")
                facilitatorLogin()
            else:
                print("Your facilitator password saved successfully.")

            try:
                if not re.search("[A-Za-z0-9]", facilitatorPassword):
                    raise passwordException
            except passwordValidateException as e:
                print(f"invalid password: {e}")

            try:
                facilitator_email = input("Please enter your facilitator email: ")
                validateEmail = validate_email(facilitator_email)


                print(f"Valid facilitator emailAddress: {validateEmail} saved successfully")
                pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
                if not re.match(pattern, facilitator_email):
                    raise emailException(facilitator_email)
                return facilitator_email
            except emailException as e:
                print(f"Invalid email: {e}")


def facilitatorLogin():
    facilitator_password = input("Please enter your facilitator password: ")

    if len(facilitator_password) < 8:
        print("Your facilitator password must be at least 8 characters long")
        facilitatorLogin()
    try:
        if not re.search("[A-Za-z0-9]", facilitator_password):
            raise passwordException
    except passwordValidateException as e:
        print(f"invalid password: {e}")

    facilitatorEmail = input("Please enter your facilitator email: ")
    try:
        validateEmail = validate_email(facilitatorEmail)

        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(pattern, facilitatorEmail):
            raise emailException(facilitatorEmail)
        return facilitatorEmail
    except emailException as e:
        print(f"Invalid email: {e}")
        if facilitator_password == facilitatorPassword:
            print("hi")


mainMenu()