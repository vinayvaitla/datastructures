"""
This is an ADT which is used to create an Array
"""


class SingleArray:
    data = []
    used_size = 0

    def __init__(self, total_size):
        self.total_size = total_size
        self.data = [0]*total_size

    def print_array(self):
        print(self.data)

    def set_value(self,value):
        self.data[self.used_size] = value
        self.used_size = self.used_size + 1

    def get_total_size(self):
        return self.total_size

    def get_used_size(self):
        return self.used_size