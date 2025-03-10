import pickle
import json
import re
from unittest import case

from pyexpat.errors import messages

from src.studentmanagement.exception import passwordException, passwordValidateException, emailException, \
    validate_email, nameValidationException, nameException

global facilitator_email
facilitatorEmail = ''

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


def facilitatorLogin():
            print("""
            Welcome to facilitator login
            
            """)
            facilitator_password = input("Please enter your facilitator password: ")
            if len(facilitator_password) < 8:
                print("Your facilitator password must be at least 8 characters long")
                facilitatorLogin()
            else:
                print("Your facilitator password saved successfully.")

            try:
                if not re.search("[A-Za-z0-9]", facilitator_password):
                    raise passwordException
            except passwordValidateException as e:
                print(f"invalid password: {e}")

            try:
                facilitator_email = input("Please enter your facilitator email: ")
                validateEmail = validate_email(facilitator_email)

                # if facilitator_email != facilitatorEmail:
                #     print("Enter correct Email!!!")
                # else:
                #     facilitatorLogin()
                print(f"Valid facilitator emailAddress: {validateEmail} saved successfully")
                pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
                if not re.match(pattern, facilitator_email):
                    raise emailException(facilitator_email)
                return facilitator_email
            except emailException as e:
                print(f"Invalid email: {e}")


def facilitatorRegister():
    menu = input("""
        ~~~~Facilitator register platform ~~~~
        1. Register to facilitator
        2.Create course and assign grades
        3. View Student courses
        0.Logout
    """)
    match(menu):
        case "1":
            register()
        case "0":
            mainMenu()
        case _:
            print("Enter correct input!!!")

def register():
    firstName = input("Please enter your first name: ")
    try:
        if not re.search("[A-Za-z]", firstName):
            raise nameException
    except nameValidationException as e:
        print(f"Invalid first name: {e}")
        register()
    secondName = input("Please enter your last name: ")
    try:
        if not re.search("[A-Za-z]", secondName):
            raise nameException
    except nameValidationException as e:
            print(f"Invalid last name: {e}")
            register()

    facilitatorEmail = input("Please enter your facilitator email: ")
    try:
        validateEmail = validate_email(facilitatorEmail)
        print(f"Valid emailAddress: {validateEmail} saved successfully")

        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(pattern, facilitatorEmail):
            raise emailException(facilitatorEmail)
        return facilitatorEmail
    except emailException as e:
        print(f"Invalid email: {e}")
        register()





# def createCourseAndAssignGrades():




mainMenu()