import pickle

class WriteToFile:
    @staticmethod
    def add_to_file(filename, input_object):
        with open(filename, "wb") as file:
            pickle.dump(input_object, file)

    @staticmethod
    def read_from_file(filename):
        object_list =[]
        with open(filename, "rb") as file:
            while True:
                try:
                    input_object = pickle.load(file)
                    object_list.append(input_object)
                except EOFError:
                    break
        return object_list




