class CoursesOffered:

    def __init__(self, courses):
        self.courses = {}
        self.coursesID = []

    def createCourses(self, courses, courseID):
        if courses in self.courses and courseID in self.coursesID:
            return f"Course {courseID} already exists"