import pickle

class WriteToFile:
    @staticmethod
    def add_to_file(filename, input_object):
        with open(filename, "wb") as file:
            pickle.dump(input_object, file)

    @staticmethod
    def read_from_file(filename):
        with open(filename, "rb") as file:
            pickle.load(file)

