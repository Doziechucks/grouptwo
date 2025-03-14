from src.studentmanagement.facilitator import Facilitator
from unittest import TestCase

class TestFacilitator(TestCase):
    def setUp(self):
        self.facilitator = Facilitator("firstname", "lastname", "email", "password")

    def test_if_facilitator_can_create_a_course(self):
        self.facilitator.create_course_by_facilitator("course_id")
        self.assertEqual(1, self.facilitator.get_length_of_course_list())


