class User:
    def __init__(self, first_name, last_name, email, password):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__password = password
        self.__is_logged_in = False

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    def check_password(self, password):
        if self.__password == password:
            return True
        else:
            return False

    def change_password(self, old_password, new_password):
        if self.check_password(old_password):
            self.__password = new_password
        else:
            raise ValueError("Password doesn't match")

    @property
    def is_logged_in(self):
        return self.__is_logged_in

    def log_in(self, password):
        if self.check_password(password):
            self.__is_logged_in = True

    def logout(self):
        self.__is_logged_in = False

