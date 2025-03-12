import os
class FileHandler:

    def __init__(self, file):
        self.__set_file(file)

    def __set_file(self, file):
        self.__file= os.path.abspath(file)

    def write(self, content:str) -> None:
        try:
            with open(self.__file, 'a') as file:
                file.write(content+'\n')
        except FileNotFoundError:
            with open(self.__file, 'w') as file:
                file.write(content+'\n')

    def read(self) -> [str]:
        try:
            with open(self.__file, 'r') as file:
                return file.read().split('\n')[:-1]
        except FileNotFoundError:
            with open(self.__file, 'w') as file:
                file.write('')
            return self.read()