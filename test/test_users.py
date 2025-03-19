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

    def test_facilitator_list_increases_with_add(self):
        self.manager.create_facilitator_list("firstname1", "lastname", "email", "password")
        self.assertEqual(2, self.manager.facilitator_length())

    def test_if_facilitator_can_login(self):
        self.manager.create_facilitator_list("firstname1", "lastname", "email", "password")
        self.manager.facilitator_loging("email", "password")
        actual = self.manager.check_facilitator_logged_in("email")
        self.assertEqual(True, actual)

    def test_if_facilitator_course_list_is_printed(self):
        self.manager.create_facilitator_list("firstname1", "lastname", "email", "password")
        self.manager.create_course_by_a_facilitator("email", "CHE-101")
        self.manager.create_course_by_a_facilitator("email", "CHE-102")
        actual = self.manager.printing_courses_of_a_facilitator("email")
        expected = "CHE-101\nCHE-102\n"
        self.assertEqual(expected, actual)

    def test_facilitator_login(self):
        self.manager.create_facilitator_list("firstname1", "lastname", "email", "password")
        self.manager.facilitator_loging("email", "password")
        self.assertEqual(True, self.manager.check_facilitator_logged_in("email"))
