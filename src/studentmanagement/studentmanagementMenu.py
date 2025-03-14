from src.studentmanagement.users import UserManagement
import re


from src.studentmanagement.exception import passwordException, passwordValidateException, emailException, \
    validate_email, nameValidationException, nameException

users = UserManagement()

def main_menu():
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
                    main_menu()
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
    logger = login_in(checker)
    if logger != "":
        facilitator_choice(logger)





def login_in(checker):
    email = input("Please enter your email: ")
    password = input("Please enter your password: ")
    if checker == 1:
        users.facilitator_loging(email, password)
        print(users.check_facilitator_logged_in(email))
        while not users.check_facilitator_logged_in(email):
            print("Invalid login attempt")
            email = input("Please enter your facilitator email: ")
            password = input("Please enter your facilitator password: ")
            users.facilitator_loging(email, password)
        else:
            print("Login successful")
    if checker == 2:
        users.student_login(email, password)
        while not users.check_student_logged_in(email):
            print("Invalid login attempt")
            email = input("Please enter your email: ")
            password = input("Please enter your password: ")
            users.facilitator_loging(email, password)
        else:
            print("Login successful")
    return email

def register(check):
    done = False
    firstname = ""
    while not done:
        try:
            firstname = input("Please enter your first name: ")
            if not re.search("[A-Za-z]", firstname):
                raise nameException
            else: done = True
        except nameValidationException as e:
            print(f"Invalid first name: {e}")

    move = False
    lastname = ""
    while not move:
        try:
            lastname = input("Please enter your last name: ")
            if not re.search("[A-Za-z]", lastname):
                raise nameException
            else: move = True
        except nameValidationException as e:
            print(f"Invalid last name: {e}")

    facilitator_password = ""
    pass_check = False
    while not pass_check:

        try:
            facilitator_password = input("Please enter your password: ")
            if not re.search("[A-Za-z0-9]", facilitator_password) or len(facilitator_password) < 4:
                raise passwordException
            else: pass_check = True
        except passwordValidateException as e:
            print(f"invalid password: {e}")

    facilitator_email = ""
    mail_check = False
    while not mail_check:
        try:
            facilitator_email = input("Please enter your email: ")
            validate_email(facilitator_email)
            pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
            if not re.match(pattern, facilitator_email):
                raise emailException(facilitator_email)
            else: mail_check = True
        except emailException as e:
            print(f"Invalid email: {e}")

    if check == 1:
        users.create_facilitator_list(firstname, lastname, facilitator_email, facilitator_password)
        print("Facilitator list created")
    elif check == 2:
        users.create_student_list(firstname, lastname, facilitator_email, facilitator_password)

def facilitator_choice(email):
    option = input("""
    1. create course
    2. show my courses
    3. get student offering a course
    4. grade student
    """)

    match option:
        case "1":
            create_course(email)
        case "2":
            show_courses(email)
        case "3":
            get_course_students(email)
        case "4":
            grade_student(email)
        case _:
            main_menu()

def create_course(email):
    course_id = input("Please enter course id: ")
    users.create_course_by_facilitator(course_id, email)
    facilitator_choice(email)

def show_courses(email):
     users.printing_courses_of_a_facilitator(email)
     facilitator_choice(email)

def get_course_students(email):
    users.print_a_course_grade_for_a_facilitator(email)
    facilitator_choice(email)

def grade_student(email):
    course_id = input("Please enter course id: ")
    student_email = input("Enter your student email: ")
    grade = input("Please enter grade for student: ")
    users.grade_a_particular_course(course_id, student_email, grade, email)
    facilitator_choice(email)






main_menu()