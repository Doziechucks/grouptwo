class Student:
    def _init_(self, user_id, name, email, password):
        super()._init_(user_id, name, email, password)
        self.courses = []

    def view_courses(self):
        for course in self.courses:
            print(course)