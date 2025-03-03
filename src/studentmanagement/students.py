from src.studentmanagement.user import User

class StudentManagement(User):
    def __init__(self, firstname, lastname, email, password):
        super().__init__(firstname, lastname, email, password)





    def view_courses(self):
        pass

    def add_course(self):
        pass

    def view_course_lecturer(self, course_name):
        pass

