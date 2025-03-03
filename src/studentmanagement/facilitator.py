class Facilitator:

    def __init__(self, firstName, lastName, email, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.idNumber = idNumber
        self.courses = []
        self.student = {}

    def setScore(self, studentID, courseID, score):
        if courseID in self.courses and studentID in self.student:
            if 'scores' not in self.student[studentID]:
                self.student[studentID]['scores'] = {}
            self.student[studentID]['scores'][courseID] = score
        else:
            raise ValueError("Course or student not found.")

    def createCourse(self,courseName):
        if courseName not in self.courses:
            self.courses.append(courseName)
            return f'Course {courseName} has been created'
        else:
            raise ValueError("Course Name already exists")

    def setGrades(self, studentID, courseID, grade):
        if courseID in self.courses and studentID in self.student:
            self.courses[studentID]['grades'][courseID] = grade
        else:
            raise ValueError("Course ID or Student ID not found")

    def viewStudentList(self):
        studentList = []
        for studentId,studentInfo in self.student.items():
            studentList.append({
                'studentID': studentId,
                'firstName': studentInfo['firstName'],
                'lastName': studentInfo['lastName'],
                'score': studentInfo['score'],
                'grades': studentInfo['grades']
            })
        return studentList

    def editCourses(self, oldCourseName, newCourseName):
        if oldCourseName in self.courses:
            self.courses[self.courses.index(oldCourseName)] = newCourseName
            for studentId,studentInfo in self.student.items():
                if oldCourseName in studentInfo['scores']:
                    studentInfo['scores'][newCourseName] = studentInfo['scores'].pop(oldCourseName)
                if oldCourseName in studentInfo['grades']:
                    studentInfo['grades'][newCourseName] = studentInfo['grades'].pop(oldCourseName)
            return f"Course '{oldCourseName}' renamed to '{newCourseName}' successfully."
        else:
            raise ValueError("Course not found.")

    def addStudent(self, studentId, firstName, secondName):
        if studentId not in self.student:
            self.student[studentId] = {
                'firstName': firstName,
                'secondName': secondName,
                'scores': {},
                'grades': {}
            }
            return f"Student '{firstName} {secondName}' added successfully."
        else:
            raise ValueError("Student already exists.")
