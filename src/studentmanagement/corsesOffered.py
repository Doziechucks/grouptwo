class CoursesOffered:

    def __init__(self, courses,courseID):
        self.courses = {}
        self.coursesID = []

    def createCourses(self, courses, courseID):
        if courses in self.courses and courseID in self.coursesID:
            self.courses[courseID].append(courses)
            self.coursesID.append(courseID)
            return f"Course {courseID} already exists"