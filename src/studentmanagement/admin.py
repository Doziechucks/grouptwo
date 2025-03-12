from src.studentmanagement.user import User
from src.studentmanagement.course import Course


class CourseAdmin(User):
    def __init__(self, firstname, lastname, email, password):
        super().__init__(firstname, lastname, email, password)
        self.__course_list = []



    def create_course(self,  course_id, facilitator_name, facilitator_email):
        course_information = Course(course_id, facilitator_name, facilitator_email)
        self.__course_list.append(course_information)

    def get_course_id(self):
        for course in self.__course_list:
            return course.course_id

    def get_course_facilitator(self):
        for course in self.__course_list:
            return course.facilitator_email

    def get_facilitator_email(self):
        for course in self.__course_list:
            return course.facilitator_email

    def get_course_list(self):
        return self.__course_list

    def get_course_and_instructor(self):
        for course in self.__course_list:
            return course.get_course()




