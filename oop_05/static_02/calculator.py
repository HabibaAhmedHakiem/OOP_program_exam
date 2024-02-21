# attributes  { length, width, color, model }
class calculator:
    def __init__(self, length, width, color, model):
        self.__length = length
        self.__width = width
        self.__color = color
        self.__model = model

        # accessors [ Getters & setters ]

    def get_length(self, length):
        self.__length =length

    def set_length(self, length):
        self.__length + length

    # extra Methods

# instance method : because it depends on instance attributes : __length, __width
    def calc_body_area(self):
        return self.__length * self.__width

    # static method : because it doesn't depend on instant attributes -
    # result doesn't change from object to another for the same parameter
    # self is not put as a parameter as it doesn't need it so it's removed
    @staticmethod
    def add(a, b):
        return a + b

    @ staticmethod
    def subtract(a, b):
        return  a - b





