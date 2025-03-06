
class Course:
    def __init__(self, course_id):
        self.__course_id = course_id
        self.__student_list = []

    @property
    def course_id(self):
        return self.__course_id

    @course_id.setter
    def course_id(self, course_id):
        self.__course_id = course_id

    def get_student_list(self):
        return self.__student_list



