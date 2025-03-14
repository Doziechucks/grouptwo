from src.studentmanagement.users import UserManagement
import re


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
        match menu:
                case "1":
                    facilitator_register()
                case "2":
                    facilitator_login()
                case "3":
                    student_register()
                case "4":
                    student_login()
                case "0":
                    mainMenu()
                case _:
                    print("Enter correct input!!!")


def facilitator_register():
    check = 1
    register(check)


def student_register():
    check = 2
    register(check)


def student_login():
    checker = 2
    login_in(checker)

def facilitator_login():
    checker = 1
    login_in(checker)


def login_in(checker):
    email = input("Please enter your email: ")
    password = input("Please enter your password: ")
    if checker == 1:
        users.facilitator_loging(email, password)
        while not users.check_facilitator_logged_in(email):
            print("Invalid login attempt")
            email = input("Please enter your facilitator email: ")
            password = input("Please enter your facilitator password: ")
            users.facilitator_loging(email, password)
    if checker == 2:
        users.student_login(email, password)
        while not users.check_student_logged_in(email):
            print("Invalid login attempt")
            email = input("Please enter your email: ")
            password = input("Please enter your password: ")
            users.facilitator_loging(email, password)

def register(check):
    firstname = input("Please enter your first name: ")
    try:
        if not re.search("[A-Za-z]", firstname):
            raise nameException
    except nameValidationException as e:
        print(f"Invalid first name: {e}")

    lastname = input("Please enter your last name: ")
    try:
        if not re.search("[A-Za-z]", lastname):
            raise nameException
    except nameValidationException as e:
        print(f"Invalid last name: {e}")

    facilitator_password = input("Please enter your password: ")
    try:
        if not re.search("[A-Za-z0-9]", facilitator_password) or len(facilitator_password) < 4:
            raise passwordException
    except passwordValidateException as e:
        print(f"invalid password: {e}")

    facilitator_email = input("Please enter your email: ")
    try:
        validateEmail = validate_email(facilitator_email)
        print(f"Valid emailAddress: {validateEmail} saved successfully")
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(pattern, facilitator_email):
            raise emailException(facilitator_email)
        return facilitator_email
    except emailException as e:
        print(f"Invalid email: {e}")
    if check == 1:
        users.create_facilitator_list(firstname, lastname, facilitator_email, facilitator_password)
    elif check == 2:
        users.create_student_list(firstname, lastname, facilitator_email, facilitator_password)




mainMenu()