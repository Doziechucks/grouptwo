from src.studentmanagement.courses import Course
from src.studentmanagement.facilitator import Facilitator
from src.studentmanagement.students import StudentManagement
from src.studentmanagement.writetofile import WriteToFile
import os

from studentmanagement import courses


class UserManagement:
    def __init__(self):
        self.__student_list: list[StudentManagement] = []
        self.__facilitator_list: list[Facilitator] = []
        self.__course_list = []
        self.__course_list_names = []
        self.__all_emails_list: list[str] = []

    def create_student_list(self, firstname, lastname, email, password):
        if len(self.__student_list) == 0 and os.path.exists("students.txt"):
            my_list = WriteToFile.read_from_file("students.txt")
            self.__student_list = [my_object for my_object in my_list]
            for student in self.__student_list:
                self.__all_emails_list.append(student.email)
            self.write_student(firstname, lastname, email, password)
        else:
            self.write_student(firstname, lastname, email, password)

    def create_facilitator_list(self, firstname, lastname, email, password):
        if len(self.__facilitator_list) == 0 and os.path.exists("facilitators.txt"):
            my_list = WriteToFile.read_from_file("facilitators.txt")
            self.__facilitator_list = [my_object for my_object in my_list]
            for facilitator in self.__facilitator_list:
                self.__all_emails_list.append(facilitator.email)
        else:
            self.write_facilitator(firstname, lastname, email, password)

    def create_course_list(self, course_id):
        if len(self.__course_list) == 0 and os.path.exists("courses.txt"):
            my_list = WriteToFile.read_from_file("courses.txt")
            self.__course_list = [my_object for my_object in my_list]
        else:
            course_information = Course(course_id)
            self.__course_list.append(course_information)
            WriteToFile.add_to_file("courses.txt", course_information)

    def check_if_student_offers_course(self, course_id, email):
        for student in self.__student_list:
            for course in student.course_list:
                if course == course_id and email == student.email:
                    return True
        return False

    def update_student_in_course(self, user_course_id, email):
        checker = self.check_if_student_offers_course(user_course_id, email)
        if checker:
            for courses in self.__course_list:
                if courses.course_id == user_course_id:
                    courses.get_student_list().append(email)


    def add_course(self, course_id, user_email):
        for student in self.__student_list:
            if student.email == user_email and self.__course_list.__contains__(course_id):
                student.add_course(course_id)

    def check_if_course_is_in_course_list(self, course_id):
        for course in self.__course_list_names:
            if course.course_id == course_id:
                return True
            return False


    def view_course_offered_by_student(self, email):
        for student in self.__student_list:
            if student.email == email:
                for course in student.course_list:
                    print(course)

    def student_login(self, email, password):
        if len(self.__student_list) == 0 and os.path.exists("students.txt"):
            my_list = WriteToFile.read_from_file("students.txt")
            self.__student_list = [my_object for my_object in my_list]
            for student in self.__student_list:
                self.__all_emails_list.append(student.email)
        for student in self.__student_list:
            if student.email == email and student.check_password(password):

                student.log_in(password)



    def facilitator_loging(self, email, password):
        if len(self.__facilitator_list) == 0 and os.path.exists("facilitators.txt"):
            my_list = WriteToFile.read_from_file("facilitators.txt")
            self.__facilitator_list = [my_object for my_object in my_list]
            for facilitator in self.__facilitator_list:
                self.__all_emails_list.append(facilitator.email)
        for facilitator in self.__facilitator_list:
            if facilitator.email == email and facilitator.check_password(password):
                facilitator.log_in(password)



    def facilitator_logout(self, email):
        for facilitator in self.__facilitator_list:
            if facilitator.email == email:
                facilitator.logout()

    def logout(self, email):
        for student in self.__student_list:
            if student.email == email and student.is_logged_in == True:
                student.logout()
        raise ValueError("cant perform this action")

    def get_course_list(self):
        return self.__course_list

    def get_student_list_of_courses(self):
        for students in self.__student_list:
            for course in students.course_list:
                print(course)

    def get_students_offering_a_course(self, course_id):
        for courses in self.__course_list:
            if courses.course_id == course_id:
                for students in courses.get_student_list():
                    return students
        raise ValueError("cant perform this action")

    def create_course_by_a_facilitator(self, facilitator_email, course_id):
        for facilitator in self.__facilitator_list:
            if facilitator.email == facilitator_email:
                facilitator.create_course_by_facilitator(course_id)

    def get_all_courses(self):
        courses = ""
        for course in self.__course_list:
            courses = courses + str(course) + "\n"

    def add_to_course_list(self):
        for facilitator in self.__facilitator_list:
            for course in facilitator.get_facilitator_course_list():
                self.__course_list.append({str(course)} + "lecturers email:" + {str(facilitator.email)})
                self.__course_list_names.append(course)




    def add_students_email_to_facilitator_course(self, facilitator_email):
        for facilitator in self.__facilitator_list:
            if facilitator.email == facilitator_email:
                facilitator.add_student_emails_to_course()
            else:
                raise ValueError("no facilitator with this email")

    def printing_courses_of_a_facilitator(self, facilitator_email):
        for facilitator in self.__facilitator_list:
            if facilitator.email == facilitator_email:
                return facilitator.print_facilitator_course_list()
            else:
                raise ValueError("no facilitator with this email")

    def grade_a_particular_course(self, course_id, student_email, student_grade, facilitator_email):
        for facilitator in self.__facilitator_list:
            if facilitator.email == facilitator_email:
                self.add_students_email_to_facilitator_course(facilitator_email)
                facilitator.grade_course(course_id)
                facilitator.course_grades(course_id, student_email, student_grade)

    def print_a_course_grade_for_a_facilitator(self, facilitator_email):
        for facilitator in self.__facilitator_list:
            if facilitator.email == facilitator_email:
                facilitator.print_facilitator_grades()

    def print_courses_and_students_of_a_facilitator(self, facilitator_email):
        for facilitator in self.__facilitator_list:
            if facilitator.email == facilitator_email:
                facilitator.print_facilitator_course_list()

    def create_course_by_facilitator(self, facilitator_email, course_id):
        for facilitator in self.__facilitator_list:
            if facilitator.email == facilitator_email:
                facilitator.create_course_by_facilitator(course_id)
                self.__course_list.append(course_id)

    def check_facilitator_logged_in(self, facilitator_email):
        for facilitator in self.__facilitator_list:
            if facilitator.email == facilitator_email and facilitator.is_logged_in == True:
                return True
            else:
                return False

    def check_student_logged_in(self, student_email):
        for student in self.__student_list:
            if student.email == student_email and student.is_logged_in:
                return True
            else:
                return False

    def write_student(self, firstname, lastname, email, password):
        student_information = StudentManagement(firstname, lastname, email, password)
        self.__student_list.append(student_information)
        self.__all_emails_list.append(student_information.email)
        WriteToFile.add_to_file("students.txt", student_information)

    def write_facilitator(self, firstname, lastname, email, password):
        facilitator_information = Facilitator(firstname, lastname, email, password)
        self.__facilitator_list.append(facilitator_information)
        self.__all_emails_list.append(facilitator_information.email)
        WriteToFile.add_to_file("facilitators.txt", facilitator_information)

    def facilitator_length(self):
        return len(self.__facilitator_list)

    def logout_method(self):
        for facilitator in self.__facilitator_list:
            WriteToFile.add_to_file("facilitators.txt", facilitator)
        for student in self.__student_list:
            WriteToFile.add_to_file("students.txt", student)
        for course in self.__course_list:
            WriteToFile.add_to_file("courses.txt", course)


