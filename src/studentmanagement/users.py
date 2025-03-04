from src.studentmanagement.user import User
from studentmanagement.courses import Course
from studentmanagement.facilitator import Facilitator
from studentmanagement.students import StudentManagement


class UserManagement:
    def __init__(self, user):
        self.__student_list: list[StudentManagement] = []
        self.__facilitator_list: list[Facilitator] = []
        self.__course_list: list[Course] = []

    def find_course(self, course_id):
        for student in self.__student_list:
            for number in range(len(student.course_list)):
                if student.course_list[number] == course_id:
                    self.__course_list.append(self.__student_list)

    def add_student_to_course(self):
        course = Course().get_course_dictionary()
        for key, value in course.items():
            if key == course_id:
                course[key] = value.append(self.last_name)
                course[key] = value.append(self.email)