from src.studentmanagement.user import User

class UserManagement:
    def __init__(self, user):
        self.__users_list: list[User] = []

    def create