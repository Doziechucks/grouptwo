from src.studentmanagement.user import User
from src.studentmanagement.students import StudentManagement
from src.studentmanagement.courses import Course

class Facilitator(User):
    def __init__(self, firstname, lastname, email, password):
        super().__init__(firstname, lastname, email, password)
        self.__student_list: list[StudentManagement] = []
        self.__course_list: list[Course] = []
        self.__facilitator_course_dict = {}
        self.__facilitator_course_list = []
        self.__facilitator_grade = {}

    def create_student(self, firstname, lastname, email, password):
        student_information = StudentManagement(firstname, lastname, email, password)
        self.__student_list.append(student_information)

    def create_course_list(self, course_id):
        course_information = Course(course_id)
        self.__course_list.append(course_information)

    def create_course_by_facilitator(self, course_id):
        self.__facilitator_course_dict[course_id] = []
        self.__facilitator_course_list.append(course_id)

    def add_student_emails_to_course(self):
        for student in self.__student_list:
            for course in student.course_list:
                if course.course_id in self.__facilitator_course_dict.keys():
                    self.__facilitator_course_dict[course.course_id].append(student.email)

    def print_facilitator_course_list(self):
        courses = ""
        for course in self.__facilitator_course_list:
            courses = courses + course + "\n"
            return courses

    def grade_course(self, course_id):
        self.__facilitator_grade[course_id] = []

    def course_grades(self, course_id, email, grade):
        for course in self.__facilitator_course_dict.keys():
            if course == course_id and self.__facilitator_course_dict[course_id] == [email]:
                self.__facilitator_grade[course_id].append(email)
                self.__facilitator_grade[course_id].append(grade)
            else:
                raise ValueError("no student with this email")

    def print_facilitator_grades(self):
        for course in self.__facilitator_grade.keys():
            print(course.course_id, end="")
            for grade in self.__facilitator_grade[course.course_id]:
                print(grade)

    def print_course_students(self):
        for course in self.__facilitator_course_dict:
            print(course.course_id, end="")
            for student in self.__facilitator_course_dict[course.course_id]:
                print(student)

    def get_length_of_course_list(self):
        return len(self.__facilitator_course_list)





        












