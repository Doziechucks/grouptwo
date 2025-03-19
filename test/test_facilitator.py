from src.studentmanagement.facilitator import Facilitator
from unittest import TestCase

class TestFacilitator(TestCase):
    def setUp(self):
        self.facilitator = Facilitator("firstname", "lastname", "email", "password")

    def test_if_facilitator_can_create_a_course(self):
        self.facilitator.create_course_by_facilitator("course_id")
        self.facilitator.create_course_by_facilitator("course_id2")
        self.assertEqual(2, self.facilitator.get_length_of_course_list())

    def test_if_print_facilitator_course_works(self):
        self.facilitator.create_course_by_facilitator("course_id")
        self.facilitator.create_course_by_facilitator("course_id2")
        expected = "course_id\ncourse_id2\n"
        self.assertEqual(expected, self.facilitator.print_facilitator_course_list())


