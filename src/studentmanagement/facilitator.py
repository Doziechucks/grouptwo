from src.studentmanagement.user import User

class Facilitator(User):
    def __init__(self, firstname, lastname, email, password, course_name):
        super().__init__(firstname, lastname, email, password)
        self.__course_name = course_name
        self.__course_dictionary = {}

    @property
    def course_name(self):
        return self.__course_name

    @course_name.setter
    def course_name(self, course_name):
        self.__course_name = course_name

    def create_course(self, course_name):
        self.__course_dictionary[self.__course_name] = []

