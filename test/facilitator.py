import unittest

from src.studentmanagement.facilitator import Facilitator


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.facilitator = Facilitator("Akinyemi", "Ayomide", "ayomide@321.com", 12)

    def test_that_create_courses(self):
        self.assertEqual(self.facilitator.createCourse("English"), "Course English has been created")

    def test_create_duplicate_course(self):
        self.facilitator.createCourse("Python Programming")
        with self.assertRaises(ValueError):
            self.facilitator.createCourse("Python Programming")

    def test_that_editCourses(self):
        self.facilitator.createCourse("Python Programming")
        self.assertEqual(self.facilitator.editCourses("Python Programming", "java Programming"),
                         "Course 'Python Programming' renamed to 'java Programming' successfully.")

    def test_that_add_students(self):
        self.assertEqual(self.facilitator.addStudent("STU001", "Akinyemi", "Ayomide"),
                         "Student 'Akinyemi Ayomide' added successfully.")

    def test_set_score(self):
        self.facilitator.createCourse("Python Programming")
        self.facilitator.addStudent("STU001", "Akinyemi", "Ayomide")
        self.facilitator.setScore("STU001", "Python Programming", 85)
        self.assertEqual(self.facilitator.student["STU001"]["scores"]["Python Programming"], 85)

    # def test_view_student_list(self):
    #     self.facilitator.addStudent("STU001", "Efin", "Onyin")
    #     self.facilitator.addStudent("STU002", "Akinyemi", "Ayommide")
    #     self.facilitator.createCourse("Python Programming")
    #     self.facilitator.setScore("STU001", "Python Programming", 85)
    #     self.facilitator.setScore("STU002", "Python Programming", 90)
    #     result = self.facilitator.viewStudentList()
    #     expected_result = [
    #         {
    #             "student_id": "STU001",
    #             "firstName": "Efin",
    #             "lastName": "Onyin",
    #             "courses": {"Python Programming": 85},
    #             "grades": {}
    #         },
    #         {
    #             "student_id": "STU002",
    #             "firstName": "Akinyemi",
    #             "lastName": "Ayomide",
    #             "courses": {"Python Programming": 90},
    #             "grades": {}
    #         }
    #     ]
    #     self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
