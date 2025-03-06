from src.studentmanagement.users import UserManagement
from unittest import TestCase

class TestUserManagement(TestCase):
    def setUp(self):
        self.manager = UserManagement()

    def test_if_student_offers_course(self):
        self.manager.create_student_list("firstname", "lastname", "email", "password")
        self.manager.add_course("CHE-101", "email")
        actual = self.manager.check_if_student_offers_course("CHE-101", "email")
        expected = True
        self.assertEqual(expected, actual)


    def test_add_student_to_course(self):
        self.manager.create_student_list("firstname", "lastname", "email", "password")
        self.manager.add_course("CHE-101", "email")
        self.manager.create_course_list("CHE-101")
        self.manager.update_student_in_course("CHE-101", "email")
        self.manager.get_course_list()
        actual = self.manager.get_students_offering_a_course("CHE-101")
        expected = "email"
        self.assertEqual(expected, actual)


