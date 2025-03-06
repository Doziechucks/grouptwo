from src.studentmanagement.user import User


class CourseAdmin(User):
    def __init__(self, firstname, lastname, email, password):
        super().__init__(firstname, lastname, email, password)
        self.__course_list = []



    def create_course(self, course_name, course_id, facilitator_name, facilitator_email):
        course_information = [course_name, course_id, facilitator_name, facilitator_email]
        self.__course_list.append(course_information)

    def get_course_list(self):
        return self.__course_list




