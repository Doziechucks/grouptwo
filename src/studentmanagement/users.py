from src.studentmanagement.courses import Course
from src.studentmanagement.facilitator import Facilitator
from src.studentmanagement.students import StudentManagement


class UserManagement:
    def __init__(self):
        self.__student_list: list[StudentManagement] = []
        self.__facilitator_list: list[Facilitator] = []
        self.__course_list: list[Course] = []

    def create_student_list(self, firstname, lastname, email, password):
        student_information = StudentManagement(firstname, lastname, email, password)
        self.__student_list.append(student_information)

    def create_facilitator_list(self, firstname, lastname, email, password):
        facilitator_information = Facilitator(firstname, lastname, email, password)
        self.__facilitator_list.append(facilitator_information)

    def create_course_list(self, course_id):
        course_information = Course(course_id, )
        self.__course_list.append(course_information)

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
            if student.email == user_email:
                student.add_course(course_id)

    def view_course_offered_by_student(self, email):
        for student in self.__student_list:
            if student.email == email:
                for course in student.course_list:
                    print(course)

    def student_login(self, email, password):
        for student in self.__student_list:
            if student.email == email and student.check_password(password):
                student.log_in()
        raise ValueError("Invalid details")

    def logout(self, email):
        for student in self.__student_list:
            if student.email == email and student.is_logged_in == True:
                student.logout()
        raise ValueError("cant perform this action")

    def get_course_list(self):
        return self.__course_list

    def get_student_list_of_courses(self):
        for students in self.__student_list:
            for courses in students.course_list:
                print(courses)

    def get_students_offering_a_course(self, course_id):
        for courses in self.__course_list:
            if courses.course_id == course_id:
                for students in courses.get_student_list():
                    return students
        raise ValueError("cant perform this action")



