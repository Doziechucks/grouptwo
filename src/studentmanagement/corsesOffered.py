class CoursesOffered:

    def __init__(self, courses,courseID):
        self.courses = []
        self.coursesID = []

    def create_courses(self, course, course_id):
        if course_id in self.coursesID:
            return f"Course {course_id} already exists"
        self.courses[course_id] = course
        self.coursesID.append(course_id)
        return f"Course {course_id} created successfully"
