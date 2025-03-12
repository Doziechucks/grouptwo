from src.studentmanagement.users import UserManagement
import re
from unittest import case

from pyexpat.errors import messages

from src.studentmanagement.exception import passwordException, passwordValidateException, emailException, \
    validate_email, nameValidationException, nameException

users = UserManagement()

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
    try:
        if not re.search("[A-Za-z0-9]", facilitatorPassword) or len(facilitatorPassword) < 4 :
            raise passwordException
        else:
            print("Your facilitator password saved successfully.")
    except passwordValidateException as e:
        print(f"invalid password: {e}")

    facilitator_email = input("Please enter your facilitator email: ")
    try:
        validateEmail = validate_email(facilitator_email)
        print(f"Valid facilitator emailAddress: {validateEmail} saved successfully")
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(pattern, facilitator_email):
            raise emailException(facilitator_email)
        return facilitator_email
    except emailException as e:
        print(f"Invalid email: {e}")
    users.create_facilitator_list(firstName, secondName, facilitator_email, facilitator_password)


def facilitatorLogin():
    facilitator_email = input("Please enter your facilitator email: ")
    facilitator_pass = input("Please enter your facilitator password: ")
    users.facilitator_loging(facilitator_email, facilitator_pass)
    if users.check_facilitator_logged_in():


        login = input("""
            Lecturer Menu
            1.Create Course
            2.Set Student Score
        """)
def facilitator_password():
    facilitatorPassword = input("Please enter your facilitator password: ")
    if len(facilitatorPassword) < 4:
        print("Your facilitator password must be at least 4 characters long")
        facilitator_password()
    else:
        print("Your facilitator password saved successfully.")
    try:
        if not re.search("[A-Za-z0-9]", facilitatorPassword):
            raise passwordException
    except passwordValidateException as e:
        print(f"invalid password: {e}")


mainMenu()