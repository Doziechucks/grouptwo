class Course:
    def __init__(self, course_id, facilitator_name, facilitator_email):
        self.__course_id = course_id
        self.__facilitator_name = facilitator_name
        self.__facilitator_email = facilitator_email

    @property
    def course_id(self):
        return self.__course_id

    @course_id.setter
    def course_id(self, course_id):
        self.__course_id = course_id

    @property
    def facilitator_name(self):
        return self.__facilitator_name

    @facilitator_name.setter
    def facilitator_name(self, facilitator_name):
        self.__facilitator_name = facilitator_name

    @property
    def facilitator_email(self):
        return self.__facilitator_email

    @facilitator_email.setter
    def facilitator_email(self, facilitator_email):
        self.__facilitator_email = facilitator_email

    def get_course(self):
        return "" + self.__course_id + " " + self.__facilitator_name + " " + self.__facilitator_email +""
