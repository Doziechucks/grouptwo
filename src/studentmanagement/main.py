from src.studentmanagement.users import UserManagement

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
 # Press ⌘F8 to toggle the breakpoint.
user = UserManagement()
email = input("enter email: ")
password = input("enter password: ")
user.student_login(email, password)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
