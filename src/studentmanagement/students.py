from user import User
from admin import CourseAdmin


def view_available_courses():
    course_available = CourseAdmin()
    count = 1
    print("course name,")
    for course in course_available.get_course_list():
        print(f"{count}.")
        for number in range(len(course)):
            print({course[number]}, end= " ")
        count += 1
        print()


class StudentManagement(User):
    def __init__(self, firstname, lastname, email, password):
        super().__init__(firstname, lastname, email, password)
        self.__course_list = []

    @property
    def course_list(self):
        return self.__course_list

    def add_course(self, course_id):
        self.__course_list.append(course_id)

    def view_offered_corurse(self):
        for course in self.__course_list:
            print(f"{course}")




