
class Course:
    def __init__(self, course_id):
        self.__course_id = course_id
        self.__course_dictionary = {}

    @property
    def course_id(self):
        return self.__course_id

    @course_id.setter
    def course_id(self, course_id):
        self.__course_id = course_id

    def add_student(self):
        self.__course_dictionary[self.__course_id] = []

    def get_course_dictionary(self):
        return self.__course_dictionary

