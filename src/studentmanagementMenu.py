import pickle
import json
import re
from unittest import case

from pyexpat.errors import messages

from src.studentmanagement.exception import passwordException, passwordValidateException, emailException, validate_email


def mainMenu():
    while True:
        menu = input("""
   !!!! Welcome to ADC Student Management System !!!!
        1. Facilitator login
        2. Facilitator register
        3. Student login
        4. Student register
        0.Back
    """)
        match(menu):
                case "1":
                    facilitatorLogin()
                case "0":
                    mainMenu()
                case _:
                    print("Enter correct input!!!")


def facilitatorLogin():
            print("""
            Welcome to facilitator login
            
            """)
            facilitator_password = input("Please enter your facilitator password: ")
            try:
                if not re.search("[A-Za-z0-9]", facilitator_password):
                    raise passwordException

            except passwordValidateException as e:
                print(f"invalid password: {e}")
            if len(facilitator_password) < 8:
                print("Your facilitator password must be at least 8 characters long")

            try:
                facilitator_email = input("Please enter your facilitator email: ")
                validateEmail = validate_email(facilitator_email)
                print(f"Valid facilitator emailAddress: {validateEmail}")

                pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
                if not re.match(pattern, facilitator_email):
                    raise emailException(facilitator_email)
                return facilitator_email
            except emailException as e:
                print(f"Invalid email: {e}")



mainMenu()