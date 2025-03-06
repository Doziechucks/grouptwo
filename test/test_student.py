from unittest import TestCase
from src.studentmanagement.students import StudentManagement

class TestStudent(TestCase):
    def setUp(self):
        self.student = StudentManagement("firstname", "lastname", "email", "password")

    def test_add_course(self):
        self.assertEqual(0, self.student.get_course_list_size())
        self.student.add_course("CHE-101")
        self.assertEqual(1, self.student.get_course_list_size())