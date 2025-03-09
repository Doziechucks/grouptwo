from src.studentmanagement.user import User
from unittest import TestCase

class TestUser(TestCase):
    def setUp(self):
        self.user = User("firstname", "lastname", "email", "password")

    def test_check_password(self):
        self.assertTrue(self.user.check_password("password"))

    def test_if_password_is_changed(self):
        self.user.change_password("password", "lunguboy")
        self.assertTrue(self.user.check_password("lunguboy"))

    def test_if_logged_in_by_default(self):
        self.assertFalse(self.user.is_logged_in)

    def test_if_logged_in(self):
        self.user.log_in()
        self.assertTrue(self.user.is_logged_in)
        self.user.logout()
        self.assertFalse(self.user.is_logged_in)