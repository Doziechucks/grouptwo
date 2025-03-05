import unittest

from src.studentmanagement.corsesOffered import CoursesOffered


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.coursesOffered = CoursesOffered("English","STU12")

    def test_that_create_courses(self):
        self.assertEqual(self.coursesOffered.createCourses("English","STU12"), "Course STU12 already exists")

if __name__ == '__main__':
    unittest.main()
